---
title: "[Java OOP] Observer pattern "
category: Java OOP
tags: []
comments: true
date: 2014-09-02 00:00
---


### Observer pattern

**[The observer pattern](http://en.wikipedia.org/wiki/Observer_pattern)** is a software design pattern in which an object(subject) maintains a list of dependents(observers), and notifies them automatically of any state changes (usually by calling one of their methods).

The Observer pattern is mainly used to implement distributed event handling systems. It's also **a key part in MVC architectural pattern**.

### Example

A mailing list example.

Each student in the mailing list would be a listener/observer, and teacher would be announcer/subject.

So in the code, there's a Listener Interface that all students implement. There's a update() method in the interface, where each student define their own implementation.

Teacher would keep a list of Listeners. When there's any news, teacher would call update() on each object.
