server {
    listen ${LISTEN_PORT} ssl http2;
    listen [::]:443 ssl http2;

    ssl_certificate /var/lib/letsencrypt/live/ec2-18-216-246-117.us-east-2.compute.amazonaws.com/fullchain.pem;
    ssl_certificate_key /var/lib/letsencrypt/live/ec2-18-216-246-117.us-east-2.compute.amazonaws.com/privkey.pem;


    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass           ${APP_HOST}:${APP_PORT};
        include              /etc/nginx/uwsgi_params;
        client_max_body_size 10M;
    }

}