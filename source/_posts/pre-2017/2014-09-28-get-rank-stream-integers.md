---
title: "[CC150v5] 11.8 Get Rank in Stream of Integers "
category: CC150v5
tags: []
comments: true
date: 2014-09-28 00:00
---


### Question

> Imagine you are reading in a stream of integers. Periodically, you wish to be able to look up the rank of a number x (the number of values less than or equal to x).

> Implement the data structures and algorithms to support these operations. That is, implement the method **track(int x)**, which is called when each number is generated, and the method **getRankOfNumber(int x)**, which returns the number of values less than or equal to x (not including x itself).

### Solution

**This question requires a special type of Data Structure**. It basically is a modified BST like this:

> The tree node stores both number value and the **count of node on left subtree**

![](/images/get-rank-number-stream.png)

Suppose we want to find the rank of 24 in the tree above. We would compare 24 with the root, 20, and find that 24 must reside on the right. The root has 4 nodes in its left subtree, and when we include the root itself, this gives us five total nodes smaller than 24. We set counter to 5.

Then, we compare 24 with node 25 and find that 24 must be on the left. The value of counter does not update, since we're not "passing over" any smaller nodes. The value of counter is still 5.

Next, we compare 24 with node 23,and find that 24 must be on the right. Counter gets incremented by just 1 (to 6), since 23 has no left nodes.

Finally, we find 24 and we return counter: 6.

### Code

Refer to another post **[Question] Stock Span Problem**.
