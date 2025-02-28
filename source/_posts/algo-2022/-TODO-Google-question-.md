---
title: Google questions
category: Leetcode
tags: []
comments: true
date: 2022-11-17 08:56
---



# Leetcode

https://leetcode.cn/problems/shortest-path-in-a-grid-with-obstacles-elimination/

https://leetcode.cn/problems/path-with-maximum-probability/

# Q1

排序以下 table:

    name  |  start  |  end
    abc          3          8
    bcd          7         10
    cde          3          6

output:

    3    -    6      abc, cde
    6    -    7      bcd
    7    -    8      bcd, cde
    8    ‍‌‌‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍-    10    bcd

Solution：用 Heap。类似：https://mar2ndx.github.io/2014/07/01/The-Skyline-Problem/

# Q2

一片房子有三个社区，

    {
        {8, 2, 7},
        {3, 1, 5},
        {4, 8, 9}
    }

排序所有的社区 并且每个社区不能有同样的门牌号（每个数字代表一个门牌号）

完全没看懂。source：https://www.1point3acres.com/bbs/thread-944293-1-1.html

# Q3

    有一个list，
    [( 'John',5), ('Mary',4), ('Sherry',10), ('John',3),('Mary',3),...........]
    这个list里有重复的人名，每个人名对应是他们短信里的字数。 给你这样一个list和特定数字N，要求你返回前N个最活跃的用户量。
    我用了dict来计数，计每个人一共说了多少话。然后就排序了。
    我是fail了。
    面我的是一个 很有好的国人小哥，在狗家工作了9个月的。 他和我说，这个时间复杂度太大了，当 这个list里的用户成千上万的时候。
    让我想有没有其他方法减少时间复杂度。我想不出来。 他大‍‌‌‌‍‌‌‍‌‍‌‌‍‌‌‍‌‍概给了我方向是用最大堆做。

# Q4

    第一题比较简单 就是non-decreasing contiguous array那道题，然后第二题就是第一题的变形， 你可以改变其中一个数字 比如原本[1,0,0,0,0,3,4] 你可以改掉0变成1 然后找到最长contiguous non decreasing array

其他参考：

https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/

https://leetcode.cn/problems/contiguous-array/

https://leetcode.cn/problems/non-decreasing-array/solution/

# Q5

    一个白人老大爷出的题
    给一个N面的骰子 一个小人 一段无限长的一维坐标 给一段范围[a,b] 小人从0点出发 根据骰子走x步 骰子可以掷无数次 小人走到[a, b]这个范围内包括a和b就算获胜

source：https://www.1point3acres.com/bbs/thread-942744-1-1.html

# 其他

https://www.1point3acres.com/bbs/thread-941066-1-1.html
https://www.1point3acres.com/bbs/thread-942679-1-1.html
https://www.1point3acres.com/bbs/thread-942984-1-1.html
https://www.1point3acres.com/bbs/thread-935670-1-1.html
https://www.1point3acres.com/bbs/thread-935154-1-1.html
