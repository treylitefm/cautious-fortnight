### Redis 

Is [docker](https://docs.docker.com/) installed yet?

Change directories to /path/to/root/of/project/docker, so that Dockerfile is in your current dir
```bash
$ cd /path/to/root/of/project/docker
```

Pull official redis image

```bash
$ docker pull redis
```

Run docker image
```
$ docker run --name [name-your-container] -d redis redis-server --appendonly yes
```

References:

 - https://docs.docker.com/engine/examples/running_redis_service/
 - https://hub.docker.com/_/redis/
 - http://redis.io/
