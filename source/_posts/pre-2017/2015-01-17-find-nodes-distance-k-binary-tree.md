---
title: "[Amazon] Find nodes of distance k from Binary Tree "
category: Question
tags: []
comments: true
date: 2015-01-17 00:00
---


### Question

[link](http://www.careercup.com/question?id=15069740)

> Find the nodes at d distance from a certain node in a Binary Tree

### Solution

[There are two types](http://www.geeksforgeeks.org/print-nodes-distance-k-given-node-binary-tree/) of nodes to be considered:

1. Nodes in the subtree rooted of the target node.
1. Other nodes, may be an ancestor of target, or a node in some other subtree.

The details of find these nodes:

1. Find the nodes which can be reached in k hops from the given node.

2. Second part we look at those nodes **on the upper part of the tree**. The parent of the given node is 1 hop away. Hence in the **other child subtree** of the parent, we find nodes with k-1 hops.

   Similarly the grand parent of B, we find nodes with k - 2 distance.

Implementation:

1. Start from root, **store all nodes in a queue** of maximum size k till you reach the given node.

1. Call FindNodesAtDistance() on the nodes from the queue to get all the nodes **distance k -i** from the node.
