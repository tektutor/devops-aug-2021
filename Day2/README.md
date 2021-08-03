### Orchestration Platforms
- can deploy your applications to ensure they are Highly Available(HA)
- also offers monitoring capabilities
- automatically detects faults applications and replaces them with another good instance
- on demand, you could scale up/down the number of instances of your application
- rolling updates
	- should be able upgrade your appln from one version to the other
 	- should be able to rollback to older version in case of any instability observed in your latest upgrade
- you can external/internal/cloud services for your applications

Orchestration Platform
	- Docker SWARM - only supports Docker Container Runtime
	- Google Kubernetes
		- Supports Docker Runtime by default as of 1.21 Kubernetes version
		- Likely to move to Podman Container Runtime starting from 1.22 K8s onwards
		- Also supports LXC, RKt, Podman Container Runtimes
		- This orchestration platform is time tested as Google used it several years internally
	- RedHat Openshift (IBM)
		- orchestration platform built on top of Opensource Google Kubernetes
		- by default used Podman as Container Runtime
		- supports Private Containter Registry out of the box
		- supports CI/CD out of the box
		- supports Private GitHub like version control with OpenShift out of the box
		- supports Jenkins, etc
		- supports Sonatype Nexus, JFrog Artifactory, etc
		- also you get support from RedHat(IBM) depending on the SLA signed between
		  your organization and RedHat(IBM)

	- Rancher
		- GUI for Google Kubernetes
		- offers some of the features provided by RedHat OpenShift
		- opensource
		


