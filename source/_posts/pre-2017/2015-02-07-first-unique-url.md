---
title: "[Google] First Unique URL "
category: q-google
tags: []
comments: true
date: 2015-02-07 00:00
---


### Question

[link](http://www.careercup.com/question?id=11856466)

> Given a very long list of URLs, find the first URL which is unique ( occurred exactly once ).

> Must do it in one traversal.

### Solution

Suggested by the [top answer and second answer](http://www.careercup.com/question?id=11856466), using **a combination of trie and linked list**.

1. The leaf node of a trie maintains a flag to record duplicate urls and pointer to a node in a link list.

1. Use a doubly linked list to link all the unique ones
1. Remove the URL from the list if its count goes over 1
1. So after one traversal, the first one of your linked list is the desired one.

Alternatively, we can also use **Hash** instead of Trie.

### Code

not written
