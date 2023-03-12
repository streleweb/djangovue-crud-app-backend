#!/bin/sh

set -e

if [ ! -f '/etc/letsencrypt/live/ec2-18-216-246-117.us-east-2.compute.amazonaws.com/fullchain.pem' ]; then
    certbot certonly \
        --nginx \
        --non-interactive \
        --agree-tos \
        --email streleweb@gmail.com \
        --domains ec2-18-216-246-117.us-east-2.compute.amazonaws.com \
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

nginx -g 'daemon off;'