FROM python:3.10-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo
RUN python3 -m pip install PyMySQL[rsa]
RUN pip install -r requirements.txt
RUN pip install flask-cors

COPY . ./app


CMD ["python", "app/server.py"]
