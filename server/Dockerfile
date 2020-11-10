FROM python:3.8-slim-buster


WORKDIR /app



RUN useradd -s /bin/bash -d /app samsja \
    && chown -R samsja: /app



COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src .


USER samsja


EXPOSE 8888


CMD  gunicorn -t 300 -b :8888 -w 1 run:app
