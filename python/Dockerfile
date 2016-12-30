FROM python:2.7

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt

CMD ["python", "-u", "runner.py"]
