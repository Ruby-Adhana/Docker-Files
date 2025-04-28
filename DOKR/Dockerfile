FROM ubuntu:latest
LABEL maintainer="RubyGujjar"
LABEL created_on="10-04-2025"
RUN apt update -y && \
    apt install -y apache2 && \
    apt clean

WORKDIR /var/www/html
COPY HtmlProject/*.jpg ./
COPY HtmlProject/index.html ./index.html
ENV Name=RubyAdhana
CMD ["/usr/sbin/apache2ctl","-D","FOREGROUND"]

