### Redis 

Is [docker](https://docs.docker.com/) installed yet?

Change directories to /path/to/root/of/project/docker, so that Dockerfile is in your current dir
```bash
$ cd /path/to/root/of/project/docker
```

Build redis server image

```bash
$ docker build -t <username>/redis .
```

Run docker image
```
$ docker run --name redis -d <username>/redis
```

References:

 - https://docs.docker.com/engine/examples/running_redis_service/
 - https://hub.docker.com/_/redis/
 - http://redis.io/
