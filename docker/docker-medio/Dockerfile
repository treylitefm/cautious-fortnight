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

WORKDIR /var/medio/medio/flask

COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh", "medio-redis-server", "6379"]
