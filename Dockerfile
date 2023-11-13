FROM python:3.8-slim

WORKDIR /app

COPY . /app
COPY default.conf /etc/nginx/nginx.conf

RUN apt-get update \
    && apt-get upgrade\
    && apt-get install -y gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

ENV NAME venv

CMD ["python", "app.py"]
