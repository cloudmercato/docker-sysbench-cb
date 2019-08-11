FROM cloudspectator/sysbench
MAINTAINER Anthony Monthe <amonthe@cloudspectator.com>

ENV CB_CLIENT_VERSION master
RUN apt install -y python3-pip
RUN pip3 install https://github.com/cloudspectatordevelopment/cb-client/archive/${CB_CLIENT_VERSION}.zip

ADD entrypoint.py /bin/entrypoint

CMD entrypoint
