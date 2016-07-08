### Redis 

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
