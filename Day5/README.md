### Install JDK 1.8
```
sudo yum install java-1.8.0-openjdk-devel
```

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
