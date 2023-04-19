from python:3

RUN apt-get update && apt-get -y install vim lsof

COPY requirements.txt requirements-dev.txt /tmp/

ENV PYTHON /usr/local/bin/python
RUN $PYTHON -m pip install -r /tmp/requirements-dev.txt


WORKDIR /workspace
