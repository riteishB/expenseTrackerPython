FROM python:3.7

ADD . /app

WORKDIR /app

RUN pip install pipenv

RUN pipenv lock -r > requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app/src

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000"]
