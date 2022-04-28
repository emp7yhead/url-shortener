
FROM python:3.8-alpine

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --upgrade pip -r requirements.txt

COPY . /app/

ENTRYPOINT [ "gunicorn" ]

CMD [ "-w" , "4", "--bind", "0.0.0.0:10000", "wsgi:app" ]


