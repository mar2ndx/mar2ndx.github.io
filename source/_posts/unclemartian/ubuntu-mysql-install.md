---
title: 【Tech】 Install MySQL 5.7 on Ubuntu 20.04
category: unknown
tags: ubuntu
comments: true
date: 2021-09-02 00:00:00
---


# Installation

    apt-get update
    apt-get install wget
    mkdir /downloads
    cd /downloads
    wget wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
    sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb
    # if the prompt is closed by accident, run:
    sudo dpkg-reconfigure mysql-apt-config

Here, select MySQL 5.7, you will be prompt that Ubuntu 20.04 does not support MySQL 5.7. 

Don't worry, select Ubuntu bionic. Then OK. 

    sudo apt-get update
    apt-cache policy mysql-server

We can see

    5.7.35-1ubuntu18.04 500 
       500 http://repo.mysql.com/apt/ubuntu bionic/mysql-5.7 amd64 Packages

Now simulate the installation first, then actually install:

> Use the -s flag to simulate an action. 
> 
> For example: "apt-get -s install <package_name>" will simulate installing the package, showing you what packages will be installed and configured.

    sudo apt install -s -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*
    sudo apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*

then:

    sudo apt-get install -s mysql-client=5.7.34-1ubuntu18.04
    sudo apt-get install mysql-client=5.7.34-1ubuntu18.04
    sudo apt-get install -s mysql-community-server=5.7.34-1ubuntu18.04
    sudo apt-get install mysql-community-server=5.7.34-1ubuntu18.04

Or simply:

    sudo apt-get install -s mysql-server=5.7.35-1ubuntu18.04
    sudo apt-get install mysql-server=5.7.35-1ubuntu18.04
    mysql -V
    mysql -u root -p

As a next-step, you need to check status of your wirefall and open up Port 3306:

    sudo ufw status
    sudo ufw allow 80
    sudo ufw allow 3306

## Prevent MySql upgrade

Modify this file: 

    vi /etc/apt/preferences.d/mysql

File content: 

    Package: mysql-server
    Pin: version 5.7.35-1ubuntu18.04
    Pin-Priority: 1001

    Package: mysql-client
    Pin: version 5.7.35-1ubuntu18.04
    Pin-Priority: 1001

    Package: mysql-community-server
    Pin: version 5.7.35-1ubuntu18.04
    Pin-Priority: 1001

    Package: mysql-community-client
    Pin: version 5.7.35-1ubuntu18.04
    Pin-Priority: 1001

    Package: mysql-apt-config
    Pin: version 0.8.12-1
    Pin-Priority: 1001

Try to update mysql-server and you will get notified: 

    mysql-server is already the newest version (5.7.35-1ubuntu18.04). 
    0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.

# Run MySQL

    mysql -u root -p
    select version();
    CREATE USER 'michael'@'%' IDENTIFIED BY 'bob';
    CREATE USER 'alex'@'%' IDENTIFIED BY 'alice';
    select host,user,password_last_changed from mysql.user;

## Config privileges

Now flash privileges for non-root users:

    mysql -u root -p
    use mysql;
    select host, user from user; 
    update user set host = '%' where user = 'root';
    select host, user from user;
    flush privileges;

Allow remote access of MySQL:

因为默认3306端口只允许本地访问的，注释掉这行

    sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf

    # By default we only accept connections from localhost
    # bind-address  = 127.0.0.1

Restart MySQL: 

    service mysql restart
    systemctl restart mysql

# Install an MySQL client

If you are on ubuntu 18: 

    sudo apt-get install emma

If you are on ubuntu 20, use DBeaver. 


# To uninstall

    service mysql status
    service mysql stop
    sudo apt-get purge mysql-server mysql-client mysql-common mysql-server-core-* mysql-client-core-*
    sudo rm -rf /etc/mysql /var/lib/mysql
    sudo apt autoremove

# Ref

https://techexpert.tips/mysql/installing-mysql-5-7-ubuntu-20-04/
https://www.cnblogs.com/wang666/p/10218950.html
https://www.cnblogs.com/chenlove/p/9552438.html
