FROM python:3.9.2-slim-buster

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo
ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD src/requirements.txt /app
ADD docker/wait-for-it.sh /usr/local/bin/wait-for-it.sh

RUN apt-get update -y
RUN apt-get update -y
RUN apt-get install -y make bash gcc g++ tzdata vim git
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x /usr/local/bin/wait-for-it.sh
