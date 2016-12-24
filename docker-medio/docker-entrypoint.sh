#!/bin/bash

nc -vz $1 $2

while [ $? -eq 1 ]; do
    echo Database not ready for connections
    echo Sleeping 3 seconds then trying again...
    sleep 3
    nc -vz $1 $2
done

echo Database is ready bub

cd /var/medio
python configure.py $1 $2
/usr/bin/supervisord -n -c supervisord.conf
