---
title: 17.12. BiNode LCCI
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link：https://leetcode.cn/problems/binode-lcci/

# Question

difficulty: easy
adj diff: 3

    The data structure TreeNode is used for binary tree, but it can also used to represent a single linked list (where left is null, and right is the next node in the list). Implement a method to convert a binary search tree (implemented with TreeNode) into a single linked list. The values should be kept in order and the operation should be performed in place (that is, on the original data structure).

    Return the head node of the linked list after converting.

    Note: This problem is slightly different from the original one in the book.

    Example:

    Input:  [4,2,5,1,3,null,6,0]
    Output:  [0,null,1,null,2,null,3,null,4,null,5,null,6]

    Note:

    	The number of nodes will not exceed 100000.

这道题的逻辑就是一个中序遍历，不太难（注意 head 是如何存的）。

不过注意审题：“left is null, and right is the next node in the list”。

所以只要加一句：node.left = null; 就行了

# Code

```
    TreeNode preNode = null;
    TreeNode head = null;

    public TreeNode convertBiNode(TreeNode node) {
        helper(node);
        return head;
    }

    private void helper(TreeNode node) {
        if (node == null) return;
        helper(node.left);

    	// 中序遍历
        if (preNode != null) {
            preNode.right = node;
        }
        if (head == null) {
            head = node;
        }
        node.left = null;
        preNode = node;

        helper(node.right);
    }
```
