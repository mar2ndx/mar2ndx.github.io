---
title: "[Fundamental] Suffix Array "
category: Fundamental
tags: []
comments: true
date: 2015-01-27 00:00
---


[ref](http://www.geeksforgeeks.org/suffix-array-set-1-introduction/)

### Suffix Array

A suffix array is a sorted array of all suffixes of a given string.

**Any suffix tree based algorithm** can be replaced with an algorithm **that uses a suffix array** enhanced with additional information and solves the same problem in the same time complexity.

**Naive algorithm** for construction of suffix array is to consider all suffixes, sort them using a O(nLogn) sorting algorithm and while sorting, maintain original indexes. Time complexity is \_O(n^2 \* Logn)\_\_.

There is an advanced **nLogn Algorithm** algorithm available to read [here](http://www.geeksforgeeks.org/suffix-array-set-2-a-nlognlogn-algorithm/). Basic idea is to "Sort according to first two characters" and then "according to first four character".

Example question: **[Facebook] Query Search (HashMap, suffix array)**.
