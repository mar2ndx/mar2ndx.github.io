---
title: 445. Add Two Numbers II
category: Leetcode
tags: []
comments: true
date: 2024-07-16 17:49
---


Link: [445. Add Two Numbers II](https://leetcode.cn/problems/add-two-numbers/description/)

# Question

difficulty: mid
adj diff: ?

    You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example 1:

    Input: l1 = [7,2,4,3], l2 = [5,6,4]
    Output: [7,8,0,7]
    Example 2:

    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [8,0,7]
    Example 3:

    Input: l1 = [0], l2 = [0]
    Output: [0]
    
    Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.    

    Follow up: Could you solve it without reversing the input lists?

# Code

两种办法：

1. 三次链表反转，具体代码参考 https://mar2ndx.github.io/2022/10/08/algo-2022-206-Reverse-Linked-List/

1. 用Stack，更加推荐，代码简单。

方法2，如下：

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Stack<Integer> s1 = new Stack<Integer>();
        Stack<Integer> s2 = new Stack<Integer>();
        while (l1 != null) {
            s1.push(l1.val);
            l1 = l1.next;
        }
        while (l2 != null) {
            s2.push(l2.val);
            l2 = l2.next;
        }
        int carry = 0;
        ListNode ans = new ListNode();

        while (!s1.isEmpty() || !s2.isEmpty()) {
            int sum = carry + 
                (s1.isEmpty() ? 0 : s1.pop()) +
                (s2.isEmpty() ? 0 : s2.pop());
            ans.val = sum % 10;
            carry = sum / 10;
            ListNode tmp = new ListNode();
            tmp.next = ans;
            ans = tmp;
        }

        if (carry > 0) ans.val = carry;
        else ans = ans.next;
        return ans;
    }
