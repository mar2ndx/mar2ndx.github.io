---
layout: post
title: "[Java OOP] Why avoid using Protected? "
comments: true
category: Java OOP
---

# Overview

Some experienced developers don’t use **protected** since it cannot provide clean data hiding.

Why is that?

## background

Remembering in the post **[Java OOP] Java modifier and Access Level**, we got this:

![](/images/java-access-level-table.png)

**Note**: Java default access setting is 'No modifier', which is also called '**Package Private**'.

**Another note**: by saying 'subclass', it means subclass declared in **another package**.

And in **[Design] Composition Over Inheritance**, we know that basically **inheritance breaks encapsulation**.

## the reason

1. inheritance is seldom the best tool and is not as flexible

1. the protected members form an interface towards subclasses (which is bad)

1. interfaces are tricky to get right and document properly

So, [it's better not to make](http://stackoverflow.com/questions/4913025/reasons-to-use-private-instead-of-protected-for-fields-and-methods) the class inheritable and instead make sure it's as flexible as possible (and no more) by using other means.

## A excellent answer

A excellent answer [from Sam Brand](http://programmers.stackexchange.com/questions/162643/why-is-clean-code-suggesting-avoiding-protected-variables):

1. They tend to lead to **[YAGNI](https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it)** issues. Unless you have a descendant class that actually does stuff with the protected member, make it private.

   > **"You aren't gonna need it"** (acronym: YAGNI) is a principle of extreme programming (XP) that states a programmer should not add functionality until deemed necessary.

1. They tend to lead to **[LSP](https://en.wikipedia.org/wiki/Liskov_substitution_principle)** issues. Protected variables generally have some intrinsic invariance associated with them (or else they'd be public). Inheritors then need to maintain those properties, which people can screw up or willfully violate.

   > **Substitutability** is a principle in OOP. It states that if S is a subtype of T, then objects of type T may be replaced with objects of type S without altering any of the desirable properties of that program

   > **Liskov substitution principle (LSP)** is a particular definition of a subtyping relation introduced by Barbara Liskov in 1987

1. They tend to violate **[OCP](https://en.wikipedia.org/wiki/Open/closed_principle)**. If the base class makes too many assumptions about the protected member, or the inheritor is too flexible with the behavior of the class, it can lead to the base class' behavior being modified by that extension.

   > **open/closed principle** states "software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification".

   > That is, such an entity can allow its behaviour to be extended without modifying its source code.

   > This is especially valuable in a production environment, where changes to source code may necessitate code reviews, unit tests, and other such procedures to qualify it for use in a product

1. They tend to lead to inheritance for extension rather than composition. This tends to lead to tighter coupling, more violations of **[SRP](https://en.wikipedia.org/wiki/Single_responsibility_principle)**, more difficult testing, and a slew of other things that fall within the 'favor composition over inheritance' discussion.

> **single responsibility principle** states that every class should have responsibility over a single part of the functionality provided by the software, and that responsibility should be entirely encapsulated by the class. All its services should be narrowly aligned with that responsibility

# An example

ClassA in packageA:

    package packA;

    import packB.ClassB;

    public class ClassA {

        protected int val = 10;

        protected String getColor() {
            return "colored";
        }

        public static void main(String[] args) {
            ClassA ins = new ClassA();
            System.out.println("val is " + ins.val);
            System.out.println("color is " + ins.getColor());
            System.out.println();

            ClassB ins2 = new ClassB();
            System.out.println("val is " + ins2.val);
            System.out.println("color is " + ins2.getColor());
        }
    }

ClassB in packageB:

    package packB;

    import packA.ClassA;

    public class ClassB extends ClassA {

        public ClassB() {
            val = 5;
        }

        public String getColor() {
            return super.getColor();
        }
    }

Execution result:

    val is 10
    color is colored

    val is 5
    color is colored

The code shows how **ClassB** is able to access 1 **protected variable** and 1 **protected method**.
