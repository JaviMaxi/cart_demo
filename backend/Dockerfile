FROM python:3.8.10
RUN apt update && apt -y install python3-pip
COPY ./requirements.txt /
RUN pip install -r /requirements.txt
COPY ./ /app
WORKDIR /app

CMD ["gunicorn", "webshop.wsgi", "-b", "unix:/run/backend/backend.sock"]
