FROM local/base:latest

ARG username="skytreader"
RUN add-apt-repository ppa:audio-recorder/ppa && \
    apt-get update && \
    apt-get install -y dbus audio-recorder
USER $username
WORKDIR /home/$username

ENTRYPOINT audio-recorder
