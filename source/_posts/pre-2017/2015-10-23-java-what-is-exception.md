---
title: "[Java OOP] What is Java Exception"
category: Java OOP
tags: []
comments: true
date: 2015-10-23 00:00
---


# The class

**[The class Exception](http://docs.oracle.com/javase/7/docs/api/java/lang/Exception.html)** and its subclasses are a form of **Throwable** that indicates conditions that a reasonable application might want to catch.

# The object

**[An exception is an event](https://docs.oracle.com/javase/tutorial/essential/exceptions/definition.html)**, which occurs during the execution of a program, that disrupts the normal flow of the program's instructions.

**When an error occurs** within a method, the method **creates an object and hands it off to the runtime system**. The object, called an **exception object**, contains information about the error(eg. type, state etc).

## throw this object out!

Creating an exception object and handing it to the runtime system is called **throwing an exception**.

After a method throws an exception, the runtime system (i.e. **JVM**) attempts to find something to handle it. This is **exception handler**.
