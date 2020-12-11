FROM python:3.8-slim

WORKDIR /home

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3-dev build-essential && \
    apt-get install -y libpcre3 libpcre3-dev && \
    apt-get install -y uwsgi && \
    apt-get install -y supervisor && \
    apt-get install -y curl && \
    apt-get clean

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir gateway

COPY gateway/ ./gateway/
COPY refresh.sh ./refresh.sh
COPY app.ini ./app.ini
COPY supervisord.conf /usr/local/etc/supervisord.conf
COPY api.conf /etc/supervisor/conf.d/api.conf

EXPOSE 8080

CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/api.conf