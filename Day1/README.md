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

