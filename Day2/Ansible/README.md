Vagrant
   - Virtual Management Management tool
   - helps you in provisioning a new container, new virtual machine, new cloud machine in Azure/AWS/GCP, etc
   - it interacts with VirtulBox, Docker, Podman, AWS, Azure, GCP, etc
   - Vagrantfile
	- this is Iaac(Infrastructure services as a Code)
   - some sample commands
	 vagrant init
	 vagrant up

Progamming Languages are of two major types
	1. Imperative
	What ?
	- you need to write code to automate
	How ?
	- you need to write logic as code to perform the configuration management
	2. Declarative
	What ?
		- You need to mention in the Ansible declarative style
	How ?
		- is taken care by Ansible

YAML
 - Yet Another Markup Language
 - Super set of JSON(JavaScript Object Notation)

### Configuration Management Tools
	- Puppet - DSL(Domain Specific Language) - Ruby
	- Chef - DSL used is Ruby
	- Ansible - is developed in Python but uses YAML as DSL
	- Salt (SaltStack)

Puppet/Chef
  - Pull based client/server architecture
  - DSL used is Ruby
  - Software setup is complex
  - Learning curve is steep
  - People coming from different background(Operations, QA & Dev) 

Ansible 
  - though it is developed in Python
  - Automation requires only knowlede in YAML
  - Software setup is very simple
  - Learning Ansible also doesn't take must time
  - comes in 2 flavours
	- Ansible Core (Opensource and command-line based)
	- RedHat Ansible Tower ( Enterprise Grade - requires license and it is Web GUI )
		- underhood it uses Ansible Core open source configuration mangement tool
  
### Ansible
- Configuration Mangement Tool
	- Developed by Ansible Inc organization
		- Founded by Michael Deehan
		- Michael Deehan is a former RedHat employee
	- Agentless less
        - Follows PUSH based architecture
	- Ansible Core is Open source
    	- Install softwares
	- Configure softwares
	- Manage users/permission/network policies
	- typically most of the admin related day-today-work
	- helps in automating configuration management using Declarative Languages

### Installing Ansible
```
su -
yum install -y epel-release
yum install -y ansible
```

### Check if ansible is installed correctly
```
ansible --version
```

### Install git
```
su -
yum install -y git
```

### Cloning source code (Do this as Devops user)
```
git clone https://github.com/tektutor/devops-aug-2021.git
cd devops-aug-2021/Day2/Ansible
```

### Creating ssh key pairs (Do this as Devops user)
```
ssh-keygen
```
Accept all defaults by hitting Enter key 3 times.

### Copy the public key and put it in Day2/Ansible/ubuntu-ansible (Do this as Devops user)
```
cd devops-aug-2021/Day2/Ansible/ubuntu-ansible
cp ~/.ssh/id_rsa.pub authorized_keys
```

### Build the custom ubuntu ansible image (Do this as Devops user)
```
docker build -t tektutor/ansible-ubuntu .
```

### Troubleshooting permission denied issue
```
su -
usermod -aG docker devops
exit
sudo su devops
docker build -t tektutor/ansible-ubuntu .
```

### Check if you can see the newly build image
```
docker images
```

### Remove any existing containers
```
docker rm -f $(docker ps -aq)
```

### Create couple of ubuntu containers using our custom ubuntu image
```
docker run -d --name ubuntu1 --hostname ubuntu1 -p 2001:22 -p 8001:80 tektutor/ansible-ubuntu:latest 
docker run -d --name ubuntu2 --hostname ubuntu2 -p 2002:22 -p 8002:80 tektutor/ansible-ubuntu:latest 
```

### See if the ubuntu1 and ubuntu2 containers are running
```
docker ps
```

### Test if you can do ssh into ubuntu1 and ubuntu2 containers without typing password
```
ssh -p 2001 root@localhost
ssh -p 2002 root@localhost
```
When it prompts a question, type yes
```
Are you sure, you want to continue connecting (yes/no): 
```
