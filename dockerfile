FROM python:3.8-slim-buster
WORKDIR /bot
COPY requirements.txt requirements.txt
COPY .env .env
RUN pip3 install -r requirements.txt
COPY main.py main.py
CMD ["python3" "main.py"]