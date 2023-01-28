# syntax=docker/dockerfile:1

FROM python:3.7-alpine

RUN apk add --no-cache findutils

LABEL MAINTAINER="Alex Piña <alexpddd@alejandropina.com>"

ENV FLASK_APP application.py
ENV FLASK_CONFIG production

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /applications/alexddd_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN addgroup -g $GROUP_ID applications \
  && adduser -D -u $USER_ID -G applications alexddd_app -s /bin/sh

COPY requirements.txt ./
RUN  python -m venv venv
RUN  venv/bin/pip install -r requirements.txt

COPY app app
COPY application.py boot.sh config.py ./

RUN chmod +x boot.sh

USER alexddd_app

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]
