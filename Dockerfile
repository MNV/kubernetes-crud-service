# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip -r /requirements.txt

RUN mkdir /src
WORKDIR /src
COPY ./src /src

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /

EXPOSE 8000

ENTRYPOINT ["python", "app.py"]
