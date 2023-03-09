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

crond -f -d 8 &

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf

# restart nginx
nginx -s reload

nginx -g 'daemon off;'