#!/bin/sh

set -e

if [ ! -f '/etc/letsencrypt/live/todoapi.peterstrele.com/fullchain.pem' ]; then
    certbot certonly --nginx --non-interactive --agree-tos --email streleweb@gmail.com --domains todoapi.peterstrele.com
else
    certbot renew
fi
    crond -f -d 8 &

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf

nginx -g 'daemon off;'