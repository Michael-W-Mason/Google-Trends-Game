FROM python:3.10-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
# RUN apk add libffi-dev
# RUN python3 -m pip install cryptography
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
RUN python3 -m pip install PyMySQL[rsa]
RUN pip install -r requirements.txt
RUN pip install flask-cors

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:application"]