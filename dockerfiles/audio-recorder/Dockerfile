FROM local/base:latest

ARG username="skytreader"
RUN add-apt-repository ppa:audio-recorder/ppa && \
    apt-get update && \
    apt-get install -y dbus audio-recorder
COPY system.conf /etc/dbus-1/system.conf
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
USER $username
WORKDIR /home/$username

ENTRYPOINT /docker-entrypoint.sh
