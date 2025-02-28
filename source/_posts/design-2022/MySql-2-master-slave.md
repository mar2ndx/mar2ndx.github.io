---
title: MySql (2) - Master/slave
category: Design
tags: []
comments: true
date: 2022-10-30 10:13
---


# MySQL-2: master / slave

# NewSQL

MySQL 关系型

NoSQL（Redis，MongoDB）

NewSQL = 分布式 Relational DB，例如 淘宝的 TiDB

## 分布式 MySQL 最重要的3个概念

1. 主从复制
1. 读写分离
1. 分库分表

# 主从复制

## 主从复制 的原理

1. master开启binary log
1. master事务提交，记录入bin log
1. slave的I/O thread，读取master中的binary log
1. slave写入relay log（中继人）
1. slave的SQL thread读取relay log，并写入slave

![](/images/mysql-master-slave-structure.png)

## 主从复制 的步骤

1. 关闭防火墙

    systemctl stop iptables
    systemctl stop firewalld (默认)
    systemctl disable firewalld.service

1. Master 开启 binary log
1. 选择哪个DB用于主从复制

    binlog-do-db=白名单
    binlog-ignore-db=黑名单

1. 重启 mysql
1. 授权 Replication Slave（复制权限）或者 All Privileges 给slave机器。
1. 刷新权限：Flush privilege

# 读写分离

读写分离 depends on 主从复制.

## Why seperate R/W？

默认情况下，master对外，slave只是个备份。

所以：读写分离

1. master：partial read + write
1. slave：read

## 实现

原理：read通常发给slave，除非发现 **主从延时**。

用Linux 下面的 mysql-proxy实现的（linux下需要先安装）。

配置文件用Lua写的：

    proxy-backend-addresses = master_address
    proxy-read-only-backend-addresses = slave_address
    proxy-lua-script = .../mysql-proxy/rw-splitting.lua

Lua语言写的小脚本，可以内嵌在应用程序里。

### Lua 配置

举个例子：

    min_idle_connections = 3,
    max_idle_connections = 4,

所有SQL走 proxy，Lua脚本规定了分流规则。
