### Building custom centos ansible image
```
cp ~/.ssh/id_rsa.pub ~/devops-aug-2021/Day2/Ansible/centos-ansible/authorized_keys
cd ~/devops-aug-2021/Day2/Ansible/centos-ansible
sudo su devops
docker build -t tektutor/ansible-centos .
```

### Check if the newly built centos image is listed
```
docker images
```

### Create centos1 and centos2 containers as shown below
```
docker run -d --name centos1 --hostname centos1 -p 2003:22 -p 8003:80 tektutor/ansible-centos:latest 
docker run -d --name centos2 --hostname centos2 -p 2004:22 -p 8004:80 tektutor/ansible-centos:latest 
```

### Test if you are able to SSH into the centos1 and centos2 containers without password
```
ssh -p 2003 root@localhost
exit
ssh -p 2004 root@localhost
exit
```

### Check if ansible ping works 
```
cd ~/devops-aug-2021
git pull
cd Day3
ansible all -m ping
ansible ubuntu -m ping
ansible centos -m ping
```

### Running the playbook
```
cd ~/devops-aug-2021
git pull
cd Day3
ansible-playbook install-nginx-playbook.yml
```

### Test if you are able to access web page from the ubunt1,ubuntu2, centos1 and centos2 containers respectively
```
curl http://localhost:8001
curl http://localhost:8002
curl http://localhost:8003
curl http://localhost:8004
```

### Running the final refactored playbook
```
cd ~/devops-aug-2021
git pull
cd Day3/refactored-v3
ansible-playbook install-nginx-playbook.yml
```

### Test if you are able to access web page from the ubunt1,ubuntu2, centos1 and centos2 containers respectively
```
curl http://localhost:8001
curl http://localhost:8002
curl http://localhost:8003
curl http://localhost:8004
```

### Running the playbook that demonstrates handlers and notifiers
```
cd ~/devops-aug-2021
git pull
cd Day3/HandlersAndNotifiers
ansible-playbook install-nginx-playbook.yml
```

### Ansible Galaxy
```
ansible-galaxy init apache
```
The above command will create the directory structure recommended by Ansible role.  However, for our trainig purpose, you could ignore this command as Day3/CustomAnsibleRole already has the apache role.

### Remove the existing otherwise nginx and apache port conflicts will happen
```
docker rm -f $(docker ps -aq)
```

### Create new containers
```
docker run -d --name ubuntu1 --hostname ubuntu1 -p 2001:22 -p 8001:80 tektutor/ansible-ubuntu:latest 
docker run -d --name ubuntu2 --hostname ubuntu2 -p 2002:22 -p 8002:80 tektutor/ansible-ubuntu:latest 

docker run -d --name centos1 --hostname centos1 -p 2003:22 -p 8003:80 tektutor/ansible-centos:latest 
docker run -d --name centos2 --hostname centos2 -p 2004:22 -p 8004:80 tektutor/ansible-centos:latest 
```

### Running the playbook that demonstrates using custom ansible role
```
cd ~/devops-aug-2021
git pull
cd Day3/CustomAnsibleRole
ansible-playbook install-apache-playbook.yml
```

### Check if you can access the custom web pages
```
curl http://localhost:8001
curl http://localhost:8002
curl http://localhost:8003
curl http://localhost:8004
```
