FROM python:3.11.0-slim-bullseye

WORKDIR /monte-carlo

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "main.py"]