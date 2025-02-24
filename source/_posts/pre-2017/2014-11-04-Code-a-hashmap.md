---
layout: post
title: "[Google] Code a HashMap "
comments: true
category: q-google
---

### Question

[link](http://www.glassdoor.com/Interview/Code-a-hashmap-which-you-would-be-happy-to-place-into-a-production-environment-QTN_725885.htm)

> Code a hashmap which you would be happy to place into a production environment.

### Solution

We already write 2 post before:

1. **[Question] Implement a HashMap**

1. **[CC150v5] 8.10 Implement a Hashmap**

But still, this is not an easy question when asked at an interview. It won't harm to do a little recap:

1. The basic structure is an array. It can be:
   1. An array of linked nodes (with a next pointer).
   1. An array of linked list.
1. There should be a hash function.
1. There should be a function to convert the hash value to corresponding array index.
1. Remember there's **a concept of Load factor**. It means to what percentage the hashmap is filled.
1. h & (length – 1) means h % length, which maps a hashcode to an array index.
