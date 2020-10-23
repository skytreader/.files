FROM alpine:3.7
RUN apk add --no-cache sqlite
RUN mkdir /db
VOLUME /db/data.db
ENTRYPOINT /usr/bin/sqlite3 /db/data.db
