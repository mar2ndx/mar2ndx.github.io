---
title: "[Java OOP] Interface and Abstract classes "
category: Java OOP
tags: []
comments: true
date: 2015-01-20 00:00
---


# Definition

[source](http://www.programmerinterview.com/index.php/java-questions/interface-vs-abstract-class/)

**A abstract class** is declared when it has one or more **abstract methods**.

**An interface** differs from an abstract class because an interface is not a class. An interface is essentially a type that **can be satisfied by any class** that implements the interface.

# The short answer

1. Abstract class is REAL parent.

1. Abstr can have data members and non-abstract methods
   while interface only got constant variable and abstract methods (read below)
1. class can implement multiple interface
   but only extend from 1 abstract class

### does interface got 'abstract' methods?

An interface is "purely" abstract class: every method is an abstract method. We do not use 'abstract' keyword. eg.

    interface Bicycle {
        void changeCadence(int newValue);
        void changeGear(int newValue);
        void speedUp(int increment);
        void applyBrakes(int decrement);
    }

> [According to the Java Language Specification](http://stackoverflow.com/a/641549), the abstract keyword for interfaces is obsolete and should no longer be used. (Section 9.1.1.1)

# The long answer

### Abstract classes: strong relationship

**Abstract classes** are meant to be inherited from, and often **indicates a strong relationship**.

For instance, if we have an abstract base class called "Canine", any deriving class should be an animal that belongs to the Canine family (like a Dog or a Wolf).

**With an interface on the other hand**, the relationship is **not necessarily strong**.

For example, if we have a class called "House", that class could also implement an interface called "AirConditioning". Having air conditioning not an essential part of a House.

**A TownHouse** is a type of House, that relationship is very strong, and would be more appropriately defined **through inheritance** instead of interfaces.

### What's more

1. Multiple inheritance

   Java class can inherit from only one abstract class, but can implement multiple interfaces.

1. Abstract method

   Abstract class can have non-abstract methods with actual implementation details.

### When to use which

**Use abstract class when**:

1. You want to **[share code](http://docs.oracle.com/javase/tutorial/java/IandI/abstract.html)** among several closely related classes.

1. you want to be able to declare **non-public members**. In an interface, all methods must be public.

1. you think you will need to **add methods** in the future.

   Because if you add new method headings to an interface, then all of the classes that already implement that interface will have to be changed to implement the new methods. That can be quite a hassle.

**Use interface when**:

1. You expect that **unrelated classes** would implement your interface. For example, the interfaces **Comparable and Cloneable** are implemented by many unrelated classes.

1. you think that the API will not change for a while.

1. you want to have something similar to multiple inheritance.
