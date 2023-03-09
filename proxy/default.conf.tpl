server {
    listen ${LISTEN_PORT} ssl;

    ssl_certificate /etc/letsencrypt/live/todoapi.peterstrele.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/todoapi.peterstrele.com/privkey.pem;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass           ${APP_HOST}:${APP_PORT};
        include              /etc/nginx/uwsgi_params;
        client_max_body_size 10M;
    }

    location /.well-known/acme-challenge {
        proxy_pass http://certbot:80;

    }
}