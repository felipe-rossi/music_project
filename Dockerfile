FROM python:latest AS build

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Define a variável de ambiente do Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expõe a porta (Flask roda na 5000 por padrão)
EXPOSE 5000

CMD [ "flask", "run" ]