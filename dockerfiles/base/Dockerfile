FROM ubuntu:xenial

ARG userid
ARG username="skytreader"
RUN useradd -m -U -s /bin/bash -u $userid $username

RUN apt-get update && \
    apt-get install -y software-properties-common libgtk-3-0 libappindicator3-1
