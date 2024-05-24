FROM python:3.10-buster

RUN apt-get update && \
    apt-get install -y cron

RUN pip install poetry==1.8.0

RUN pip install pipx && \
    pipx ensurepath

RUN pipx install poethepoet

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

COPY . .

RUN cat /app/crontab > /etc/crontab

CMD ["poetry", "run", "uvicorn", "app.web:app", "--host", "0.0.0.0", "--port", "8000"]
