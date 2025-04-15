---
title: 【Tech】 CentOS 7 Commands
category: unknown
tags: ubuntu
comments: true
date: 2021-07-01 00:00:00
---


一边学一边写的，不太完整。

# Jenkins

Installation: [centos7安装nginx并配置前端环境 - simplesally - 博客园](https://www.cnblogs.com/simple1025/p/11394312.html)

Change to root: [jenkins 构建出现 permission-denied问题_feifei10244499的博客-CSDN博客](https://blog.csdn.net/feifei10244499/article/details/105714574/)

Install maven: [linux 安装 maven 、解决：bash: mvn: command not found](https://cloud.tencent.com/developer/article/1556981)

# Nginx

Start and stop nginx locally:

```
cd /usr/local/webserver/nginx/sbin

# Run Nginx
./nginx -v
./nginx

# Stop Nginx
./nginx -s stop
```

Config nginx when system starts:

(config nginx to systemctl first, then systemctl enable)

Ref: [centos7下安装、配置Nginx、设置Nginx开机自启动 - 阿木工作室 - 博客园](https://www.cnblogs.com/iverson-3/p/12301009.html)

# Linux

Kill process

    # check port
    netstat -apn | grep 9999

    # check process iD
    ps -ef | grep httpd

    # kill process
    kill -HUP PID
    kill -9 PID

## Get my IP address

    ip addr show

## Extract tar.gz

    # 解开一个tar 
    tar -xvf etcbak.tar

    # 解压一个tar.gz
    tar -zxvf etcbak.tar.gz

Meaning of __zxvf__:
 
1. z	通过gzip支持的压缩或解压缩。还有其他的压缩或解压缩方式，比如j表示bzip2的方式
1. x	解压缩
1. v	在压缩或解压缩过程中显示正在处理的文件名
1. f	f后面必须跟上要处理的文件名。

## Trojan 

[Trojan For Linux 教程 - 西部世界VPN](https://xbsj6147.xyz/pagesv2/download-linux.html)

```
cd /usr/src/trojan
./trojan -l ./trojan.log -c ./config.json
ss -tlnp | grep 1080
curl --socks5 127.0.0.1:1080 https://www.google.com -k 

# test IP addrees 
curl http://icanhazip.com
# should return singapore IP address 149.129.53.1
```

把 proxychains 放入 shell 中：

```
Nginx
proxychains4 -q /bin/bash 
```
