### Install JDK 1.8
```
sudo yum install java-1.8.0-openjdk-devel
```
### Install Apache Maven 
```
cd ~/Downloads
wget https://mirrors.estointernet.in/apache/maven/maven-3/3.8.1/binaries/apache-maven-3.8.1-bin.tar.gz
tar xvfz apache-maven-3.8.1-bin.tar.gz
```

### Adding JDK and Maven in environments settings
You need to edit ~/.bashrc and append the below path at the end of the file
```
export M2_HOME=/home/devops/Downloads/apache-maven-3.8.1
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.302.b08-0.el8_4.x86_64
export PATH=$JAVA_HOME/bin:$M2_HOME/bin:$PATH
```
To apply the above environment settings, you need to execute the below command
```
source ~/.bashrc
```
You can now verify if maven is added to environment path correctly
```
mvn --version
```
The expected output is
<pre>
jegan@tektutor ~]$ vim ~/.bashrc
[jegan@tektutor ~]$ source ~/.bashrc
[jegan@tektutor ~]$ mvn --version
Apache Maven 3.8.1 (05c21c65bdfed0f71a2f2ada8b84da59348c4c5d)
Maven home: /home/devops/Downloads/apache-maven-3.8.1
Java version: 1.8.0_302, vendor: Red Hat, Inc., runtime: /usr/lib/jvm/java-1.8.0-openjdk-1.8.0.302.b08-0.el8_4.x86_64/jre
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "4.18.0-240.el8.x86_64", arch: "amd64", family: "unix"
[jegan@tektutor ~]$ 
</pre>

### Verify if JDK 1.8 is installed properly
```
java -version
javac -version
```
Expected output is
<pre>
[jegan@tektutor Downloads]$ javac -version
javac 1.8.0_302
[jegan@tektutor Downloads]$ java -version
openjdk version "1.8.0_302"
</pre>

### Downloading Jenkins
```
cd ~/Downloads
wget https://get.jenkins.io/war-stable/2.289.3/jenkins.war
```

### Launching Jenkins
```
cd ~/Downloads
java -jar ./jenkins.war
```
You won't able to use the terminal once jenkins is launched as it will block the terminal.  Avoid pressing Ctrl + C, in case you need to copy, you may use the track pad or mouse. For all other purpose, you may use a different terminal tab.

### Accessing Jenkins Page from your lab machine Web browser(Chrome)
```
http://localhost:8080
```
You need to copy the initial admin password from the Jenkins terminal, make sure you "are not" using Ctrl + C, as it will terminate Jenkins.

### We need to enable REST API facility in Docker Application Engine so that Ansible can communite with it
```
sudo vim /usr/lib/systemd/system/docker.service
```
And modify the line which currently looks as
```
ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
```
To
```
ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock - H tcp://0.0.0.0:4243
```

We need to restart the docker service to apply the config changes
```
sudo systemctl daemon-reload
sudo systemctl restart docker
sudo systemctl status docker
```
The expected output is
<pre>
[jegan@tektutor Ansible]$ sudo systemctl status docker
● docker.service - Docker Application Container Engine
   Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; vendor preset: disabled)
   Active: active (running) (thawing) since Fri 2021-08-06 14:41:21 IST; 7s ago
     Docs: https://docs.docker.com
 Main PID: 27647 (dockerd)
    Tasks: 18
   Memory: 57.2M
   CGroup: /system.slice/docker.service
           └─27647 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock -H tcp://0.0.0.0:4243

Aug 06 14:41:19 tektutor dockerd[27647]: time="2021-08-06T14:41:19.910054699+05:30" level=info msg="Firewalld: interface>
Aug 06 14:41:19 tektutor dockerd[27647]: time="2021-08-06T14:41:19.978499981+05:30" level=info msg="Firewalld: interface>
Aug 06 14:41:20 tektutor dockerd[27647]: time="2021-08-06T14:41:20.468188365+05:30" level=info msg="Default bridge (dock>
Aug 06 14:41:20 tektutor dockerd[27647]: time="2021-08-06T14:41:20.710088968+05:30" level=info msg="Firewalld: interface>
Aug 06 14:41:20 tektutor dockerd[27647]: time="2021-08-06T14:41:20.966675727+05:30" level=info msg="Loading containers: >
Aug 06 14:41:21 tektutor dockerd[27647]: time="2021-08-06T14:41:21.006764874+05:30" level=info msg="Docker daemon" commi>
Aug 06 14:41:21 tektutor dockerd[27647]: time="2021-08-06T14:41:21.006945032+05:30" level=info msg="Daemon has completed>
Aug 06 14:41:21 tektutor systemd[1]: Started Docker Application Container Engine.
Aug 06 14:41:21 tektutor dockerd[27647]: time="2021-08-06T14:41:21.057823259+05:30" level=info msg="API listen on /var/r>
Aug 06 14:41:21 tektutor dockerd[27647]: time="2021-08-06T14:41:21.065545519+05:30" level=info msg="API listen on [::]:4>
lines 1-20/20 (END)...skipping...
● docker.service - Docker Application Container Engine
   Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; vendor preset: disabled)
   Active: active (running) (thawing) since Fri 2021-08-06 14:41:21 IST; 7s ago
     Docs: https://docs.docker.com
 Main PID: 27647 (dockerd)
    Tasks: 18
   Memory: 57.2M
   CGroup: /system.slice/docker.service
           └─27647 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock -H tcp://0.0.0.0:4243

Aug 06 14:41:19 tektutor dockerd[27647]: time="2021-08-06T14:41:19.910054699+05:30" level=info msg="Firewalld: interface br-cfe86aa580ac al>
Aug 06 14:41:19 tektutor dockerd[27647]: time="2021-08-06T14:41:19.978499981+05:30" level=info msg="Firewalld: interface br-cfe86aa580ac al>
Aug 06 14:41:20 tektutor dockerd[27647]: time="2021-08-06T14:41:20.468188365+05:30" level=info msg="Default bridge (docker0) is assigned wi>
Aug 06 14:41:20 tektutor dockerd[27647]: time="2021-08-06T14:41:20.710088968+05:30" level=info msg="Firewalld: interface docker0 already pa>
Aug 06 14:41:20 tektutor dockerd[27647]: time="2021-08-06T14:41:20.966675727+05:30" level=info msg="Loading containers: done."
Aug 06 14:41:21 tektutor dockerd[27647]: time="2021-08-06T14:41:21.006764874+05:30" level=info msg="Docker daemon" commit=b0f5bc3 graphdriv>
Aug 06 14:41:21 tektutor dockerd[27647]: time="2021-08-06T14:41:21.006945032+05:30" level=info msg="Daemon has completed initialization"
Aug 06 14:41:21 tektutor systemd[1]: Started Docker Application Container Engine.
Aug 06 14:41:21 tektutor dockerd[27647]: time="2021-08-06T14:41:21.057823259+05:30" level=info msg="API listen on /var/run/docker.sock"
Aug 06 14:41:21 tektutor dockerd[27647]: time="2021-08-06T14:41:21.065545519+05:30" level=info msg="API listen on [::]:4243"
</pre>

