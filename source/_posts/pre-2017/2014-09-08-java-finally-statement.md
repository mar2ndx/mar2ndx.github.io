---
title: "[CC150v4] 14.2 Java Finally Statement "
category: CC150v4
tags: []
comments: true
date: 2014-09-08 00:00
---


### Question

> In Java, does the finally block gets executed if we insert a return statement inside the try block of a try-catch-finally?

### Solution

Yes, it will.

Even when we attempt to exit within the try block (normal exit, return, continue, break or any exception), **the finally block will still be executed**.

The only time finally [won't be called](http://stackoverflow.com/a/65049) is if you call System.exit() or if the JVM crashes first.
