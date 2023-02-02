FROM python:3.9-alpine3.13

LABEL maintainer="streleweb"

#avoid console python logs delays
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . .
EXPOSE 8000


RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r requirements.txt && \
    rm -rf requirements.txt && \
    apk del .tmp-build-deps && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user

ENV PATH="/py/bin:$PATH"

#switch user, so whoever runs image, does not have root-user privileges
# USER django-user
