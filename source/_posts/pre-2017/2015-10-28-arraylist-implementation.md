---
layout: post
title: "[Java OOP] Java ArrayList implementation "
comments: true
category: Java OOP
---

# Overview

**[Resizable-array](http://docs.oracle.com/javase/7/docs/api/java/util/ArrayList.html)** implementation of the List interface. (it's actually an [array of Object](http://stackoverflow.com/a/7382507))

It's not synced.

## Underlying design

1. **Random access** – no need to traverse thru all nodes.

1. **Circular array** - Array size is pre-defined. Use head and tail to keep track of list position.

1. **Insertion and deletion** - Implement **shiftRight()** and shiftLeft() methods.

Actual code will come later...
