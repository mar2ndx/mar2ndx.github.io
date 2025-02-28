---
title: MySql (4) - Performance Optimization
category: Design
tags: []
comments: true
date: 2022-10-30 10:06
---


# MySQL-4: optimize

# 性能分析

Steps：

1. 开启 slow query log
1. 查看执行计划：explain 有问题的SQL语句
1. show profile 查看问题SQL的使用情况

## Slow Query

除了用慢查询日志，还可以用：

1. MySQL自带的 mysqldumpslow 工具
1. 一款Linux软件：percona-toolkit (DBA喜欢用)

![](/images/mysql-dumpslow-slow-query.png)

## Profile

```
set profiling = 1
```

例如：

![](/images/mysql-profiling-for-query.png)

可以看出：sending data 耗费了大量的时间。

# 服务器层的优化

1. 扩大 Buffer pool：理论上可以到内存的70% ~ 80%

	如何知道 buffer时候满了？看 innodb_buffer_pool_pages_free == 0 则说明满了。
	
	在 my.cnf 中，可以改 innodb_buffer_pool_size = 750M
	
1. innodb_log_file_size 设置成 buffer log 的 25%

1. select from... 可以不放入 binlog

1. 提高磁盘效率：SSD

# SQL 语句的优化

（重要！）

## SQL 设计层面

1. 设计一些**中间表**，针对统计分析功能
	1. 或：实时性要求不高的话：OLTP，OLAP
1. 创建一些冗余字段，例如 name 字段
	1. 这样可以避免很多关联查询
	1. 注意：别出现数据的Consistancy问题
1. 把 ID —— Name 的关联关系，放入缓存，这样计算的更快
1. 表太大的话：拆表
	1. vertical split：太多字段了，拆成2个表 （例如，ID —— 产品介绍）
	1. horizontal split：sharding
1. 建议每个表有一个primary key（主键索引），最好是int类型，而且是自增的。

## SQL 语句层面

1. 索引优化
	where字段，组合索引，索引下推，索引覆盖。。。
	‘on’ 关联字段的两边：排序 分组统计
	不要用 *

1. Limit优化
	limit 可以停止全表扫描

## 最终方案

如果已经做了：SQL 参数优化，cache，indexing，还是性能不好。

可以考虑最终极方案：

1. 读写分离
1. 分库分表
