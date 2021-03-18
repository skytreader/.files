FROM local/base:latest

ARG username="skytreader"
RUN apt-get update && \
    apt-get install -y curl wget apt-transport-https libcanberra-gtk-module libgl1-mesa-dri libgl1-mesa-glx alsa-utils libpulse0 xdg-utils libpangoxft-1.0 && \
    wget https://launchpad.net/ubuntu/+archive/primary/+files/libgcrypt11_1.5.3-2ubuntu4.2_amd64.deb && \
    dpkg -i libgcrypt11_1.5.3-2ubuntu4.2_amd64.deb && \
    curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | apt-key add - && \
    #apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 931FF8E79F0876134EDDBDCCA87FF9DF48BF1C90 && \
    echo "deb http://repository.spotify.com stable non-free" | tee /etc/apt/sources.list.d/spotify.list && \
    apt-get update && \
    apt-get install -y spotify-client-0.9.17
USER $username
WORKDIR /home/$username
ENTRYPOINT "/usr/bin/spotify"
