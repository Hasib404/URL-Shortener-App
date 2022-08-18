FROM python:3.8-alpine
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN python -m pip install -r requirements.txt
COPY . /app
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]