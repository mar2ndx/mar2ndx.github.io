---
title: "[CC150v4] 14.3 Java Final, Finally and Finalize "
category: CC150v4
tags: []
comments: true
date: 2014-09-08 00:00
---


### Question

> What is the difference between Final, Finally, and finalize?

### final

**is a keyword**.

1. **Variable** decleared as final should be initialized only once and cannot be changed.
1. **Classes** declared as final cannot be extended.
1. **Methods** declared as final cannot be overridden.

Code:

    private final String name = "foo";

    public final String toString() {  return "NULL"; }

    // final can also make a class not "inheritable"
    public final class finalClass {...}
    public class classNotAllowed extends finalClass {...}
    // Not allowed

### finally

**is a block**.

The finally block **always executes** when the try block exits (even if an unexpected exception occurs).

    lock.lock();
    try {
        //do stuff
    } catch (SomeException se) {
        //handle se
    } finally {
        lock.unlock(); //always executed, even if Exception or Error or se
    }

### finalize

**is a method**.

**It's called by Garbage Collector** before reclaiming GC eligible objects.

    public void finalize() {
        //free resources (e.g. unallocate memory)
        super.finalize();
    }

[source1](http://www.java2novice.com/java_interview_questions/final-finally-finalize/)

[source2](http://javarevisited.blogspot.sg/2012/11/difference-between-final-finally-and-finalize-java.html)
