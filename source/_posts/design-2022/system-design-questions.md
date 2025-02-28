---
title: System design questions
category: Design
tags: []
comments: true
date: 2022-11-15 21:58
---


# TikTok

Java AOP 的用法
Rest vs RPC 区别
手写 singleton Java
double checked locking singleton java
distributed lock 分布式锁
LRU cache 如何变成线程安全，然后展开如果是分布系统，如何做 replica，并且保证数据一致性

系统设计，就是抖音的 profile 页面

Circular queue's follow up 多个线程要访问这个 queue 怎么办。我说用锁。他说效率不好。我提出分成 2 种锁，enqueue/dequeue 各一种。他说有没有听过乐观锁。答曰没有。

设计一个服务，用户可以拿到 Amazon 上商品的历史价格
这个挺有意思的，因为里边隐藏了一个 web crawler。相当于一个简易版的 web crawler + 典型分布式服务设计。记得多问问题，举个例子，现实中有这么个网站亚麻是很容易知道的，你还要去爬网页就有 legal 风险（虽然是公开数据，但也是亚麻的数据，亚麻和商户之间肯定也是有相关协议的）。面试官就会告诉你其实亚麻是允许你爬的，但是设置了限制，1 个 IP 一秒只能访问一次。这样的话你的设计里就只能牺牲 data freshness，同时可以给货品的 popularity 分类，不然那么多商品肯定爬不完的。
另外还有一些有意思的讨论，比如这个网站肯定是 prime day 用的最多，如何应对一年一度的访问峰值的问题。
这轮应该也过了吧，抖音的同事说一般只有这轮过了才有下一轮

# eBay

eBay OOD，设计一个 chess game

开始设计 promoted listing，主要涉及 API design，backend design，DB，cache，LB，logging，monitoring，rate limiter，auth system，就是一个 seller 可能有 item1, item2, item3，然后这个 seller 去 eBay 买了推广，这些 item 会被 eBay 在首页或者别的地方推荐，然后会提供 seller 一个 dashboard 上面有各种 metrics，比如 click count, view count 这些 metric，要求设计这个系统和 API
（听起来是设计 metric collection system, 不是设计 promoted listing 本身是怎么实现的？）
（是的 针对的 metrics system）

crawler: 问你爬虫怎么驱虫 然后提了布隆过滤 讲了分布式存储, 不过面试官感觉不太 convince

rate limiter: 限流器, 从算法 配置讨论到 log 消息队列

rating system: 一个物品评分打星系统

然后问俩个 local meachine, 网络不好, 两边都有大文件, 怎么样判定文件完全相同 -答 checksum, hash
接着问怎样能够列出不相同的文件, 最后他希望用 tree

MySQL 的设计，需要尽量的规范化：normalization。减少数据冗余，但是查询比较麻烦，需要关联 Join。但是 NoSQL 需要反规范化 denormalize，为了方便查询而设计。例如：一个 video 在一个 date，一个小时内，view count，就可以存成这样：

```
    video_id + date_time | uploader_id | video_name | video_count:1500 | video_count:1600 | video_count:1700 |
```

# Amazon

## Amazon BQ / LP questions

    Tell me about a time when you have worked against tight deadlines and didn't have the time to consider all options before making a decision. What approach did you take?

    We ship millions of customer orders around the world, carried by different carriers like UPS, FedEx.  We report status of the delivery via a push notification and via website. These carriers have varying formats, SLAs, and QoSs. How would you design a system to maintain status of our shipments and report the same to the customer?
    
    Tell me about a time someone disagreed with your approach.
    
    Tell me about a time a customer wanted one thing, but you felt they needed something else. How did you approach the situation, what were your actions and what was the end result?
    
    Give me an example of a time when you didn't think you were going to meet the commitments you promised. How did you identify the risk and communicate it to stakeholders? What was the outcome?

    Assume you are using an app that has a feed. To edit content, you would click on a button to open a new screen which has an edit text. Hitting submit will kick off an http request and update the first screen. What are the various manual tests you can think of to test this flow?

    Design a system used for taxi reservation. How would you handle conditions such as users, scale and other conditions.

    Model a system which will allow an administrator to control the product visibility of a sale at Amazon using a given set of rules. The system should allow the administrator to create rules on transaction information and thus disabling or enabling products visible for sale, such as price, category, etc.

    Give an example of a tough or critical piece of feedback you received. What was it and what did you do about it?
    Tell me about a time when you took on something significant outside your area of responsibility. Why was it important? What was the outcome?

    Tell me about a time you made a hard decision to sacrifice short term gain for a longer term goal.
    
    Give an example of when you saw a peer struggling and decided to step in and help. What was the situation and what actions did you take? What was the outcome?
    
    Give me an example of when you took an unpopular stance in a meeting with peers and your leader and you were the outlier. What was it, why did you feel strongly about it, and what did you do?

BQ 半个小时，他从我的简历上挑了一段他感兴趣的实习经历，之后开始 dfs 式的提问。整个过程中对细节扣得非常细，比如我提到我在团队合作中帮助到了别人，他就会问我的帮助对别人具体产生了什么影响。我说我们团队需要考一个证书，他就问整个证书是干什么的，考这个证书都会涉及哪些知识哪些题型。我提了一下用户会要求一些定制化开发的内容，他就问具体哪一些是定制化的，最后的解决方案是什么。还问了我组里开会每天都会聊什么等等各种细节的东西。所以对于说过的每一句话每一个词，都会可能成为面试官提问你的理由。就这样，在浓浓的咖喱味儿口音中，我被提问了半个小时。

## Amazon System Design

Write a background service that queries the status on the backend by a certain interval.

Write a program that could determine the number of times a specific item is purchased.

接下来是 coding，除了一道比较奇怪的题目，不是算法题，偏向 ood。一个亚麻用户下单送货支付的场景，给我了一些 class，给了一些 rule，写一个 method 检查是否符合所有 rule。比如要 check paymant method, check item, check address 之类的一共 4 条 rule。写完之后，follow up 1，怎么支持更多的 payment method。follow up2。如果有更多的 rule，要加进来，程序改怎么拓展。我答了用 DI，印度老哥要求写 DI 的伪代码。最后时间不够了，匆匆写了一些伪代码。

## Amazon Coding

How would you design a class that behaves similar to a Java Map <Date,Object> except that get() returns the mapped value for not only an exact match but also for the latest Date in the Map

Thinking of Amazon Locker for example. Each Locker has a position and a size. Given the number of times a locker has been used, find the size that is most popular. 
    
Convert json file to object with the variable type(没说必须 json object， 问了面试官我假设就 hashmap 也行)
数据类型有：

    Map -”M”
    List- “L”
    Number- “N”
    String-”S”
    Boolean-”B”

    Input:
    Person: {
    name: “John”,
    age: 40,
    }
    Output:
    M: {Person:{
    S: {name: “John”},
    N: {age: 40}
    }}
