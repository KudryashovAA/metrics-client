# Создать README.md через echo
echo "# Клиент для сервера метрик" > README.md
echo "" >> README.md
echo "[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://KudryashovAA.github.io/metrics-client/)" >> README.md
echo "" >> README.md
echo "Клиент для взаимодействия с сервером метрик по текстовому протоколу через TCP сокеты." >> README.md
echo "" >> README.md
echo "## Возможности" >> README.md
echo "" >> README.md
echo "- Отправка метрик на сервер (put)" >> README.md
echo "- Получение метрик с сервера (get)" >> README.md
echo "- Поддержка символа '*' для получения всех метрик" >> README.md
echo "- Автоматическая подстановка текущего времени" >> README.md
echo "- Обработка сетевых ошибок и ошибок протокола" >> README.md
echo "" >> README.md
echo "## Документация" >> README.md
echo "" >> README.md
echo "Готовая документация доступна по адресу:" >> README.md
echo "**[https://KudryashovAA.github.io/metrics-client/](https://KudryashovAA.github.io/metrics-client/)**" >> README.md
echo "" >> README.md
echo "### Сборка документации локально" >> README.md
echo "" >> README.md
echo '```bash' >> README.md
echo "cd docs" >> README.md
echo "make html        # для Linux/Mac" >> README.md
echo "# или" >> README.md
echo "make.bat html    # для Windows" >> README.md
echo "" >> README.md
echo "# Открыть документацию" >> README.md
echo "open build/html/index.html        # для Mac" >> README.md
echo "start build/html/index.html       # для Windows" >> README.md
echo "xdg-open build/html/index.html    # для Linux" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "## Установка" >> README.md
echo "" >> README.md
echo '```bash' >> README.md
echo "git clone https://github.com/KudryashovAA/metrics-client.git" >> README.md
echo "cd metrics-client" >> README.md
echo "pip install -r requirements.txt" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "## Использование" >> README.md
echo "" >> README.md
echo '```python' >> README.md
echo "from client import Client" >> README.md
echo "" >> README.md
echo "client = Client('localhost', 8888, timeout=5)" >> README.md
echo "client.put('cpu.load', 0.75)" >> README.md
echo "cpu_data = client.get('cpu.load')" >> README.md
echo "print(cpu_data)" >> README.md
echo "# {'cpu.load': [(1609459200, 0.75)]}" >> README.md
echo "" >> README.md
echo "# Получение всех метрик" >> README.md
echo "all_metrics = client.get('*')" >> README.md
echo "for metric, values in all_metrics.items():" >> README.md
echo "    print(f'{metric}: {len(values)} значений')" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "## Примеры с обработкой ошибок" >> README.md
echo "" >> README.md
echo '```python' >> README.md
echo "from client import Client, ClientSocketError, ClientProtocolError" >> README.md
echo "" >> README.md
echo "client = Client('localhost', 8888, timeout=5)" >> README.md
echo "" >> README.md
echo "try:" >> README.md
echo "    client.put('temperature', 23.5)" >> README.md
echo "    data = client.get('temperature')" >> README.md
echo "    print(data)" >> README.md
echo "except ClientSocketError as e:" >> README.md
echo "    print(f'Ошибка соединения: {e}')" >> README.md
echo "except ClientProtocolError as e:" >> README.md
echo "    print(f'Ошибка протокола: {e}')" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "## Требования" >> README.md
echo "" >> README.md
echo "- Python 3.7 или выше" >> README.md
echo "- Sphinx (для сборки документации)" >> README.md
echo "" >> README.md
echo "## Зависимости" >> README.md
echo "" >> README.md
echo '```' >> README.md
echo "sphinx==7.2.6" >> README.md
echo "sphinx-rtd-theme==2.0.0" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "## Структура проекта" >> README.md
echo "" >> README.md
echo '```' >> README.md
echo "metrics-client/" >> README.md
echo "├── client.py              # основной код клиента" >> README.md
echo "├── README.md              # документация проекта" >> README.md
echo "├── requirements.txt       # зависимости" >> README.md
echo "├── .gitignore             # игнорируемые файлы" >> README.md
echo "└── docs/                  # документация Sphinx" >> README.md
echo "    ├── Makefile" >> README.md
echo "    ├── make.bat" >> README.md
echo "    └── source/" >> README.md
echo "        ├── conf.py" >> README.md
echo "        ├── index.rst" >> README.md
echo "        └── api.rst" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "## Устранение неполадок" >> README.md
echo "" >> README.md
echo "### Ошибка соединения" >> README.md
echo "" >> README.md
echo '```python' >> README.md
echo "client = Client('127.0.0.1', 8888)  # вместо 'localhost'" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "### Документация не собирается" >> README.md
echo "" >> README.md
echo '```bash' >> README.md
echo "cd docs" >> README.md
echo "make clean" >> README.md
echo "make html" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "## Автор" >> README.md
echo "" >> README.md
echo "Алексей Кудряшов, 2026" >> README.md
echo "" >> README.md
echo "## Лицензия" >> README.md
echo "" >> README.md
echo "MIT License" >> README.md
echo "" >> README.md
echo "Copyright (c) 2026 Алексей Кудряшов" >> README.md
echo "" >> README.md
echo "Permission is hereby granted, free of charge, to any person obtaining a copy" >> README.md
echo "of this software and associated documentation files (the 'Software'), to deal" >> README.md
echo "in the Software without restriction, including without limitation the rights" >> README.md
echo "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell" >> README.md
echo "copies of the Software, and to permit persons to whom the Software is" >> README.md
echo "furnished to do so, subject to the following conditions:" >> README.md
echo "" >> README.md
echo "The above copyright notice and this permission notice shall be included in all" >> README.md
echo "copies or substantial portions of the Software." >> README.md
echo "" >> README.md
echo "THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR" >> README.md
echo "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY," >> README.md
echo "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE" >> README.md
echo "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER" >> README.md
echo "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM," >> README.md
echo "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE" >> README.md
echo "SOFTWARE." >> README.md
echo "" >> README.md
echo "---" >> README.md
echo "" >> README.md
echo "**Проект разработан в 2026 году.**" >> README.md

# Проверьте, что файл создался
ls README.md
echo "README.md успешно создан с ссылкой на документацию!"