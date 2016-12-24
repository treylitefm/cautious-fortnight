### Medio Flask app

Note: If installed through docker container, none of these setup steps are necessary.

Install dependencies
```
$ pip install -r requirements.txt
```

Run configuration script
```
$ python configure.py [hostname] [port #]
```

Run application
```
$ python server.py 
```

Navigate to `localhost:5000` in browser and voila!

Edit 'directory' path variables in supervisord.conf file
```
[program:medio]
command=/usr/bin/python server.py
process_name=%(program_name)s

numprocs=1

directory=/path/to/app
stopsignal=TERM

autostart=true
autorestart=true

[program:rqworker]
command=/usr/local/bin/rq worker -c redis_settings
process_name=%(program_name)s

numprocs=1

directory=/path/to/app
stopsignal=TERM

autostart=true
autorestart=true
```

Run supervisor to load up webapp and rq workers (Pass the -n parameter to run supervisor daemon in foreground)
```
$ supervisord -c supervisord.conf
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
