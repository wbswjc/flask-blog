FROM python:3.7.2

RUN apt update && apt install vim -y

ENV FLASK_APP flaskr

ADD flask /app

WORKDIR /app

RUN pip install -r requirements.txt
