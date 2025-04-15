---
title: 【Tech】 Install Jdk / Java on Linux
category: unknown
tags: ubuntu
comments: true
date: 2021-09-05 00:00:00
---


# Install JDK 8

    sudo apt-get install openjdk-8-jdk
    ls /usr/lib/jvm/java-8-openjdk-amd64/

    # Put in ~/.bashrc
    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
    export PATH=$PATH:$JAVA_HOME/bin

    # To verify Java:
    java -version

To switch java version that you want to use: 

    sudo update-alternatives --config java
