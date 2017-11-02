FROM python:3.5

# Force stdio/out/err to be unbuffered - we want to see errors pronto.
ENV PYTHONUNBUFFERED 1

ADD requirements.txt /requirements.txt
ADD requirements_base.txt /requirements_base.txt
ADD requirements_server.txt /requirements_server.txt
ADD requirements_heroku.txt /requirements_heroku.txt

RUN pip install -r requirements.txt

RUN mkdir /code
WORKDIR /code
ADD . /code