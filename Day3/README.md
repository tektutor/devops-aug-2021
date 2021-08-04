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
