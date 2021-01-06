FROM python:3.8.3-buster

RUN apt-get update && apt-get install -y libjpeg-progs zlib1g-dev
COPY requirements.txt .
RUN pip install -r requirements.txt
