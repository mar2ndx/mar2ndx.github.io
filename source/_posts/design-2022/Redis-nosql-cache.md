---
title: Redis (NoSQL) Cache
comments: true
category: Design
tags: []
---

# Redis

NoSQL = Not Only SQL

NewSQL = TiDB

## Why MySQL maybe better than NoSQL?

Because support of: 

1. data consistency
1. transaction (ACID)

## NoSQL 4 types

1. Key-value型：Redis，Voldemort，Tokyo Cabinet，Tyrant，BerkeleyDB
	优点：快速查询
	缺点：数据缺少结构化

1. 列存储型：Cassandra，HBase，Riak
	用于：分布式文件系统。同一列的数据存在一起。

1. 文档型：MongoDB，CouchDB
	类似是 a series of key-value pair
	常用语web application，数据结构要求不严格。

1. Graph 型 （不需要知道）：Neo4J，InfoGrid
	常用语social network

# Redis

一个**单线程**的**内存**数据库，用C写的，支持 **100,000 QPS**。

底层用了 IO多路复用 （Non-blocking IO 思想）

支持5种类型：


1. string
1. hash
1. list
1. set
1. sortedset （zset）

目前，Redis 创始人加入了 VMWare 并开源。

## Redis use-cases

1. in-memory database
	记录非登录用户的信息。（没必要存入MySQL）
	例如游客用户浏览记录，浏览记录。。。

1. Cache
	为了提升性能。（注意跟1不同。）
	例如：商品数据，广告等。

1. 数据过期处理
	例如：广告；冷热商品。。。

1. 其他 use cases
	1. 解决 distributed cluster 的session分离问题
	1. 任务队列（性能 + 线程安全），秒杀
	1. 分布式lock（也可以用zookeeper）
	1. 发布订阅消息模式（pub-sub）
	1. app 排行榜
	1. 计数器 （eg 网站访问统计）

## Use Redis in Java

Jedis, Redisson 是官方推荐的 Java client。

Jedis 开源。只需要添加依赖：

```
<dependency>
    <groupId>redis.clients</groupId>
    <artifactId>jedis</artifactId>
    <version>2.8.1</version>
</dependency>
```

Use It:

```
Jedis jedis = new Jedis();

jedis.set("events/city/rome", "32,15,223,828");
String cachedResponse = jedis.get("events/city/rome");
```

## Jedis 连接池

直接：Jedis jedis = new Jedis(); 这样是不 thread-safe 的。不行！

正解是 [create a pool of connections to Redis ](https://www.baeldung.com/jedis-java-redis-client-library)， 可复用，而且调用是线程安全的。

这么写：

```
final JedisPoolConfig poolConfig = buildPoolConfig();
JedisPool jedisPool = new JedisPool(poolConfig, "localhost");

private JedisPoolConfig buildPoolConfig() {
    final JedisPoolConfig poolConfig = new JedisPoolConfig();
    poolConfig.setMaxTotal(128);
    poolConfig.setMaxIdle(128);
    poolConfig.setMinIdle(16);
    poolConfig.setTestOnBorrow(true);
    poolConfig.setTestOnReturn(true);
    poolConfig.setTestWhileIdle(true);
    poolConfig.setMinEvictableIdleTimeMillis(Duration.ofSeconds(60).toMillis());
    poolConfig.setTimeBetweenEvictionRunsMillis(Duration.ofSeconds(30).toMillis());
    poolConfig.setNumTestsPerEvictionRun(3);
    poolConfig.setBlockWhenExhausted(true);
    return poolConfig;
}
```

## 其他几种type

### 2. List

原理：doubly linked list，无下标，有序。

```
jedis.lpush("queue#tasks", "firstTask");
jedis.lpush("queue#tasks", "secondTask");

String task = jedis.rpop("queue#tasks");
```

### 3. hashes

k-v只能整取整存（类似 String）；

但是hash类型，可以存一个Java object。get()的时候，可以只取一个字段。

例如：取得一个用户(user)的地址(postal address)，不需要把整个user信息返回来。

```
jedis.hset("user#1", "name", "Peter");
jedis.hset("user#1", "job", "politician");
		
String name = jedis.hget("user#1", "name");
		
Map<String, String> fields = jedis.hgetAll("user#1");
String job = fields.get("job");
```

### 4. Set

```
jedis.sadd("nicknames", "nickname#1");
jedis.sadd("nicknames", "nickname#2");
jedis.sadd("nicknames", "nickname#1");

Set<String> nicknames = jedis.smembers("nicknames");
boolean exists = jedis.sismember("nicknames", "nickname#1");
```

### 5. zset

zset兼具 list 和 set 的特点。

1. list：有序，可重复
1. set：无序，不可重复
1. zset：有序，不可重复

## get/set/delete/increment

语法：

```
set key value
get key
getset key value (先get value，然后set成新的value）
hdel key field
```

数据增减：Incr

语法：

```
incr key
incrby key increment
decr key
decrby key decrement
```

如何保证原子性？

1. 通过 transaction
1. 通过 Lua 脚本

【重要】：setnx = 当且仅当不存在时，赋值。

eg. 

```
exists job = 0             # job还不存在
setnx job "programmer" = 1 # job赋值成功
setnx job "developer" = 0  # 再次赋值，失败了
get job = "programmer"     # job依然是曾经的那个value
```

用 SetNX 可以实现分布式lock。

> set类型的 spop()可以随机弹出一个值，可以用于公司内部抽奖。

## 通用性命令

1. keys: 查看由哪些key，可以自定义pattern
1. del：删掉一个key
1. exists：判断key是否存在 
1. expires：在多少seconds时候，自动过期。（精确到毫秒）
1. rename
1. type：查看类型，例如string，set，zset，list

建议：Redis用作缓存时，一定要设置expire时间。

（priority越高，时间设置越长，每次都可以重新设置）

# Redis as MQ

Redis 也可以用作 消息模式（类似 Kafka，RabbitMQ）

主要区别于：

1. 如果消息有重复，或者丢失，处理不如其他MQ。
1. 消息middleware中，可靠性，重发，重复消费。

建议用于：

1. rate limit 请求限流

两种模式：队列，或者pub-sub。

## 队列模式

一个生产者，只有一个消费者。

利用 lpush 和 rpop 命令实现。

还有：brpop = blocking right-pop，好处是，如果用rpop会持续失败，相当于每次都建立一个connection，效率太低。

## subscribe 模式

一个生产者，有多个消费者。

原理：参考微信群。

命令：

1. subscribe：加入群 （消费者）
1. publish：群发消息 （生产者）

每次有人（类似群主）发布消息publish，消费者（只要subscribe过）都能收到。

# 内存和过期策略

一定要设置 maxmemory，默认为0（不设置）。如果超过了max memory，Redis 就崩溃了。

## 数据淘汰策略

如果数据过期了，自动就清除了。但问题是：即使清理过期后，memory还是不够用怎么办？

共有6种策略：

1. volatile-lru
	从**已设置过期时间**的数据集（server.db[i].expires）中挑选**least-recently-used**的数据淘汰

2. volatile-ttl
	从**已设置过期时间**的数据集（server.db[i].expires）中挑选**将要过期的**数据淘汰
3. volatile-random
	从已设置过期时间的数据集（server.db[i].expires）中**任意选择**数据淘汰
	
4. allkeys-lru
	从数据集（server.db[i].dict）中挑选最近最少使用的数据淘汰

5. allkeys-random
	从数据集（server.db[i].dict）中任意选择数据淘汰

6. no-enviction（驱逐）
	默认。不驱逐数据。

## 评价

1. volatile-lru 比 volatile-ttl 更好，因为快过期了不代表就没用了。

1. 工业界种，LRU 也比 LFU 更精准

1. 不要用allkey的。

最后：如果所有 ttl的都清理完了，内存还是不够用，会不会清除没过期的数据？

答：不会，Redis直接崩溃。

# Redis 事务

skip，好复杂。

基于Redis multi/exec/watch：

1.multi，开启Redis的事务，置客户端为事务态。

2.exec，提交事务，执行从multi到此命令前的命令队列，置客户端为非事务态。

3.discard，取消事务，置客户端为非事务态。

4.watch,监视键值对，作用时如果事务提交exec时发现监视的监视对发生变化，事务将被取消。

# 悲观锁 Pessimistic Lock

Java synchronized 是悲观锁 (Pessimistic Lock)：

1. 具有互斥性
1. 性能不会太高
1. 会使命令串行化（synchronized）。

高并发的场景下，不能用悲观锁。

## 乐观锁 Optimistic Lock

Redis 事务的最大使用场景：乐观锁 (Optimistic Lock)

基于CAS = compare and swap 的思想。

秒杀经常用 Redis 乐观锁。

# Redis 主从

主从复制，类似MySQL那一节课。

如果处理Master宕机：sentinel机制（哨兵）

1. client 是连到 Sentinel 上的，这里哨兵相当于一个 proxy。
1. 持续 ping 主机，在30s之内没有 response，就重新选举 master
1. Election：auto-failover（自动故障迁移）：
	raft算法（谁先发现，谁是新master）

## 集群

官方推荐 Redis-cluster 集群方案。

1. Redis 3 需要配合Lua脚本。
1. Redis 5 直接实现。
