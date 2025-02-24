---
title: MySql (1) - Indexing, Locking and Transaction
comments: true
category: Design
tags: []
---

# MySQL Knowledge Graph

1. Performance
1. MySQL cluster
1. Sharding
1. Indexing
1. MySQL architecture
1. Lock
1. MySQL事务 （ACID）

## Architecture

![](/images/mysql-High-Level-Architecture.png)

1. 最上层：connector

1. 中间：SQL Layer

	包含：connection pool （包括，Auth，thread，check memory，cache），以及 Management Services & Utilities

	1. SQL interface 接受sql语句
	1. Parser 词法分析，判断能否执行 （语法树）
	1. Optimizer 优化器，你写的不够完美，通过：执行查询计划（explain）
		eg 多表关联：小结果集，驱动大结果集
	1. Cache and Buffer （MySql 8.0之后弃用）

1. 下层：storage layer
	1. 就是跟文件打交道的。
	1. 多种引擎，可选：MyISAM（快），InnoDB（默认，功能更全），Memory（极快，易丢失）等等

### 对比 MyISAM 和 InnoDB

skip

现在基本都是 InnoDB。并发 + 支持事务 + 隔离性。

如果基本就是读写，数据量巨大，无并发，可以选MyIsam。

# Physical 结构

MySQL 的文件，分2中：

1. 索引文件
1. 日志文件

其实都是存在 /var/lib/mysql/ 中。

## 日志文件

1. errorlog

	默认开启，默认记录为 mysqld.log

1. binlog（binary log）

	记录所有ddl和dml语句（数据的变化），但是不记录select语句。

	是一种压缩日志，以“事件”的形式保存。

	有好多个文件，因为每次 restart MySQL，生成一个新的 binlog。

1. general query log

	增删改查，全都存。一般不开启。

1. slow query log

	如果差的很慢，存一下。用于调优。

	long_query_time = 3, 意思是超过3s的，就记录到慢查询日志中。

1. 重做日志
1. 回滚日志
1. 中继日志（用作：主从复制）

### 查询log的开启状况：

查看所有log On/Off: 

	show varibles like ‘log_%’;

查看数据位置：

	show varibles like ‘%datadir%’;

# Indexing

索引的作用：

1. 搜索
1. 排序
1. 索引下推 ICP
1. 覆盖索引 （select字段作为索引）

查看 索引：show index from tuser；

索引的种类：

1. 主键索引
1. 唯一索引 （Unique Index）
1. 组合索引
1. 单列索引（Index），或普通索引

## 原理

MyISAM / InnoDB ： B+ tree 索引。

Memery：Hash 索引

### B+ tree

B Tree 高度一般在 2～4 层。（其中，3 层就可以支持 20G，4层可以支持到 20TB）

平衡多路查找树（B-Tree）

![](/images/sql-b-tree.png)

B tree和B+ tree区别：

1. 非leaf节点 是否存储数据。（B tree 存，B+ tree 不存）
1. leaf 节点是一个 linked list

![](/images/sql-b-plus-tree.png)

# MySQL locking

1. 乐观锁

	1. 程序实现：版本号 + 时间戳。
	1. 通常是Redis实现的。这里先不讲。
	
1. 悲观锁

	我用了，你就不能用。（MySQL系统默认都是悲观锁）
	
	1. 表级锁（expensive，少用）
	
		只有当 **行锁升级为表锁**时，才会用到**表锁**。
		
	1. 行级锁（InnoDB）
		
		1. 共享读锁 - 手动加
		1. 排他写锁 - 自动加

eg. session 1 write 时候，拿到 写锁，session2 连读都读不了。

# Transaction 事务

四大特性ACID：

1. Atomicity
1. Consistency：执行前后，是稳定一致的。
1. Isolation：多个tx之间，互不影响
1. Durabilitity：一定全部写入磁盘。

