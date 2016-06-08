FROM ubuntu:xenial
MAINTAINER treylitefm

RUN apt update && apt upgrade -y
RUN apt install -y python python-pip wget unzip ffmpeg

RUN pip install --upgrade pip
RUN pip install flask flask-cors youtube-dl

RUN wget https://github.com/treylitefm/medio/zipball/master
RUN unzip master -d /usr/src/ && rm master

ENTRYPOINT DIR=$(ls /usr/src/) && ln -s /music /usr/src/$DIR/flask/music && python /usr/src/$DIR/flask/server.py
