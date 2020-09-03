FROM local/base:latest

ARG username="skytreader"
RUN apt-get update && \
    apt-get install wget apt-transport-https && \
    wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | apt-key add - && \
    echo "deb https://download.sublimetext.com/ apt/stable/" | tee /etc/apt/sources.list.d/sublime-text.list && \
    apt-get update && \
    apt-get install sublime-text
USER $username
WORKDIR /home/$username
ENTRYPOINT "/opt/sublime_text/sublime_text"
