FROM python:2.7-slim

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENV NAME Damao

CMD ["python", "counter.py"]