from node:10 AS builder

WORKDIR /app

COPY . /app

WORKDIR /app/frontend

RUN npm ci

RUN npm run build-pkg


FROM python:3.7

COPY --from=builder /app/Backend /app

WORKDIR /app

RUN pip install pipenv

RUN pipenv lock -r > requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app/src

CMD gunicorn app:app --bind 0.0.0.0:$PORT

