---
title: "[CC150v5] 3.0 Example - Implement Stack "
category: CC150v5
tags: []
comments: true
date: 2014-09-15 00:00
---


### Question

> Implement a stack. 

### Solution

__Stack uses LinkedNode to implement__. 

### Code

    public class MyStack {

        Node top;

        public int pop() {
            if (top == null) {
                return -1;
            }
            int returnVal = top.val;
            top = top.next;
            return returnVal;
        }

        public int peek() {
            if (top == null) {
                return -1;
            }
            return top.val;

        }

        public void push(int val) {
            Node newNode = new Node(val);
            newNode.next = top;
            top = newNode;
        }

        class Node {

            int val;
            Node next;

            Node(int value) {
                val = value;
            }
        }
    }
