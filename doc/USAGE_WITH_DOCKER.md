Using OSRFramework with Docker
==============================

This file will explain how to use the Docker images for OSRFramework. This will let the reader use the tools easily in almost any platform. To do so, the user will have to install Docker on its computer, what should be enough in most systems.

1.- Verifying Your Docker Installation
--------------------------------------

Docker is available for Mac, Windows and Linux and can be installed easily in Azure or AWS. We strongly recommend to follow the official guides to install and run Docker in your system. Some good starting points can be found [here](https://docs.docker.com/engine/installation/).

2.- Downloading the Latest OSRFramework Version
-----------------------------------------------

To run the latest OSRFramework isntallation from Docker you can use the following command:
```
> docker run -it i3visio/osrframework:latest
```

It will download our latest official image. Then, you will be able to login into the Docker image to interact as usual without needing to redownload it again. E. g.:
``` 
> docker run -it osrframework:latest
root@c79505f6b915:/# usufy.py -n i3visio -p twitter facebook github
...
root@c79505f6b915:/# osrfconsole.py
```

If you want to map the port opened by `osrframework_server.py` you will need to specify it when launching Docker to map the ports and make them accesible. In the following example, we are mapping the 30230 port of the container to port 8080 outside it.

```
> docker run -it -p 8080:30230 i3visio/osrframework:latest
```

Once launched `osrframework_server.py` we will be able to interact with the instance outside it using `curl`.

```
> curl http://localhost:8080/info
```

3.- Building Your Own Image Locally
-----------------------------------

As we also provide the Dockerfile, advanced users may opt to build the image themselves. This can be done by _cd-ing_ into the folder of a clones project and using:

```
> docker build -t osrframework ./
```

You will be able ro run the built image as usual:

```
> docker run -it osrframework
```

If by any circunstamce you prefer to rebuild the instance from scratch, you can always tell it to Docker:

```
> docker build --no-cache=true -t osrframework ./
```

### Example of a New Build

As an example, generally we build and push the Docker images as follows:
```
> docker login
> docker build -t osrframework:0.16.6 ./
> docker tag osrframework:0.16.6 i3visio/osrframework:latest
> docker push i3visio/osrframework:latest
> docker run -it i3visio/osrframework:latest
```

We can always opt to launch a beta vesion:

```
> docker login
> docker build -t osrframework:0.16.6 --build-arg VERSION=--pre ./
> docker tag osrframework:beta i3visio/osrframework:beta
> docker push i3visio/osrframework:beta
> docker run -it i3visio/osrframework:beta
```

