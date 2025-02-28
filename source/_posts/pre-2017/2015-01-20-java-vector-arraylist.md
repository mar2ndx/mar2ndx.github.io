---
title: "[Java OOP] Java Vector and ArrayList "
category: Java OOP
tags: []
comments: true
date: 2015-01-20 00:00
---


### Difference

1. Vectors are synchronized, ArrayLists are not.

1. Data Growth Methods

   [A Vector defaults to](http://stackoverflow.com/a/2986307) doubling the size of its array, while the ArrayList increases its array size by 50 percent.

### Similarities

1. Both Vector and ArrayList use **growable array** data structure.

1. They both are **ordered collection classes** as they maintain the elements insertion order.

1. Vector & ArrayList both allows duplicate and null values.

1. They both grows and shrinks automatically when overflow and deletion happens.

[source](http://beginnersbook.com/2013/12/difference-between-arraylist-and-vector-in-java/)

### History

The vector was not the part of collection framework - it has been included in collections later. It can be considered as **Legacy code**.

**There is nothing about Vector which List collection cannot do**. Therefore Vector should be avoided. If there is a need of thread-safe operation, make ArrayList synchronized.
