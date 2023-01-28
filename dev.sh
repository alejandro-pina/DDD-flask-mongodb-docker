#!/bin/sh
source venv/bin/activate

while true; do
    flask dev
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Development command failed, retrying in 5 secs...
    sleep 5
done
flask run