---
title: 206. Reverse Linked List
category: Leetcode
tags: []
comments: true
date: 2022-11-20 05:54
---


Link: https://leetcode.cn/problems/reverse-linked-list/

# Question

difficulty: easy
adj diff: 3

    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Example 1:

    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
    Example 2:

    Input: head = [1,2]
    Output: [2,1]
    Example 3:

    Input: head = []
    Output: []

    Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

# Code

```
    public ListNode reverseList(ListNode head) {
        ListNode pre = null;
        ListNode cur = head;
        while (cur != null) {
            ListNode next = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next;
        }
        return pre;
    }
```
