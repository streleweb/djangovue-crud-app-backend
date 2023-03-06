FROM python:3.9-alpine3.13

LABEL maintainer="streleweb"

#avoid console python logs delays
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . .
COPY ./scripts /scripts
EXPOSE 8000


RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r requirements.txt && \
    rm -rf requirements.txt && \
    apk del .tmp-build-deps && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts


ENV PATH="/scripts:/py/bin:$PATH"

#switch user, so whoever runs image, does not have root-user privileges
USER django-user

# script that will run the app in deployment( works with uwsgi)
CMD [ "run.sh" ]


