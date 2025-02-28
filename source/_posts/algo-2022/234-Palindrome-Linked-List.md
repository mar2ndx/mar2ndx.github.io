---
title: 234. Palindrome Linked List
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---


Link: https://leetcode.cn/problems/palindrome-linked-list/

# Question

difficulty: easy
adj diff: 2

    Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

    Example 1:

    Input: head = [1,2,2,1]
    Output: true

    Example 2:

    Input: head = [1,2]
    Output: false
    Constraints:

    	The number of nodes in the list is in the range [1, 105].
    	0 <= Node.val <= 9

    Follow up: Could you do it in O(n) time and O(1) space?

# Code

```
    public boolean isPalindrome(ListNode head) {
        ListNode dummy = new ListNode(-1, head);
        ListNode slow = dummy;
        ListNode fast = dummy;
        Stack<Integer> stack = new Stack<Integer>();

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            stack.push(slow.val);
        }
        // eg. if -1 2 3 4    , slow = 3, fast = null, stack = {2, 3}
        // eg. if -1 2 3 4 5  , slow = 3, fast = 5   , stack = {2, 3}
        // eg. if -1 2 3 4 5 6, slow = 4, fast = null, stack = {2, 3, 4}

        // check palindrome: stack values against slow.next
        if (fast == null) {
            stack.pop();
        }
        while (!stack.isEmpty()) {
            slow = slow.next;
            if (stack.pop() != slow.val) {
                return false;
            }
        }
        return true;
    }
```
