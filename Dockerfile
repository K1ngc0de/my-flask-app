FROM python:3.13-slim

# Устанавливаем рабочую директорию
WORKDIR /venv

# Копируем все файлы из текущей директории в контейнер
COPY . /venv

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем зависимости для тестов (например, pytest)
RUN pip install pytest

# Открываем порт 5000
EXPOSE 5000

# Указываем команду для запуска тестов по умолчанию (можно заменить на app.py для продакшн)
CMD ["pytest"]
