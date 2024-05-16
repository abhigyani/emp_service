FROM tiangolo/uvicorn-gunicorn:python3.9

LABEL maintainer="Abhigyani Anand <abhigyani.anand1@gmail.com>"

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app