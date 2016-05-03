FROM python:3.5

RUN mkdir -p /usr/src/app

COPY grattis.py /usr/src/app/

WORKDIR /usr/src/app
RUN pip install facebook-sdk
