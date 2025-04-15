---
title: 【Tech】 Install Resilio Sync on Linxu / ChromeOS
category: unknown
tags: ubuntu
comments: true
date: 2022-03-25 00:00:00
---


# Background

In this post, I will cover installing Resilio on:

1. Ubuntu
1. GalliumOS (based off Ubuntu 18)
1. Chromebook Crostini (Debian 11)
1. Chromebook Android (version 9)

# Get started

## Install 

Download Deb and install from [the official website](https://www.resilio.com/platforms/desktop/) or [this post](https://help.resilio.com/hc/en-us/articles/206178924)

    sudo dpkg -i <resilio-sync.deb>

Alternatively, install using apt-get:


    echo "deb http://linux-packages.resilio.com/resilio-sync/deb resilio-sync non-free" | sudo tee /etc/apt/sources.list.d/resilio-sync.list
    curl -L https://linux-packages.resilio.com/resilio-sync/key.asc | sudo apt-key add
    (maybe optional) wget -qO - https://linux-packages.resilio.com/resilio-sync/key.asc | sudo apt-key add -

    sudo apt-get update    
    sudo apt-get install -y resilio-sync

## Enable it

Enable the service:

    sudo systemctl status resilio-sync
    sudo systemctl enable resilio-sync
    sudo systemctl start resilio-sync

Check it out:___https://127.0.0.1:8888/gui/__

So far, you can access the UI but still not able to use it. 

For Ubuntu, go ahead and config permission.

## Config Permission

According to [this post](https://help.resilio.com/hc/en-us/articles/206178924-Installing-Sync-package-on-Linux): 

> user_group is a group name of current user, by default it's the same as user name (can be checked by running id command)

In my case I ran (My whoami = 'cb'):

    sudo usermod -aG cb rslsync
    sudo usermod -aG rslsync cb
    sudo chmod g+rw /home/rslsync/Resilio\ Sync/

This should be enough for Ubuntu. However, for the Linux on ChromeOS, you need to do the following. 

# Additional Steps on ChromeOS Linux

First, check your username in ‘Crostini’ Linux.

```
whoami
```

> Let's ensure that ‘normal’ user can read/write the synchronized files by 'rslsync' user. 

> Run the following (mind the last command which [adding user permissions to the /home/rslsync folder](https://kenfavors.com/code/how-to-add-user-permissions-to-a-folder-in-ubuntu/))

    sudo usermod -aG [whoami] rslsync    
    sudo usermod -aG rslsync [whoami]
    sudo chmod g+rw /home/rslsync/
    sudo apt install acl
    sudo setfacl -R -m "u:[whoami]:rwx" /home/rslsync

Now test link: __https://127.0.0.1:8888/gui/__

You might need to change owner for certain folders: 

    sudo chown -R [whoami]:[whoami] ./folder-name/

# Forgot username

If ever, you forgot your username. On Linux, go to [Sync Storage Folder](https://help.resilio.com/hc/en-us/articles/206664690-Sync-Storage-folder) by running the following: 

    cd /var/lib/resilio-sync

Find a file with the name "settings.dat". The [cleartext username should be there](https://forum.resilio.com/topic/43918-forgot-usernamepasswd-for-web-ui/).

Just search for the text "username2". If you have no luck trying the method above, you can refer to [this official doc to reset WebUI password](https://help.resilio.com/hc/en-us/articles/205450295-How-do-I-reset-my-WebUI-password-).

# Reference 

https://www.davidfong.org/post/resiliosyncchromebook/
