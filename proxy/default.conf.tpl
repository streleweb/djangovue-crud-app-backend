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
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Upgrade $http_upgrade;
    }
}