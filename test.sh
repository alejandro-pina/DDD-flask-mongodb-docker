#!/bin/sh
source venv/bin/activate

while true; do
    flask itests
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo TESTING command failed, retrying in 30 secs...
    sleep 30
done

flask itests | sed -n '/###START_TEST###/,/###ERROR_TEST###/p'
# U can create output txt or csv 
if [[ "$?" == "0" ]]; then
    break
fi
