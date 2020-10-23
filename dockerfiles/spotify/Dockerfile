FROM local/base:latest

ARG username="skytreader"
RUN apt-get update && \
    apt-get install -y curl wget apt-transport-https libcanberra-gtk-module libgl1-mesa-dri libgl1-mesa-glx alsa-utils libpulse0 xdg-utils && \
    curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | apt-key add - && \
    echo "deb http://repository.spotify.com stable non-free" | tee /etc/apt/sources.list.d/spotify.list && \
    apt-get update && \
    apt-get install -y spotify-client
USER $username
WORKDIR /home/$username
ENTRYPOINT "/usr/bin/spotify"
