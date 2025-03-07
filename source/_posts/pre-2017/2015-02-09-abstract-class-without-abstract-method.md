---
title: "[Java OOP] Can abstract class have 0 abstract method? "
category: Java OOP
tags: []
comments: true
date: 2015-02-09 00:00
---


# Definition

[An abstract class](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html) is a class that is declared abstract —it may or may not include abstract methods. Abstract classes cannot be instantiated, but they can be subclassed.

## with NO abstract method?

> [In JDK 1.0 it was](http://stackoverflow.com/a/2283437) indeed necessary to have **at least one abstract method** in an abstract class.
>
> This restriction was removed in JDK 1.1 (1997? (I'm old)) and such classes added to the Java library, such as java.awt.event.KeyAdapter.

**So, no abstract method is fine**. Doing it prevents you from instantiation - you can only inherit.

However, different opinions are:

> [is subjective](http://stackoverflow.com/a/2283450) and a matter of style. **Personally I would say yes**. If your intent is to prevent a class (with no abstract methods) from being instantiated, the best way to handle this is with a privateprotected constructor, not by marking it abstract.

## how about abstract variable?

There is no such thing in Java.

For more on abstract class, read **[Java OOP] Template method pattern**.
