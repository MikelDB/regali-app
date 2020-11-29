FROM python:3.8-slim-buster

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt update

RUN apt install -y python-mysqldb default-libmysqlclient-dev libssl-dev build-essential python3-dev

RUN pip install --upgrade setuptools

RUN pip install -r requirements.txt

RUN pip install pylint --upgrade

RUN pip install pylint_flask_sqlalchemy
RUN pip install pylint-flask

COPY . /app

ENTRYPOINT ["python"]

CMD ["server.py"]
