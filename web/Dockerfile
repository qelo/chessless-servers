FROM nginx:alpine

RUN apk update
RUN apk add wget zip
RUN wget http://chessboardjs.com/releases/0.3.0/chessboardjs-0.3.0.zip

ADD nginx.conf /etc/nginx/conf.d
ADD index.html /etc/nginx/html/
RUN unzip -d /etc/nginx/html/ chessboardjs-0.3.0.zip 