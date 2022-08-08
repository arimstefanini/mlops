FROM python:3.8-slim

WORKDIR /santander_chalenge

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install curl
RUN apt-get install libgomp1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 
RUN rm requirements.txt

COPY /data /santander_chalenge/data 
COPY /src  /santander_chalenge/src
