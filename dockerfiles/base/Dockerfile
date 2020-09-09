FROM ubuntu:xenial

ARG userid
ARG username="skytreader"
RUN useradd -m -U -s /bin/bash -u $userid $username

RUN apt-get update && \
    apt-get install -y software-properties-common libgtk-3-0 libappindicator3-1 locales
RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_CTYPE=en_US.UTF-8

VOLUME /home/$username
