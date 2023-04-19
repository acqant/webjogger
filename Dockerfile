from python:3

COPY requirements.txt requirements-dev.txt /tmp/
ENV PYTHON /usr/local/bin/python
RUN $PYTHON -m pip install -r /tmp/requirements-dev.txt


WORKDIR /workspace
