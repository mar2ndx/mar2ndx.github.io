---
title: 331. Verify Preorder Serialization of a Binary Tree
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link: https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree/

# Question

difficulty: mid
adj diff: 4

    One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.

    For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.

    Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.

    It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.

    You may assume that the input format is always valid.

    	For example, it could never contain two consecutive commas, such as "1,,3".

    Note: You are not allowed to reconstruct the tree.
    Example 1:

    Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    Output: true

    Example 2:

    Input: preorder = "1,#"
    Output: false

    Example 3:

    Input: preorder = "9,#,#,1"
    Output: false
    Constraints:

    	1 <= preorder.length <= 104
    	preorder consist of integers in the range [0, 100] and '#' separated by commas ','.

这道题我并没有 pass，但是这段代码应该是 work 的。

只是超时。

# Code

```
    public boolean isValidSerialization(String preorder) {
        String[] nodesStr = preorder.split(",");
        char[] nodes = new char[nodesStr.length];
        for (int i = 0; i < nodesStr.length; i++) {
            nodes[i] = nodesStr[i].charAt(0);
        }
        return isValidTree(nodes, 0, nodes.length);
    }

    private boolean isValidTree(char[] nodes, int left, int right) {
        if (left == right) {
            return false;
        } else if (left + 1 == right) {
            return nodes[left] == '#';
        } else {
            if (nodes[left] == '#') {
                return false;
            } else if (nodes[left + 1] == '#') {
                return isValidTree(nodes, left + 2, right);
            }
            boolean found = false;
            for (int i = left + 2; i < right; i++) {
                // left tree is [left+1, i]
                // right tree is [i, right]
                if (!isValidTree(nodes, left + 1, i)) {
                    continue;
                }
                if (!isValidTree(nodes, i, right)) {
                    continue;
                }
                found = true;
                break;
            }
            return found;
        }
    }
```
