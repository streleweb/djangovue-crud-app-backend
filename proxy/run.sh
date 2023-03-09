#!/bin/sh

set -e

if [ ! -f '/etc/letsencrypt/live/todoapi.peterstrele.com/fullchain.pem' ]; then
    certbot certonly \
        --nginx \
        --non-interactive \
        --agree-tos \
        --email streleweb@gmail.com \
        --domains todoapi.peterstrele.com \
        --config-dir /var/lib/letsencrypt \
        --work-dir /var/lib/letsencrypt \
        --logs-dir /var/log/letsencrypt
else
    certbot renew \
        --config-dir /var/lib/letsencrypt \
        --work-dir /var/lib/letsencrypt \
        --logs-dir /var/log/letsencrypt
fi

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf

rm /tmp/nginx.pid
nginx restart

nginx -g 'daemon off;'