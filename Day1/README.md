### How multiple operating systems were installed before the Virtualization existed?
Using bootloader utility like LILO or GRUB

### What is Virtualization(Hypervisor)?
Virtualization is Hardware + Software solution
- Heavy Weight Virtualization
    - Because each VM requires dedicated
        - CPU
        - RAM
        - Storage
        
AMD Processor
    Virtualization Feature is referred as AMD-V

Intel Processor
    Virtualization Feature is referred as VT-X

VMWare came up Virtualization product around year 2000.

### Factors that decide the number of Virtual machines a single server can host
1. Processor - number of CPU cores (Quad-core)
2. RAM
3. Storage (Hard disk)

Each Physical CPU Core is equivalent to 2 Virtual Cores

Quad Core Processors can support upto 8 Virtual Machines

### Hypervisor
- general term used to refer to the Virtualization technology
- Vendors specific Virtualization Products
- VMWare
    - VMWare Fusion (Mac-OSX)
    - VMWare Workstation (Windows & Linux)
    - VMWare Player (Windows)
    - VMWare vSphere (Bare-metal Hypervisor)


### Containers
- Application process running in its own Network Namespace
- Network Namespace provides a separate copy of Network stack to each containers
- recommendation is one application per container
- containers get its own IP Address (typically private IP Address)
- every containers gets it own port namespaces (0-65535)
Docker Application Container Engine
### Alternates to Docker Container Runtimes
1. Podman used by RedHat Openshift
2. rkt (pronounced as Rocket)
3. LXC (Light Weight Containership)

Even Kubernetes starting from 2021 Dec 1.22 release they are moving away from Docker to Podman.

### Installing Docker
```
su -
yum install -y yum-utils
yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
yum install -y docker-ce --allowerasing
```
When you are prompted for password type 'rps@12345'

### Start the docker applicaiton engine service
```
su -
systemctl enable docker
systemctl start docker
docker --version
docker images
```

### Listing images in the local Docker registry
```
docker images
```

### Downloading docker image from Docker Hub
```
docker pull hello-world:latest
```

### Finding Image layers
```
docker image inspect ubuntu:16.04
```

### Deleting an image
```
docker rmi ubuntu:16.04
```
You need to delete the containers that were created using above image first prior to deleting the containers.

### Creating a hello container 
```
docker run hello-world:latest
```

### Listing all the currently running containers
```
docker ps
```

### Listing all containers irrespective of their running states
```
docker ps -a
```
### Creating a container in interactive/foreground mode
```
docker run -it --name ubuntu1 --hostname ubuntu1 ubuntu:16.04 /bin/bash
```

### Creating container in background/daemon mode
```
docker run -dit --name ubuntu2 --hostname ubuntu2 ubuntu:16.04 /bin/bash
```


### Listing the containers running
```
docker ps
```

### Listing docker networks
```
docker network ls
```

### Creating customer docker networks
```
docker network create my-network-1
docker network create my-network-2 --subnet 192.168.0.0/16
```
Containers that are in same networks can ping each other, while containers in different networks can't ping each other by default.

### Listing docker networks
```
docker network ls
```

### Inspecting network details
```
docker network inspect my-network-2
```

### Creating a new container and adding it to our custom network
```
docker run -dit --name ubuntu3 --hostname ubuntu3 --network my-network-1 ubuntu:16.04 bash 
docker run -dit --name ubuntu4 --hostname ubuntu4 --network my-network-2 ubuntu:16.04 bash 
```
In the above commands, ubuntu:16.04 is the image name
--name is the container name
--hostname is the hostname of the container

### Getting inside a container that is running in background
```
docker exec -it ubuntu3 bash
```

### Coming out of a container shell 
```
docker exec -it ubuntu4 bash
exit
```

### Finding the IP Address of a container
```
docker inspect ubuntu3 | grep IPA
docker inspect ubuntu4 | grep IPA
```

### Stopping a running container
```
docker stop ubuntu3
```

### Start an exited container
```
docker start ubuntu3
```

### Restart an existing container
```
docker restart ubuntu3
```

### Delete a container that is stopped already
```
docker rm ubuntu3
```

### Delete a running container graciously
```
docker stop ubuntu3
docker rm ubuntu3
docker stop ubuntu4 && docker rm ubuntu3
```

### Forcibly delete a running container
```
docker rm -f ubuntu3
```

### Creating a mysql container
```
docker run -d --name mysql1 --hostname mysql1 -e MYSQL_ROOT_PASSWORD=root mysql:latest
```

### Getting inside mysql1 container and connecting to mysql server
```
docker exec -it mysql1 sh
mysql -u root -p
```
When prompted for password, type 'root' as the password.  This is the password you supplied while creating the container.
