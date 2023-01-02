FROM python:3.8-slim-buster
ENV PYTHONFAULTHANDLER=1

ENV PYTHONUNBUFFERED=1

ENV PYTHONHASHSEED=random

ENV PYTHONDONTWRITEBYTECODE 1

ENV PIP_NO_CACHE_DIR=off

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

ENV PIP_DEFAULT_TIMEOUT=100
ENV API_TOKEN ${API_TOKEN}
RUN mkdir -p /codebase /storage

ADD . /codebase

WORKDIR /codebase



RUN pip3 install -r requirements.txt

RUN chmod +x /codebase/main.py



CMD python3 /codebase/main.py;
