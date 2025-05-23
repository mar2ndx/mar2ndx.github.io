---
title: "[Design] Big Data - Top k Frequency (case analysis)"
category: Design
tags: []
comments: true
date: 2014-08-10 00:00
---


### Question

[link](http://dongxicheng.org/big-data/select-ten-from-billions/)

> 在海量数据中找出出现频率最高的前 K 个数，或者从海量数据中找出最大的前 K 个数，这类问题通常称为“top K”问题，

> 1. top K value
> 1. top K frequency

### Analysis

**Standard solution** is 【分治+trie 树/hash+小顶堆/quickselect】, which I covered in another post [Big Data - Top k Frequency](/design/2014-07-25-big-data-Top-k-frequency). Briefly it is 3 steps:

1. 先将数据集按照 hash 方法分解成多个小数据集，
1. 使用 trie 树或者 hash 统计每个小数据集中的 query 词频，
1. 用小顶堆/quickselect 求出每个数据集中出频率最高的前 K 个数

But, there're other senarios where different solutions may apply. Consider:

1. Single core vs. multiple core

1. Single PC vs. multiple PC

1. Large RAM vs. limited RAM

1. Distributed system

### 1. 单机+单核+足够大内存

设每个查询词平均占 8Byte，则 10 亿个查询词所需的内存大约是 10^9\*8=8G 内存。如果你有这么大的内存，直接在内存中对查询词进行排序，顺序遍历找出 10 个出现频率最大的 10 个即可。这种方法简单快速，更加实用。当然，也可以先用 HashMap 求出每个词出现的频率，然后求出出现频率最大的 10 个词。

### 2. 单机+单核+受限内存

这种情况下，需要将原数据文件切割成一个一个小文件，如，采用 hash(x)%M，将原文件中的数据切割成 M 小文件，如果小文件仍大于内存大小，继续采用 hash 的方法对数据文件进行切割，直到每个小文件小于内存大小，这样，每个文件可放到内存中处理。采用 3.1 节的方法依次处理每个小文件。

### 3. 单机+多核+足够大内存

这时可以直接在内存中实用 hash 方法将数据划分成 n 个 partition，每个 partition 交给一个线程处理，线程的处理逻辑是同[1]节类似，最后一个线程将结果归并。

该方法存在一个瓶颈会明显影响效率，即数据倾斜，每个线程的处理速度可能不同，快的线程需要等待慢的线程，最终的处理速度取决于慢的线程。解决方法是，**将数据划分成 (c x n)个 partition（c>1），每个线程处理完当前 partition 后主动取下一个 partition 继续处理**，直到所有数据处理完毕，最后由一个线程进行归并。

### 4. 多机+受限内存

这种情况下，为了合理利用多台机器的资源，可将数据分发到多台机器上，每台机器采用[3]节中的策略解决本地的数据。可采用**hash + socket**方法进行数据分发。

### 5. Distributed

Top k 问题很适合采用**MapReduce 框架**解决，用户只需编写一个 map 函数和两个 reduce 函数，然后提交到 Hadoop（采用 mapchain 和 reducechain）上即可解决该问题。

A map function. 对于 map 函数，采用 hash 算法，将 hash 值相同的数据交给同一个 reduce task.

2 reduce functions. 对于**第一个 reduce 函数**，采用 HashMap 统计出每个词出现的频率，对于**第二个 reduce 函数**，统计所有 reduce task 输出数据中的 top k 即可。

### 6. Other

公司一般不会自己写个程序进行计算，而是提交到自己核心的数据处理平台上计算，该平台的计算效率可能不如直接写程序高，但它具有**良好的扩展性和容错性**，而这才是企业最看重的。
