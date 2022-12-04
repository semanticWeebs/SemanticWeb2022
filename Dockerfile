FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app /app

CMD gunicorn --bind 0.0.0.0:$PORT app:app