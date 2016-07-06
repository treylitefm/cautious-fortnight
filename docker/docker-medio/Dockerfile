FROM ubuntu:xenial
MAINTAINER treylitefm

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python python-pip wget unzip ffmpeg supervisor redis-server vim

RUN pip install --upgrade pip
RUN pip install flask flask-cors youtube-dl redis rq

RUN wget https://github.com/treylitefm/medio/zipball/master
RUN unzip master -d /usr/src/ && rm master

#ENTRYPOINT DIR=$(ls /usr/src/) && ln -s /music /usr/src/$DIR/flask/music && python /usr/src/$DIR/flask/server.py
