# FROM bitnami/minideb:stretch
FROM launcher.gcr.io/google/debian9:latest

RUN apt-get update
RUN apt-get -y install zip wget
RUN wget https://stockfish.s3.amazonaws.com/stockfish-9-linux.zip
RUN unzip stockfish-9-linux.zip
RUN apt-get -y install python3

ADD chess_over_http.py .

CMD ["/usr/bin/python3", "chess_over_http.py", "stockfish-9-linux/Linux/stockfish-9-64"]