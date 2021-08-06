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

