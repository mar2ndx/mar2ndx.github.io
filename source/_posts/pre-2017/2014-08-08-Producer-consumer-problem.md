---
title: "[Design] Producer Consumer Problem"
category: Design
tags: []
comments: true
date: 2014-08-08 00:00
---


### Overview

Producer-consumer problem illustrates the need for **synchronization** in systems where **many processes share a resource**.

[In the problem](http://cs.gmu.edu/cne/modules/ipc/aqua/producer.html), two processes share a fixed-size buffer. One process produces information and puts it in the buffer, while the other process consumes information from the buffer. These processes do not take turns accessing the buffer, they both work concurrently.

### Inadequate Solution

![](/images/producer-workflow.gif)

![](/images/consumer-workflow.gif)

**The code might look like this**:

    BufferSize = 3;
    count = 0;

    Producer()
    {
        int widget;
        WHILE (true) {                     // loop forever
           make_new(widget);               // create a new widget to put in the buffer
           IF(count==BufferSize)
               Sleep();                    // if the buffer is full, sleep
           put_item(widget);               // put the item in the buffer
           count = count + 1;              // increment count of items
           IF (count==1)
               Wakeup(Consumer);           // if the buffer was previously empty, wake
        }                                  //  the consumer
    }

    Consumer()
    {
        int widget;
        WHILE(true) {                    // loop forever
          IF(count==0)
               Sleep();                  // if the buffer is empty, sleep
          remove_item(widget);           // take an item from the buffer
          count = count + 1;             // decrement count of items
          IF(count==N-1)
                Wakeup(Producer);        // if buffer was previously full, wake
                                         //  the producer
          Consume_item(widget);          // consume the item
        }
    }

This [will cause problems](http://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem#Inadequate_implementation), because **it contains a race condition** that can lead to a deadlock. Or in simply words, it has the potential of [losing wakeups](http://cs.gmu.edu/cne/modules/ipc/purple/prodsem.html).

An alternative analysis is that if the programming language does not define the semantics of **concurrent accesses to shared variables (in this case itemCount)** without use of synchronization, then the solution is unsatisfactory for that reason, without needing to explicitly demonstrate a race condition.

Solutions are: **semaphores or monitors**.

### Semaphore

    semaphore mutex = 1;
    semaphore fillCount = 0;
    semaphore emptyCount = BUFFER_SIZE;

    procedure producer() {
        while (true) {
            item = produceItem();
            down(emptyCount);
                down(mutex);
                    putItemIntoBuffer(item);
                up(mutex);
            up(fillCount);
        }
    }

    procedure consumer() {
        while (true) {
            down(fillCount);
                down(mutex);
                    item = removeItemFromBuffer();
                up(mutex);
            up(emptyCount);
            consumeItem(item);
        }
    }

### Monitor

    monitor ProducerConsumer {
        int itemCount;
        condition full;
        condition empty;

        procedure add(item) {
            while (itemCount == BUFFER_SIZE) {
                wait(full);
            }

            putItemIntoBuffer(item);
            itemCount = itemCount + 1;

            if (itemCount == BUFFER_SIZE -1) {
                notify(full);
            }
        }
        procedure remove() {
            while (itemCount == 0) {
                wait(empty);
            }

            item = removeItemFromBuffer();
            itemCount = itemCount - 1;

            if (itemCount == 1) {
                notify(empty);
            }


            return item;
        }
    }

    procedure producer() {
        while (true) {
            item = produceItem();
            ProducerConsumer.add(item);
        }
    }

    procedure consumer() {
        while (true) {
            item = ProducerConsumer.remove();
            consumeItem(item);
        }
    }
