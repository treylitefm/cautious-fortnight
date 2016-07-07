### Medio Flask app

Install dependencies
```
$ pip install -r requirements.txt
```

Run configuration script
```
$ python configure.py
```

Run application
```
$ python server.py 
```

Navigate to `localhost:5000` in browser and voila!


Create supervisor config
```
$ echo_supervisord_conf > /etc/supervisord.conf
```

Add rq workers program to /etc/supervisord.conf ([RQ Documentation](http://python-rq.org/docs/jobs/))
```
[program:rqworker]
command=/usr/local/bin/rq worker -c redis_settings
process_name=%(program_name)s

numprocs=1

directory=/
stopsignal=TERM

autostart=true
autorestart=true
```

Run rq workers in supervisor (Pass the -n parameter to run supervisor daemon in foreground)
```
$ supervisord -c /etc/supervisord.conf
```

Monitor task queue
```
$ rq info -c [redis_settings_file]
```

Logfile for supervisord.conf (Path can be edited in supervisord.conf)
```
$ tail -F /tmp/supervisord.conf
```

Run app in debug mode
```
$ export FLASK_DEBUG=1; python server.py
```
