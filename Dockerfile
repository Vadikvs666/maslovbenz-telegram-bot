FROM python:3.8-slim-buster
ENV API_TOKEN ${API_TOKEN}
RUN mkdir -p /bot /storage
WORKDIR /bot
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY .env /bot/.env
COPY main.py /bot/main.py
RUN chmod +x /bot/main.py
CMD python3 /bot/main.py