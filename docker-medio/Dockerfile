FROM ubuntu:xenial
MAINTAINER treylitefm

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python python-pip wget unzip ffmpeg supervisor redis-tools netcat

RUN pip install --upgrade pip
RUN pip install flask flask-cors youtube-dl redis rq
EXPOSE 5000

COPY docker-entrypoint.sh .
ENTRYPOINT ["./docker-entrypoint.sh", "medio-redis-server", "6379"]
