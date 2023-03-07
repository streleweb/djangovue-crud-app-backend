server {
    listen ${LISTEN_PORT};

    ssl_certificate /vol/certs/fullchain.pem;
    ssl_certificate_key /vol/certs/privkey.pem;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass           ${APP_HOST}:${APP_PORT};
        include              /etc/nginx/uwsgi_params;
        client_max_body_size 10M;
    }
}