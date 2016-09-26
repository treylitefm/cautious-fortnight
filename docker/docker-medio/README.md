### Medio Docker Image

Is [docker](https://docs.docker.com/) installed yet?

Change directories to /path/to/root/of/project/docker, so that Dockerfile is in your current dir
```bash
$ cd /path/to/root/of/project/docker
```

Build container with following command replacing [image-name] with whatever you'd like to call the image:

```bash
$ docker build -t [image-name] .
```

Sweet! So as long as things didn't error out, you can check out the newly created image with this command:

```bash
$ docker images
```

Now, building your container should be as simple as:
```bash
$ docker run -it --name [medio-container-name] --link [redis-container-name]:db --restart=always -v [host-path]/[container-path] -p 5000:5000 [image-name]
```

*Note: The internal port in which the container's flask app runs may change at some point, but as of writing this, the app listens on port 5000 within the container*
