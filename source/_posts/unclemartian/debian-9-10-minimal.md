---
title: 【Tech】 Debian 9/10 minimal
category: unknown
tags: ubuntu
comments: true
date: 2022-04-01 00:00:00
---


# Overview

One advantage of using Debian is: lightweight. 

Some commands are different from ubuntu, thus archiving here. 

## Disk Free

Debian 9:

    deb@debian9:~$ df -h
    Filesystem      Size  Used Avail Use% Mounted on
    udev            1.5G     0  1.5G   0% /dev
    tmpfs           302M  4.3M  297M   2% /run
    /dev/sda1       6.0G  1.8G  3.9G  32% /
    tmpfs           1.5G     0  1.5G   0% /dev/shm
    tmpfs           5.0M     0  5.0M   0% /run/lock
    tmpfs           1.5G     0  1.5G   0% /sys/fs/cgroup
    tmpfs           302M     0  302M   0% /run/user/1000

Debian 10: 

    deb@debian10:~$ df -h
    Filesystem      Size  Used Avail Use% Mounted on
    udev            984M     0  984M   0% /dev
    tmpfs           200M  3.0M  197M   2% /run
    /dev/sda1       6.9G  1.8G  4.8G  27% /
    tmpfs           998M     0  998M   0% /dev/shm
    tmpfs           5.0M     0  5.0M   0% /run/lock
    tmpfs           998M     0  998M   0% /sys/fs/cgroup
    tmpfs           200M     0  200M   0% /run/user/1000

## Hostname

To check

    hostname
    hostnamectl

To change it: 

    hostnamectl set-hostname new-hostname
    vi /etc/hosts

Run hostnamectl command again.

## SSH

    sudo apt install ssh
    sudo systemctl status ssh
    sudo systemctl start ssh

If you are connecting using VirtualBox, change network settings to Bridge (instead of NAT).

Then: 

    sudo apt install net-tools
    ip addr
    hostname -I

Edit: /etc/ssh/sshd_config on your VM:

    PasswordAuthentication yes

Now, restart SSH server. Done.

## Install make and gcc

Otherwise, you won't be able to build a lot of packages, including npm. 

    apt-get install gcc automake autoconf libtool make

# Install bt

