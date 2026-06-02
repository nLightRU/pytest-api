# Образ Python на базе slim
FROM python:3.11-slim

# Системные зависимости для Allure CLI (Java) и установки poetry
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl unzip default-jre && \
    rm -rf /var/lib/apt/lists/*

# Установка Poetry
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry

# Установка Allure Commandline (версия 2.30.0, можно заменить на актуальную)
RUN curl -sSL https://github.com/allure-framework/allure2/releases/download/2.30.0/allure-2.30.0.zip -o allure.zip && \
    unzip allure.zip -d /opt/ && \
    ln -s /opt/allure-2.30.0/bin/allure /usr/local/bin/allure && \
    rm allure.zip

WORKDIR /app

# Сначала копируем только манифесты зависимостей, чтобы использовать кеш Docker
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости в системный Python (без создания отдельного venv)
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

# Копируем весь исходный код
COPY . .

# Переменная окружения по умолчанию (можно переопределить при запуске)
ENV BOOKING_BASE_URL=http://localhost:8080

# Команда по умолчанию – запуск тестов с генерацией сырых результатов Allure
CMD ["pytest", "--alluredir=allure-results"]