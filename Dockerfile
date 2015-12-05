FROM microservice_python
MAINTAINER Cerebro <cerebro@ganymede.eu>

RUN pip install -U web.py
RUN pip install pymysql

ENV CONFIG_DIR ./config

ADD . /opt/players-backend
ADD ./supervisor/players-backend.conf /etc/supervisor/conf.d/players-backend.conf

EXPOSE 80
