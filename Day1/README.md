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
