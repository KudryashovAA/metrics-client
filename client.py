"""Реализация клиента для сервера метрик"""

import socket
from time import time
from typing import Dict, List, Optional, Tuple, Union


class ClientError(Exception):
    """Базовое исключение для всех ошибок клиента."""
    pass


class ClientSocketError(ClientError):
    """Исключение, возникающее при ошибках сетевого соединения.

    Выбрасывается, когда не удается установить соединение с сервером,
    происходит тайм-аут или разрыв соединения во время передачи данных.
    """
    pass


class ClientProtocolError(ClientError):
    """Исключение, возникающее при ошибках протокола обмена с сервером.

    Выбрасывается в следующих случаях:

    - Сервер возвращает статус "error"
    - Некорректный формат ответа от сервера
    - Неизвестный статус ответа
    - Ошибки парсинга данных метрик
    """
    pass


class Client:
    """
    Клиент для взаимодействия с сервером метрик.

    Реализует протокол отправки и получения метрик времени выполнения.
    Поддерживает операции put (сохранение метрики) и get (получение метрик).

    Attributes:

        connection: Кортеж (хост, порт) для подключения к серверу
        timeout: Тайм-аут соединения в секундах

    Example:

        Создание клиента:
          client = Client('127.0.0.1', 8888, timeout=5)

        Отправка метрик:
          client.put('cpu.load', 0.75)  # с текущим временем

          client.put('cpu.load', 0.82, 1609459200)  # с указанным timestamp

        Получение метрик:
          cpu_metrics = client.get('cpu.load')

          # символ '*' используется для получения всех метрик

          all_metrics = client.get('*')
    """

    def __init__(
            self,
            host: str,
            port: int,
            timeout: Optional[int] = None
    ) -> None:
        """
        Инициализация клиента.

        Args:

            host: Адрес сервера (например, 'localhost' или '127.0.0.1')
            port: Порт сервера (например, 8888)
            timeout: Максимальное время ожидания ответа в секундах.
                    Если None - ожидание бесконечное.

        Example:

            client = Client('localhost', 8888, timeout=3)
        """
        self.connection: Tuple[str, int] = (host, port)
        self.timeout: Optional[int] = timeout

    def _send(self, cmd: str) -> str:
        """
        Отправка команды серверу и получение ответа.

        Args:

            cmd: Команда для отправки (должна заканчиваться символом '\\n')

        Returns:

            str: Тело ответа от сервера (данные после строки статуса)

        Raises:

            ClientSocketError: При ошибках соединения
            ClientProtocolError: При ошибках протокола

        Note:

            Формат ответа сервера:
            ok\\n
            <metric1> <value> <timestamp>\\n
            \\n
        """
        data = b""

        try:
            with socket.create_connection(
                    self.connection, self.timeout
            ) as sock:
                sock.sendall(cmd.encode('utf8'))

                while True:
                    part = sock.recv(1024)
                    if not part:
                        break
                    data += part
                    if data.endswith(b'\n\n'):
                        break

        except socket.error as err:
            raise ClientSocketError(
                f'Ошибка соединения с сервером {self.connection[0]}:{self.connection[1]}: {err}'
            ) from err

        if not data:
            raise ClientProtocolError(
                f'Пустой ответ от сервера {self.connection[0]}:{self.connection[1]}'
            )

        try:
            status, payload = data.decode('utf8').split('\n', 1)
            payload = payload.strip()
        except ValueError:
            raise ClientProtocolError(
                f'Некорректный формат ответа от сервера: {data!r}'
            )

        if status == 'error':
            error_msg = payload if payload else 'Неизвестная ошибка'
            raise ClientProtocolError(f'Сервер вернул ошибку: {error_msg}')
        elif status != 'ok':
            raise ClientProtocolError(
                f'Неизвестный статус ответа: {status}'
            )

        return payload

    def put(
            self,
            metric: str,
            value: Union[float, int],
            timestamp: Optional[int] = None
    ) -> None:
        """
        Отправка метрики на сервер.

        Args:

            metric: Имя метрики (например, 'cpu.load')
            value: Значение метрики
            timestamp: Временная метка (если None - используется текущее время)

        Raises:

            ClientSocketError: При ошибках соединения
            ClientProtocolError: При ошибках протокола

        Example:

            client = Client('localhost', 8888)
            client.put('cpu.load', 0.75)
            client.put('memory.used', 1024.5, 1609459200)
        """
        if timestamp is None:
            timestamp = int(time())

        self._send(f'put {metric} {value} {timestamp}\n')

    def get(self, metric_key: str) -> Dict[str, List[Tuple[int, float]]]:
        """
        Получение метрик с сервера.

        Args:

            metric_key: Имя метрики для получения. Специальное значение '*'
                       означает запрос всех метрик.

        Returns:

            Dict[str, List[Tuple[int, float]]]: Словарь с метриками, где
            ключ - имя метрики, значение - список кортежей (timestamp, value),
            отсортированный по timestamp. Если метрика не найдена,
            возвращается пустой словарь.

        Raises:

            ClientSocketError: При ошибках соединения
            ClientProtocolError: При ошибках протокола

        Example:

            client = Client('localhost', 8888)

            # Получение конкретной метрики

            cpu_data = client.get('cpu.load')

            for timestamp, value in cpu_data.get('cpu.load', []):
                print(f'{timestamp}: {value}')

            # Получение всех метрик

            all_data = client.get('*')

            for name, values in all_data.items():
                print(f'{name}: {len(values)} значений')
        """
        result: Dict[str, List[Tuple[int, float]]] = {}
        response = self._send(f'get {metric_key}\n')

        if not response:
            return result

        for line in response.splitlines():
            if not line.strip():
                continue

            try:
                name, value, timestamp = line.split()
                ts = int(timestamp)
                val = float(value)

                if name not in result:
                    result[name] = []
                result[name].append((ts, val))

            except ValueError as error:
                raise ClientProtocolError(
                    f'Ошибка парсинга строки: {line}'
                ) from error

        # Сортировка значений по времени
        for values in result.values():
            values.sort(key=lambda x: x[0])

        return result


if __name__ == '__main__':
    # Пример использования
    client = Client('localhost', 8888, timeout=5)

    try:
        client.put('cpu.load', 0.75)
        client.put('memory.used', 1024.5, int(time()) - 60)

        cpu_data = client.get('cpu.load')
        print('CPU data:', cpu_data)

        all_data = client.get('*')
        print('All metrics:', all_data)

    except ClientSocketError as e:
        print(f'Ошибка соединения: {e}')
    except ClientProtocolError as e:
        print(f'Ошибка протокола: {e}')
    except Exception as e:
        print(f'Ошибка: {e}')