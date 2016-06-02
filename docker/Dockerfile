FROM ubuntu:xenial
MAINTAINER treylitefm
RUN apt update && apt upgrade -y
RUN apt install -y git wget python python-pip

RUN pip install flask youtube-dl
CMD python server.py
