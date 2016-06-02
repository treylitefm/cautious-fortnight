FROM ubuntu
RUN apt update
RUN apt install -y git
RUN apt install -y python
RUN apt install -y python-pip
RUN pip install -y flask
RUN pip install -y youtube-dl
CMD python server.py
