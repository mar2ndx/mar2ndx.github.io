---
layout: post
title: "[Design] Big Data - Top k Frequency"
comments: true
categories:
  - Design
  - z-top-K
---

### Question

[link](http://blog.csdn.net/v_JULY_v/article/details/6256463)

> 搜索引擎会通过日志文件把用户每次检索使用的所有检索串都记录下来，每个查询串的长度为 1-255 字节。

> 假设目前有一千万个记录（这些查询串的重复度比较高，虽然总数是 1 千万，但如果除去重复后，不超过 3 百万个。一个查询串的重复度越高，说明查询它的用户越多，也就是越热门。），请你统计最热门的 10 个查询串，要求使用的内存不能超过 1G。

### Analysis

1. divide and conquer (for large input)

1. Query 统计 (hash/trie)

1. 根据统计结果，找 Top 10 (minheap / quickselect)

Be careful: 内存不能超过 1G，10 million 条记录，每条记录是 255Byte，很显然要占据 2.375G 内存.

### Query 统计

#### Option 1: HashMap

虽然有一千万个 Query，但是由于重复度比较高，因此事实上只有 300 万的 Query，每个 Query 255Byte，因此我们可以考虑把他们都放进内存中去。

Hash Table 绝对是我们优先的选择，因为 Hash Table 的查询速度非常的快，几乎是 O(1)的时间复杂度。我们在 O(N)的时间复杂度内完成了对该海量数据的处理。

#### Option 2: trie

> 这题是考虑时间效率。用 trie 树统计每个词出现的次数，时间复杂度是 O(n x le)（le 表示单词的平准长度）。然后是找出出现最频繁的前 10 个词，可以用堆来实现，前面的题中已经讲到了，时间复杂度是 O(n x lg10)。所以总的时间复杂度，是 O(n x le)与 O(n x lg10)中较大的哪一个。

How to use Trie to calculate word frequency?

> 在 Trie 的 node 节点中[添加 count 域后](http://blog.csdn.net/ohmygirl/article/details/7953814)，可以统计单词出现的次数。统计的方法就是在插入单词的时候，令相应的 count 域加 1（初始化为 0）.

### 找 Top 10

**Heap**.

借助堆结构，我们可以在 log 量级的时间内查找和调整/移动。因此到这里，我们的算法可以改进为这样，维护一个 K(该题目中是 10)大小的小根堆，然后遍历 300 万的 Query，分别和根元素进行对比。

查找目标元素的时间复杂度为 O(logK)。

### Quickselect

refer to another pose **[Fundamental] Quickselect**.

### Conclusion

至此，算法就完全结束了。(这道题，我们不需要分治)。经过上述第一步、先用 Hash 表统计每个 Query 出现的次数，O（N）；然后第二步、采用堆数据结构找出 Top 10，O(NlogK)。所以，我们最终的时间复杂度是：O（N） + O(N'logK)。
