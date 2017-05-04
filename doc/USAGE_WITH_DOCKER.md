Using OSRFramework with Docker
==============================

This file will explain how to use the Docker images for OSRFramework. This will let the reader use the tools easily in almost any platform. To do so, the user will have to install Docker on its computer, what should be enough in most systems.

1.- Verifying Your Docker Installation
--------------------------------------

TODO.

2.- Downloading the Latest OSRFramework Version
-----------------------------------------------

To run the latest OSRFramework isntallation from Docker you can use the following command:
```
docker run -it i3visio/osrframework:latest
```

It will download our latest official image. Then, you will be able to login into the Docker image to interact as  usual. E. g.:
``` 
> docker run -it osrframework:latest
root@c79505f6b915:/# usufy.py -n i3visio -p twitter facebook github
...
root@c79505f6b915:/# osrfconsole.py
```


3.- Tips and Tricks
-------------------

TODO.
