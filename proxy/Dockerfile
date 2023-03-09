FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="streleweb"

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

ENV LISTEN_PORT=443
ENV APP_HOST=app
ENV APP_PORT=9000

USER root

RUN mkdir -p /var/log/letsencrypt && \
    chown nginx:nginx /var/log/letsencrypt && \
    chmod 700 /var/log/letsencrypt && \
    mkdir -p /var/lib/letsencrypt && \
    chown nginx:nginx /var/lib/letsencrypt && \
    chmod 700 /var/lib/letsencrypt && \
    chown nginx:nginx /tmp/nginx.pid && \
    chmod 700 /tmp/nginx.pid && \
    apk add --no-cache augeas-libs certbot certbot-nginx python3 py3-pip && \
    python3 -m ensurepip && \
    mkdir -p /vol/static && \
    pip3 install --upgrade pip && \
    pip3 install virtualenv && \
    virtualenv /opt/certbot && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /vol/static

# unprivileged nginx user for security
USER nginx

# obtains || renews SSL certificates and runs nginx in foreground
CMD ["/run.sh"]