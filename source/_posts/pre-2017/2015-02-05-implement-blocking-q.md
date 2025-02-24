---
layout: post
title: "[Google] Implement a Blocking Queue "
comments: true
category: q-google
---

### Question

[link](http://www.careercup.com/question?id=14622668)

> Implement a Blocking queue.

### Solution

First thing first, the most important characteristic of a BlockingQueue is:

> **thread-safe** BlockingQueue

Second, we need to make sure to handle the following 2 methods:

> **notifyAll();**
>
> **wait();**

Last, remember that **wait()** has got a **checked exception**(InterruptedException). We end up with the code:

    public synchronized void enqueue(Object item) throws InterruptedException {
    	while (this.queue.size() == this.size) {
    		wait();
    	}
    	if (this.queue.size() == 0) {
    		notifyAll();
    	}
    	this.queue.add(item);
    }

### Code

The entire class, refer to **[Java OOP] Java BlockingQueue (2)**:

    public class MyBlockingQueue {

        private List<Object> queue = new LinkedList<Object>();
        private int size = 10;

        public MyBlockingQueue(int size) {
            this.size = size;
        }

        public synchronized void enqueue(Object item) throws InterruptedException {
            while (this.queue.size() == this.size) {
                wait();
            }
            if (this.queue.size() == 0) {
                notifyAll();
            }
            this.queue.add(item);
        }

        public synchronized Object dequeue() throws InterruptedException {
            while (this.queue.size() == 0) {
                wait();
            }
            if (this.queue.size() == this.size) {
                notifyAll();
            }

            return this.queue.remove(0);
        }

        public boolean isEmpty() {
            return this.queue.isEmpty();
        }
    }
