---
layout: post
title: "[Design] Distributed Network Bottleneck"
comments: true
category: Design
---

## Question

[link](http://www.mitbbs.com/article_t/JobHunting/32702821.html)

> 一个 distributed 的环境，有很多机器，现在你发现性能有问题，可能是网络带宽造成的，你怎么解决？ (你不能更换网络设备的前提下)

### Answer

1. Identify problem

首先得判定是否真的是网络造成的，就算是网络问题，哪些机器之间的网络问题？ 这个得先大概了解 high level component dependency relationship，

看看是不是 cpu memory disk 都没有问题。 可以 profile 几个机器看看是不是 a lot of time spent waiting for network calls.

2. Locate the faulty component

判定是网络问题之后看是哪些 components 之间，或是某个 component 里面有很多网络通讯。

3. Improvement

不能更换设备的话，能不能改 network topology 来让 critical path machine 之间的带宽有改善。

要是不能改 topology 就只能改程序了。还是先 identify top offender,然后就只能慢慢改了

4. What's more

要还有时间的话就可以聊聊问啥不能换设备，是资金问题还是用的已经是 top of the line 了？

或者是在 public cloud 上？

Answer suggested by user **remus**.
