FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="streleweb"

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

ENV LISTEN_PORT=443
ENV APP_HOST=app
ENV APP_PORT=9000

USER root

RUN apk add --no-cache augeas-libs certbot certbot-nginx python3 py3-pip && \
    python3 -m ensurepip && \
    mkdir -p /vol/static && \
    pip3 install --upgrade pip && \
    pip3 install virtualenv && \
    virtualenv /opt/certbot && \
    ln -s /opt/certbot/bin/certbot /usr/bin/certbot && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

# Create a script to obtain and renew SSL certificates
RUN echo "#!/bin/sh\n\
    set -e\n\
    if [ ! -f '/etc/letsencrypt/live/todoapi.peterstrele.com/fullchain.pem' ]; then\n\
    certbot certonly --nginx --non-interactive --agree-tos --email streleweb@gmail.com --domains todoapi.peterstrele.com\n\
    else\n\
    certbot renew\n\
    fi\n\
    crond -f -d 8 &\n\
    " > /ssl.sh && chmod +x /ssl.sh

VOLUME /vol/static

# unprivileged nginx user for security
USER nginx

CMD ["/run.sh"]