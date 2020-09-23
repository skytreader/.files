# sqlite

The only use for this library is as a CLI prompt. Like so,

    docker run -it --entrypoint sqlite3 -v $(pwd)/data.db:/db/data.db skytreader/sqlite:latest
