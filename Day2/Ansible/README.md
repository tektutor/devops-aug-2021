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
	- helps in automating configpinguration management using Declarative Languages

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
The expected output is
<pre>
[jegan@tektutor ~]$ ssh -p 2001 root@localhost
The authenticity of host '[localhost]:2001 ([::1]:2001)' can't be established.
ECDSA key fingerprint is SHA256:rb0tLy8dB12o5T0aiKjE+pL8Ixc6Zfrkp9UBuHDz2Bk.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[localhost]:2001' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.18.0-240.el8.x86_64 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@ubuntu1:~# exit
</pre>

<pre>
jegan@tektutor ~]$ ssh -p 2002 root@localhost
The authenticity of host '[localhost]:2002 ([::1]:2002)' can't be established.
ECDSA key fingerprint is SHA256:rb0tLy8dB12o5T0aiKjE+pL8Ixc6Zfrkp9UBuHDz2Bk.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[localhost]:2002' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.18.0-240.el8.x86_64 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

root@ubuntu2:~#    
</pre>

### Running ansible adhoc ping command
```
cd devops-aug-2021
git stash
git pull
cd devops-aug-2021/Day2/Ansible
ansible -i inventory all -m ping
```
You need to replace 'jegan' with 'devops' in the inventory file 

### What happens internally when you run ansible ping
```
ansible -i inventory ubuntu1 -m ping > out.yml 2>&1
```
1. Ansible picks the connection details of ubuntu1 ansible node and makes a SSH connection to ubuntu1 ansible node.
2. Ansible creates a tmp folder in ACM(Ansible Controller Machine) and another tmp folder in ubuntu1 ansible node.
3. Ansible copies the ping.py from ACM tmp folder to ubuntu1 tmp folder.
4. Ansible then gives execute permission to ping.py in the ubuntu1 ansible node.
5. Executes the ping.py using python interpreter on the ubuntu1 ansible node.
6. Collects the output of ping.py execution.
7. Deletes the tmp folder in the ubuntu1 ansible node.
8. Prints a summary of the outcome in the Ansible Controller Machine.
