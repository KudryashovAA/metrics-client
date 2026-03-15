# Создать README.md через echo
echo "# Клиент для сервера метрик" > README.md
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
echo "## Использование" >> README.md
echo "" >> README.md
echo '```python' >> README.md
echo "from client import Client" >> README.md
echo "" >> README.md
echo "client = Client('localhost', 8888, timeout=5)" >> README.md
echo "client.put('cpu.load', 0.75)" >> README.md
echo "cpu_data = client.get('cpu.load')" >> README.md
echo '```' >> README.md
echo "" >> README.md
echo "## Автор" >> README.md
echo "" >> README.md
echo "Алексей Смирнов, 2026" >> README.md

# Проверьте, что файл создался
ls README.md