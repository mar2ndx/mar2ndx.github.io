---
title: "[Java OOP] Singleton Pattern Introduction "
category: Java OOP
tags: []
comments: true
date: 2014-08-19 00:00
---


### Singleton Pattern

**Singleton** design pattern is one of the **2 most frequent topics** for OOD.

**[Singleton pattern](http://en.wikipedia.org/wiki/Singleton_pattern)** is a design pattern that restricts the instantiation of a class to one object.

#### in Java

Since Java 5.0, the easiest way to create a Singleton is the **[enum type approach](http://en.wikipedia.org/wiki/Singleton_pattern#The_Enum_way)**. Here the code is not given.

We will instead cover a very popular implementation: **[Lazy initialization](http://en.wikipedia.org/wiki/Singleton_pattern#Lazy_initialization)** using double-checked locking:

    public class SingletonDemo {
        private static volatile SingletonDemo instance = null;
        private SingletonDemo() { }
        public static SingletonDemo getInstance() {
            if (instance == null) {
                synchronized (SingletonDemo.class) {
                    if (instance == null) {
                        instance = new SingletonDemo();
                    }
                }
            }
            return instance;
        }
    }

An alternate simpler and cleaner version may be used at the expense of potentially lower concurrency in a multithreaded environment:

    public class SingletonDemo {
        private static SingletonDemo instance = null;
        private SingletonDemo() { }
        public static synchronized SingletonDemo getInstance() {
            if (instance == null) {
                instance = new SingletonDemo();
            }
            return instance;
        }
    }
