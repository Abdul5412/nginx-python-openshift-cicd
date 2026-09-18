FROM nginxinc/nginx-unprivileged:alpine

USER root

RUN chmod -R 777 /var/cache/nginx /var/run

COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 8080
