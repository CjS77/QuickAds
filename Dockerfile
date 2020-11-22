FROM python:3

RUN apt update -yy && apt -yy install gunicorn

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME ["data", "static", "media"]

EXPOSE 8000
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

CMD [ "/bin/bash", "./scripts/start.sh" ]
