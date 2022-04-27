
FROM python:3.8-alpine

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --upgrade pip -r requirements.txt

COPY . /app/


