#!/bin/sh

set -e

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf

# Run ssl.sh script to obtain || renew SSL certificates
/ssl.sh

nginx -g 'daemon off;'