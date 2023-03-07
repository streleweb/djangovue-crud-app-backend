server {
    listen ${LISTEN_PORT};

    ssl_certificate /vol/certs/nginx-selfsigned.crt;
    ssl_certificate_key /vol/certs/nginx-selfsigned.key;

    location /static {
        alias /vol/static;
    }

    location / {
        uwsgi_pass           ${APP_HOST}:${APP_PORT};
        include              /etc/nginx/uwsgi_params;
        client_max_body_size 10M;
    }
}