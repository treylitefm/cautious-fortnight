#!/bin/bash
python configure.py $1 $2
/usr/bin/supervisord -n -c /var/medio/medio/flask/supervisord.conf
