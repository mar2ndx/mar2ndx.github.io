---
title: "[Java OOP] Java Runtime Exception "
category: Java OOP
tags: []
comments: true
date: 2014-12-23 00:00
---


### Exceptions in Java

In Java, there are [3 categories of exceptions](http://www.tutorialspoint.com/java/java_exceptions.htm):

1. checked exceptions
   1. Typically a user error
   1. eg. if a file cannot be found.
   1. These exceptions cannot simply be ignored at the time of compilation.
1. runtime exceptions (also called un-checked exceptions)

   1. exception that could have been avoided by the programmer
   1. eg. NullPointerException
   1. ignored at the time of compilation

1. error
   1. These are not exceptions at all
   1. eg. stack overflow occurs
   1. also ignored at the time of compilation

#### 1. checked exception

[A checked exception](http://stackoverflow.com/a/2190175) **must be handled explicitly** by the code (by either putting a try/catch block around the code, or adding a "throws" clause to the method).

The [class Exception](http://docs.oracle.com/javase/7/docs/api/java/lang/Exception.html) and any subclasses that are not also subclasses of RuntimeException are **checked exceptions**. Example:

1. FileNotFoundException
1. HttpRetryException
1. SocketException
1. IOException

Note: **java.lang.RuntimeException** is a subclass of **java.lang.Exception**.

#### 2. un-checked exceptions (RuntimeException)

A un-checked exception **does not need** to be explicitly handled.

[RuntimeException](http://docs.oracle.com/javase/7/docs/api/java/lang/RuntimeException.html) and its subclasses are **unchecked exceptions**.

[Generally](http://stackoverflow.com/a/2190177) RuntimeExceptions **can be prevented** programmatically. E.g NullPointerException, ArrayIndexOutOfBoundException. If you check for null before calling any method, NullPointerException would never occur. Similarly ArrayIndexOutOfBoundException would never occur if you check the index first. RuntimeException are not checked by the compiler, so it is clean code.

The runtime exception classes **[are exempted](http://stackoverflow.com/a/2190659) from compile-time checking**, since the compiler cannot establish that run-time exceptions cannot occur.
