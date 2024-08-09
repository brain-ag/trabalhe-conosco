FROM python:3.11.7-slim

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1

# Diretório de trabalho
RUN mkdir /app
WORKDIR /app
EXPOSE 8000

# Instalar dependências do sistema, incluindo wget
RUN apt-get update && apt-get install -y \
    build-essential \
    libmagic-dev \
    libjpeg-dev \
    libgif-dev \
    libcairo2-dev \
    pkg-config \
    libpq-dev \
    python3-dev \
    wget \
    gnupg

# Copiar e instalar dependências do Python

COPY requirements.txt .
COPY requirements requirements

RUN pip install -r requirements.txt

# Copiar código fonte
COPY manage.py .
COPY app app
COPY fixtures fixtures

# Rodar coletar estáticos e iniciar o servidor
CMD ["sh", "-c", "python manage.py collectstatic --no-input && gunicorn app.infrastructure.framework.django.config.wsgi:application --timeout 180 --workers 3 --bind 0.0.0.0:8000"]
