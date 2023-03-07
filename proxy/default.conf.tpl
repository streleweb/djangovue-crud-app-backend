server {
    listen ${LISTEN_PORT};

    ssl_certificate /etc/letsencrypt/live/todoapi.peterstrele.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/todoapi.peterstrele.com/fullchain.pem;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass           ${APP_HOST}:${APP_PORT};
        include              /etc/nginx/uwsgi_params;
        client_max_body_size 10M;
    }
}