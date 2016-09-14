FROM ubuntu:xenial
MAINTAINER treylitefm

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python python-pip wget unzip ffmpeg supervisor redis-tools vim tmux

RUN pip install --upgrade pip
RUN pip install flask flask-cors youtube-dl redis rq

RUN wget https://github.com/treylitefm/medio/zipball/master
RUN mkdir /var/medio
RUN unzip master -d /var/medio/ && rm master
RUN DIR=$(ls /var/medio/) && ln -s /var/medio/$DIR/flask/music /music && ln -s /var/medio/$DIR /var/medio/medio

EXPOSE 5000

ENTRYPOINT HOST=$(echo $DB_PORT_6379_TCP_ADDR) && PORT=$(echo $DB_PORT_6379_TCP_PORT) && cd /var/medio/medio/flask && /usr/bin/python configure.py $HOST $PORT && /usr/bin/supervisord -c /var/medio/medio/flask/supervisord.conf && /bin/bash
