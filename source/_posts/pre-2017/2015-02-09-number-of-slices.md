---
title: "[Google] Number of slices "
category: q-google
tags: []
comments: true
date: 2015-02-09 00:00
---


### Question

[link](http://www.careercup.com/question?id=5090693043191808)

> Calculate the number of slices. Slice means that the difference between the maximum and minimum in the slice <= 2.

> eg. Given array 3 5 7 6 3.

> There're 10: (0,0) (1,1) (2,2) (3,3) (4,4) (5,5) (0,1) (1,2) (1,3) (2,3).

### Solution

If only asked to output the total number of such slices, we can do it in **O(n) using sliding-window-like algorithm**, with the help of addtional queue-like data structure.

This is **a very difficult question**! Quoted from the [top answer](http://www.careercup.com/question?id=5090693043191808):

> The basic idea is that you can start with arr[0] and then see **how many more elements you can include before you violate the max -min <= K constraint**. When you reach some index j you can no longer include, you know the maximum subarray starting at index 0 is arr[0...j-1], and you can count j different subarrays there.

> ... you then start with a[1]. Now [1...j-1] has to be valid, so you try to advance the right boundary again (try arr[1...j], then arr[1...j+1]) and so on until again you reach a point past which you can't advance. Then you'll try string at a[2], and so on. This is what they mean when they talk about **"crawling" over the array**.

> The key issue here is how you will check whether a particular subarray is valid efficiently...

Sliding window is explained above. Now, **the minMaxQueue** explain in [this pdf](https://codility.com/media/train/solution-count-bounded-slices.pdf):

> The PDF ... have **1 queue each** (i.e. 2 queues in total) for min and max (the min is treated analogous to the max case).

> For maxQueue, whenever a new value comes in the max queue, they remove all values less than the value, since those **can never be the max**. For that reason the queue's values are in descending order. And the max at any given time is the first element.

In this way, getting min/max is O(1), thus entire solution is O(n). Nice question!

### Code

Not written.
