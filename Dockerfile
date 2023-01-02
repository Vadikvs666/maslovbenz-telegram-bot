FROM python:3.8-slim-buster
ENV API_TOKEN ${API_TOKEN}
WORKDIR /bot
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY .env .env
COPY main.py main.py
RUN chmod +x main.py
CMD python3 main.py