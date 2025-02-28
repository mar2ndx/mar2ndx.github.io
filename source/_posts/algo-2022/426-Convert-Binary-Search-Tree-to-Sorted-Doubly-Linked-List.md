---
title: 426. Convert Binary Search Tree to Sorted Doubly Linked List
category: Leetcode
tags: []
comments: true
date: 2022-10-29 19:34
---


Link: https://leetcode.cn/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

# Question

difficulty: mid
adj diff: 3

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

Example 1:

Input: root = [4,2,5,1,3]

Output: [1,2,3,4,5]

Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

Example 2:

Input: root = [2,1,3]
Output: [1,2,3]

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
All the values of the tree are unique.

关于 public head 和 tail 节点的 null 处理，有一点点 tricky。

# Code

```
    Node head;
    Node tail;

    public Node treeToDoublyList(Node root) {
        if (root == null) {
            return root;
        }

        dfs(root);
        head.left = tail;
        tail.right = head;
        return head;
    }

    private void dfs(Node node) {
        if (node == null) return;
        dfs(node.left);
        if (tail == null) {
            head = node;
            tail = node;
        } else {
            tail.right = node;
            node.left = tail;
            tail = node;
        }
        dfs(tail.right);
    }
```
