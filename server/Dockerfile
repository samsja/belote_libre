#FROM python:3.8-slim-buster
FROM arm64v8/python:3.8-slim-buster
#FROM balenalib/raspberry-pi-debian-python:latest


WORKDIR /app



RUN useradd -s /bin/bash -d /app samsja \
    && chown -R samsja: /app



COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src src


USER samsja


EXPOSE 8888


ENV NB_WORKERS=1

# CMD  gunicorn -t 300 -b :8888 -w $NB_WORKERS src.run:app

CMD  python src/run.py
