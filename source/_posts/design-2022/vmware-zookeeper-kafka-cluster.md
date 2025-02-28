---
title: Setup Zookeeper + Kafka in VMware
category: Design
tags: []
comments: true
date: 2024-07-16 01:23
---


今天，我们在 VMware 中，跑起来 4 台 Zookeeper + 3 台 Kafka 机器。

# Conventions

Downloaded packages: /opt/tools

Installed apps: /opt/apps

默认安装的软件：

```linux
yum install tmux wget tree git

rpm -ivh jdk-8u351-linux-x64.rpm
java -version
sudo curl -fsSL https://rpm.nodesource.com/setup_14.x | sudo bash -
yum install -y nodejs
npm --version

systemctl status firewalld.service
systemctl stop firewalld.service
systemctl disable firewalld.service
```

# 静态 IP 地址

首先，IP 地址如下（在访问机器上，可以考虑直接更改 C:\Windows\System32\drivers\etc\hosts）：

```linux
192.168.1.201 zookeeper-01
192.168.1.202 zookeeper-02
192.168.1.203 zookeeper-03
192.168.1.204 zookeeper-04
192.168.1.205 kafka-01
192.168.1.206 kafka-02
192.168.1.207 kafka-03
```

记住，每次 VMware clone 一台新的机器，要做如下两个更改：

```bash
vi /etc/hostname
vi /etc/sysconfig/network-scripts/ifcfg-ens33
```

其中，网络需要用 Bridge 桥链模式（这样相当于虚拟机跟实体机一样，拥有自己的独立 IP 地址，跟 host 机没关系）；不要用 NAT 模式。

另外，ifcfg 配置如下（注意：BOOTPROTO 原值是 dhcp，改掉它）：

	BOOTPROTO="static"
	IPADDR=192.168.1.200
	NETMASK=255.255.255.0
	DNS1=192.168.1.1
	GATEWAY=192.168.1.1

重启，你就拥有了新的 hostname 和 ipv4 地址。

# Zookeeper

```terminal
wget  https://dlcdn.apache.org/zookeeper/zookeeper-3.7.1/apache-zookeeper-3.7.1-bin.tar.gz
tar -zxvf apache-zookeeper-3.7.1-bin.tar.gz
mkdir /opt/apps
mv apache-zookeeper-3.7.1-bin /opt/apps/
cd /opt/apps/
ln -s ./apache-zookeeper-3.7.1-bin/ ./zookeeper
cd /opt/apps/zookeeper/
cp conf/zoo_sample.cfg conf/zoo.cfg
vi conf/zoo.cfg
```

对于 leader/follower 机器，添加以下配置：

```linux
dataDir=/usr/data/zookeeper

server.1=192.168.1.201:2888:3888
server.2=192.168.1.202:2888:3888
server.3=192.168.1.203:2888:3888
server.4=192.168.1.204:2888:3888:observer
```

对于 observer，添加：

```linux
dataDir=/usr/data/zookeeper

peerType=observer
server.1=192.168.1.201:2888:3888
server.2=192.168.1.202:2888:3888
server.3=192.168.1.203:2888:3888
server.4=192.168.1.204:2888:3888:observer
```

【maybe optional】对于每一台机器：

```
mkdir /usr/data/zookeeper
echo 0 > /usr/data/zookeeper/myid
echo 1 > /usr/data/zookeeper/myid # for zookeeper-02
echo 2 > /usr/data/zookeeper/myid # for zookeeper-03
echo 3 > /usr/data/zookeeper/myid # for zookeeper-04
```

好了。可以开始启动了。为了方便起见：

```
vi /root/.bash_profile
PATH=$PATH:$HOME/bin:/opt/apps/zookeeper/bin
```

这样，我们就可以随时随地的跑 zkServer.sh 了。

启动：

```
zkServer.sh status
zkServer.sh start
zkServer.sh status
zkServer.sh stop
zkServer.sh status
```

注意看每台机器的角色。

zookeeper-02:

![](/images/zookeeper-status-leader.png)

zookeeper-03:

![](/images/zookeeper-status-follower.png)

zookeeper-04:

![](/images/zookeeper-status-observer.png)

# Kafka

```
cd /opt/tools/
tar -zxvf kafka_2.12-3.3.1.tgz
mv kafka_2.12-3.3.1 ../apps/
cd ../apps/
ln -s kafka_2.12-3.3.1/ ./kafka
cd /opt/apps/kafka
vi config/server.properties
```

改以下几个地方：

```
broker.id=0 # 分别是 0、1、2、3
listeners=PLAINTEXT://192.168.1.205:9092 # 自己的IP地址
# advertised.listeners 可以不配置，默认 = listeners

zookeeper.connect=192.168.1.201:2181,192.168.1.202:2181,192.168.1.203:2181,192.168.1.204:2181
# zookeeper 配置很重要。这里我用了4台机器的cluster。
```

注意看 log.dirs=/tmp/kafka-logs 这个参数。因为这里的 broker_id 也要改，否则会报错 “Configured broker.id 1 doesn't match stored broker.id Some(0) in meta.properties.”

```
vi /tmp/kafka-logs/meta.properties
broker.id=0
```

好了，可以开始跑了：

```
bin/kafka-server-start.sh config/server.properties
```

如果想在后台跑：

```
bin/kafka-server-start.sh -daemon config/server.properties
ps aux | grep kafka
bin/kafka-server-stop.sh
ps aux | grep kafka
bin/kafka-topics.sh --create --bootstrap-server kafka-01:9092 --topic cities
bin/kafka-topics.sh --list --bootstrap-server kafka-01:9092
```
