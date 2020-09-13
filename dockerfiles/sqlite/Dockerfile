FROM alpine:3.7
RUN apk add --no-cache sqlite
ARG dbname="data.db"
VOLUME /db
ENTRYPOINT /usr/bin/sqlite3 /db/data.db
