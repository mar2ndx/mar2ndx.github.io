---
title: "[Google] Collatz Conjecture (Oneness property) "
category: q-google
tags: []
comments: true
date: 2015-02-04 00:00
---


### Collatz Conjecture

The [Collatz conjecture](http://en.wikipedia.org/wiki/Collatz_conjecture) is a conjecture in mathematics known as the 3n + 1 conjecture.

Take any natural number n.

1. If n is even, divide it by 2 to get n / 2.
1. If n is odd, multiply it by 3 and add 1 to obtain 3n + 1.

Repeat the process (which has been called "Half Or Triple Plus One", or HOTPO) indefinitely. The conjecture is that no matter what number you start with, **you will always eventually reach 1**.

The property has also been called **oneness**.

### Question

[link](http://stackoverflow.com/questions/5437445/collatz-conjecture-related-interview)

> Collatz conjecture says that if you do the following

    If n is even, replace n by n/2.
    If n is odd, replace n by 3n+1.
    You ultimately end up with 1.

> For instance, 5 -> 16 -> 8 -> 4 -> 2 -> 1

> Chain length is the number of steps required to get to 1. (The chain length of 1 is 0).

> Now, the problem is given natural numbers n and k, find all numbers between 1 and n, such that the chain length is <= k.

### Solution

Generate all numbers in backwards fashion, suggest by [templatetypedef](http://stackoverflow.com/a/5437672):

                      1
                      |
                      2
                      |
                      4
                      |
                      8
                      |
                      16
                      | \
                      32 \
                      |   5
                      64  |
                     /|   10
                    / 128 | \
                   21     20 3

**Implementation**: using a queue and keep appending numbers.

**Duplication handling**?

> Assuming that the Collatz conjecture holds true, we'll never get any duplicates this way.

**Time complexity** is O(S) time, where S is the number of numbers we need to output.

### Code

not written
