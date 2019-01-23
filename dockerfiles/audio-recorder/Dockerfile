FROM local/base:latest

RUN add-apt-repository ppa:audio-recorder/ppa && \
    apt-get update && \
    apt-get install -y audio-recorder

ENTRYPOINT audio-recorder
