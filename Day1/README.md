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

The expected output is
<pre>
[jegan@tektutor DevOps]$ docker exec -it mysql1 sh
# mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.26 MySQL Community Server - GPL

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
</pre>

### Creating database, tables and inserting records
```
CREATE DATABASE tektutor;
USE tektutor;
CREATE TABLE Training (id int, name VARCHAR(25), duration VARCHAR(25));
INSERT INTO Training VALUES ( 1, "DevOps", "5 Days" );
INSERT INTO Training VALUES ( 2, "Kubernetes", "5 Days" );
INSERT INTO Training VALUES ( 3, "Artificial Intelligence", "5 Days" );
SELECT * FROM Training;
```

The expected output is
<pre>
mysql> CREATE DATABASE tektutor;
Query OK, 1 row affected (0.00 sec)

mysql> USE tektutor;
Database changed
mysql> CREATE TABLE Training (id int, name VARCHAR(25), duration VARCHAR(25));
Query OK, 0 rows affected (0.03 sec)

mysql> INSERT INTO Training VALUES(1, "DevOps", "5 Days");
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO Training VALUES(2, "Kubernetes", "5 Days");
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO Training VALUES(3, "Artificial Intelligence", "5 Days");
Query OK, 1 row affected (0.00 sec)
CREATE DATABASE tektutor;
USE tektutor;
CREATE TABLE Training (id int, name VARCHAR(25), duration VARCHAR(25));
INSERT INTO Training VALUES ( 1, "DevOps", "5 Days" );
INSERT INTO Training VALUES ( 2, "Kubernetes", "5 Days" );
INSERT INTO Training VALUES ( 3, "Artificial Intelligence", "5 Days" );
SELECT * FROM Training;
mysql> SELECT * FROM Training;
+------+-------------------------+----------+
| id   | name                    | duration |
+------+-------------------------+----------+
|    1 | DevOps                  | 5 Days   |
|    2 | Kubernetes              | 5 Days   |
|    3 | Artificial Intelligence | 5 Days   |
+------+-------------------------+----------+
3 rows in set (0.00 sec)

mysql> 
</pre>

### Stopping and restarting mysql1 container will not lead to loss of data
```
mysql> exit
exit
docker stop mysql1
docker start mysql1
docker exec -it mysql1 sh
mysql -u root -p
mysql> SHOW DATABASES;
mysql> USE tektutor;CREATE DATABASE tektutor;
USE tektutor;
CREATE TABLE Training (id int, name VARCHAR(25), duration VARCHAR(25));
INSERT INTO Training VALUES ( 1, "DevOps", "5 Days" );
INSERT INTO Training VALUES ( 2, "Kubernetes", "5 Days" );
INSERT INTO Training VALUES ( 3, "Artificial Intelligence", "5 Days" );
SELECT * FROM Training;
mysql> SHOW TABLES;
mysql> SELECT * FROM Training;
mysql> exit
exit
```
As you can observe, you will not loose records stored in container storge by restarting container.

### Deleting container also deletes any data stored in container storage
```
docker rm -f mysql1
```

### Storing mysql1 database and its records into an external volume
```
mkdir -p /tmp/mysql
docker run -d --name mysql1 --hostname mysql1 -v /tmp/mysql:/var/lib/mysql mysql:latest
docker exec -it mysql1 sh
mysql -u root -p
CREATE DATABASE tektutor;
USE tektutor;
CREATE TABLE Training (id int, name VARCHAR(25), duration VARCHAR(25));
INSERT INTO Training VALUES ( 1, "DevOps", "5 Days" );
INSERT INTO Training VALUES ( 2, "Kubernetes", "5 Days" );
INSERT INTO Training VALUES ( 3, "Artificial Intelligence", "5 Days" );
SELECT * FROM Training;
exit
exit
docker rm -f mysql1
docker run -d --name mysql1 --hostname mysql1 -v /tmp/mysql:/var/lib/mysql mysql:latest
docker exec -it mysql1 sh
mysql -u root -p
USE tektutor;
SELECT * FROM Training;
```
As you can observe, though mysql1 container was deleted we are able to access the records created in old container from the new mysql1 container.  This is possible as we are using Volume Mounting /tmp/mysql.

### Setting up Load Balancer with nginx
Let's create 3 nginx containers as shown below to be used as web servers
```
docker run -d --name nginx1 --hostname nginx1 nginx:1.20
docker run -d --name nginx2 --hostname nginx2 nginx:1.20
docker run -d --name nginx3 --hostname nginx3 nginx:1.20
```

Let's create a loadbalancer container using nginx image
```
docker run -d --name lb --hostname lb nginx:1.20
```

We need to configure lb container to work like a Load Balancer otherwise by default nginx works as a typical webserver. Let's copy the existing config file from lb to local machine as shown below.
```
docker cp lb:/etc/nginx/nginx.conf .
```

We need to modify the copied nginx.conf file as below
```
user  nginx;
worker_processes  auto;

error_log  /var/log/nginx/error.log notice;
pid        /var/run/nginx.pid;


events {
    worker_connections  1024;
}

http {
    upstream backend {
        server 172.17.0.2;
        server 172.17.0.3;
        server 172.17.0.4;
        server 172.17.0.6;
        server 172.17.0.7;
    }
    
    server {
        location / {
            proxy_pass http://backend;
        }
    }
}
```

We need to copy the nginx.conf file into the lb container and restart the apply the changes
```
docker cp nginx.conf lb:/etc/nginx/nginx.conf
docker restart lb
```

See if the lb container is running after the config changes
```
docker ps
```

Let's modify index.html with custom message on nginx1, nginx2 and nginx3 to differentiate the output coming from each server.
```
echo "Server 1" > index.hmtl
docker cp index.html nginx1:/usr/share/nginx/html/index.html
echo "Server 2" > index.hmtl
docker cp index.html nginx2:/usr/share/nginx/html/index.html
echo "Server 3" > index.hmtl
docker cp index.html nginx3:/usr/share/nginx/html/index.html
```

### Time to test your load balancer
```
curl http://localhost
curl http://localhost
curl http://localhost
```
Each time you curl, you are expected to see web pages served by nginx1, nginx2 and nginx3 in a round-robin fashion.
