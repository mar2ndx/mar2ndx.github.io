---
title: "[Java OOP] Java Vector and ArrayList "
category: Java OOP
tags: []
comments: true
date: 2015-10-23 00:00
---


# Vector in Java

Vector class implements a **growable array** of objects.

It's an array, **not a list**.

# Vector VS ArrayList

1. Vectors are synchronized, ArrayLists are not.
1. Data Growth Methods (ArrayList grow by 1/2 of its size, while Vector doubles)

Usage: [ALWAYS use ArrayLists](http://stackoverflow.com/a/2986307)

> The vector was not the part of collection framework, it has been included in collections later. **It can be considered as Legacy code**.
>
> There is nothing about Vector which List collection cannot do. Therefore Vector **[should be avoided](http://beginnersbook.com/2013/12/difference-between-arraylist-and-vector-in-java/)**.
