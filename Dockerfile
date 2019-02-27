FROM python:3.7.2
ENV FLASK_APP app.py
ADD flask /app
WORKDIR /app
RUN pip install -r requirements.txt
