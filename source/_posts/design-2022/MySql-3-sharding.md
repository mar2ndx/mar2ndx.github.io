---
title: MySql (3) - Sharding
category: Design
tags: []
comments: true
date: 2022-10-30 10:50
---


# MySQL-3: sharding

1. MySQL 连接数

	MySQL默认100个连接。（单机最大1500连接）

2. 数据量

	如果单行是100 bytes，当超过50M行的时候，很吃力

3. 索引

	占空间大，命中率低，查询的可能很慢。

## MySQL 性能优化

4种方案：

1. 参数优化
1. 加Cache，加index
1. 读写分离
1. （最终方案）： 分库分表

## What is NewSQL

分布式 + Relational DB，例如 TiDB。

# 分库分表

类型：

1. 垂直分

	eg。不同表放入不同DB种（vertical DB）
	eg。blob文件，单独拿出来放（vertical table）

1. 水平分：一张大表，切割分开

	1.1 范围式分割（例如：时间）
	1.1 hash 分割（例如：ID取模）
	1.1 hybrid 式

## 对比2中 水平分割方法

根据范围分割：

1. 好处：数据部分迁移，extensibility更好
1. 坏处：热点数据分布不均匀，压力不能 balance

根据hash分割：

1. 好处：热点数据分布均匀，可以balance压力
1. 坏处：hash算法一旦改，数据全部需要迁移，extensibility差

解决办法：hybrid 式

1. 先范围，再hash。
1. 一致性hash环（consistent hashing）

## 分布式事务问题

本地的transaction 要做到 ACID。但是distributed transaction做不到 ACID。

CAP定理：

1. consistency
1. availability
1. partition tolerance

三者只能得其二。

BASE定理 = 

	Basically Available(基本可用)
	Soft state(软状态)
	Eventually consistent(最终一致性)

## 分布式主键

1. Redis incr命令
1. UUID 可以，但是：长，且不是排序的，对MySQL不太友好。

终极解决方案：Snowflake algorithm （by Twitter）：

	在分布式系统中，生产全局唯一，且趋势递增的 ID。

> 雪花算法原理就是生成一个的64位比特位的 long 类型的唯一 id。
>
> 1. 最高1位固定值0，因为生成的 id 是正整数，如果是1就是负数了。
> 1. 接下来41位存储毫秒级时间戳，2^41/(1000606024365)=69，大概可以使用69年。
> 1. 再接下10位存储机器码，包括5位 datacenterId 和5位 workerId。最多可以部署2^10=1024台机器。
> 1. 最后12位存储序列号。同一毫秒时间戳时，通过这个递增的序列号来区分。即对于同一台机器而言，同一毫秒时间戳下，可以生成2^12=4096个不重复 id。
>
> 可以将雪花算法作为一个单独的服务进行部署，然后需要全局唯一 id 的系统，请求雪花算法服务获取 id 即可。
>
> 对于每一个雪花算法服务，需要先指定10位的机器码，这个根据自身业务进行设定即可。例如机房号+机器号，机器号+服务号，或者是其他可区别标识的10位比特位的整数值都行。

但是snowflake基于timestamp，所以，如果某台machine clock回拨了，可能会造成ID冲突，或ID乱序。

## 注意

避免跨DB的join。

2种办法：

1. E-R分片：将有ER关系的，存在一个库中（根据ID的奇偶）
1. “全局表”：在每一个分布式DB中，都建立一个表，并且数据是一样的。

# 实战

问：现在有5亿行，有ID, name, city, sex,  请问如何 shard？

答：

1. 用City，不好 ———— 会造成热点数据不均匀问题。
1. 用timestamp，也不好 ———— 也会造成热点数据不均匀。

表的大小？

1. 单行 data < 100 bytes，则 50M rows 一张表。
1. 单行 data > 100 bytes，则 10M rows 一张表。

所以：500M / 50M = 10，向上取整 = 16。hash function 最好用（uid % 16）。
