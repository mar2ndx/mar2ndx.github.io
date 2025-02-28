---
title: "[Question] Overriding private method"
category: Question
tags: []
comments: true
date: 2014-08-01 00:00
---


### Question

[link](http://stackoverflow.com/questions/2000137/overriding-private-methods-in-java)

> Can we overriding private method in Java?

### Analysis

> Overriding private methods in Java is invalid because a parent class's private methods are "automatically final, and hidden from the derived class". [source](http://www.linuxtopia.org/online_books/programming_books/thinking_in_java/TIJ309_006.htm)

### Solution

You can't override a private method, but you can introduce one in a derived class [without a problem](http://stackoverflow.com/a/2000156). Read more below.

### Code

**not a problem**

    public class OverridePrivateMethod {
    	private void foo() {
    	}
    }

    class Child extends OverridePrivateMethod {
    	private void foo() {
    	}
    }

**add @Override annotation and get error**

    public class OverridePrivateMethod {
    	private void foo() {
    	}
    }

    class Child extends OverridePrivateMethod {
    	@Override
    	private void foo() {
    	}
    }
