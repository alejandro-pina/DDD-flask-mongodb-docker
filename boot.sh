#!/bin/sh
source venv/bin/activate

while true; do
    flask deploy
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done
# Gunicorn documentation recommends (2 x $num_cores) + 1 as the number of workers to start with.
exec gunicorn --name AlexAPP --timeout 300 --graceful-timeout 10 -w 3 -b :5000 --access-logfile - --error-logfile - application:app