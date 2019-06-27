FROM ubuntu:18.04
MAINTAINER Artem Svetlov <trolleway@yandex.ru>
RUN apt-get update
RUN apt-get install -y git \
osmctools \
curl 

RUN git clone https://github.com/trolleway/osm-scripts.git
WORKDIR osm-scripts/osmupdate

