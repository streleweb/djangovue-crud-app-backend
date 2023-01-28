FROM python:3.9-alpine3.13

LABEL maintainer="streleweb"

#avoid console python logs delays
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt .
COPY ./init_db.sh /docker-entrypoint-initdb.d/
COPY . .
EXPOSE 8000


RUN python -m venv venv && \
    source venv/bin/activate && \
    pip install --upgrade pip && \
    apk add --update --no-cache mysql-client && \
    pip install -r requirements.txt && \
    rm -rf /requirements.txt && \
    #chmod +x /docker-entrypoint-initdb.d/init_db.sh && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user

ENV PATH="/venv/bin:$PATH"

#switch user, so whoever runs image, does not have root-user privileges
USER django-user
