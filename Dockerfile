# pull official base image
FROM python:3.9.4-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT=8000

## install psycopg2 dependencies
#RUN apk update \
#    && apk add postgresql-dev gcc python3-dev musl-dev
#
## install dependencies
#RUN pip install --upgrade pip
#COPY ./requirements.txt .
#RUN pip install -r requirements.txt
#
## copy project
#COPY . .
#
#CMD python manage.py runserver 0.0.0.0:$PORT:m

RUN apt-get update
RUN apt-get -y install python-pip
RUN apt-get update
RUN pip install --upgrade pip
RUN pip install psycopg2-binary

COPY base.py base.py

CMD ["python", "base.py"]