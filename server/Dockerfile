FROM python:3.8-alpine
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python -m pip install -r requirements.txt
COPY . /app