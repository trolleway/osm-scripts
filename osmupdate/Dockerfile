FROM ubuntu:18.04
MAINTAINER Artem Svetlov <trolleway@yandex.ru>
RUN apt-get update
RUN apt-get install -y git \
osmctools \
curl \
python


RUN git clone https://github.com/trolleway/osm-scripts.git
WORKDIR osm-scripts/osmupdate

RUN python argstest.py --path "http://example.com"
