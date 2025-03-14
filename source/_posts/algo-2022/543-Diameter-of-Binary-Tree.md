---
title: 543. Diameter of Binary Tree
category: Leetcode
tags: []
comments: true
date: 2022-11-20 18:00
---



Link: https://leetcode.cn/problems/diameter-of-binary-tree/

# Question

difficulty: mid
adj diff: 4
Given the root of a binary tree, return the length of the diameter of the tree.

    The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

    The length of a path between two nodes is represented by the number of edges between them.

    

    Example 1:

    Input: root = [1,2,3,4,5]
    Output: 3
    Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

    Example 2:

    Input: root = [1,2]
    Output: 1

    

    Constraints:

        The number of nodes in the tree is in the range [1, 104].
        -100 <= Node.val <= 100

只需要借助一个 helper function 来 return depth就行了。

# Code

```
class Solution {
    
    int max = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        depth(root);
        return max - 1;
    }

    private int depth(TreeNode node) {
        if (node == null) return 0;
        int ll = depth(node.left);
        int rr = depth(node.right);
        max = Math.max(max, ll + 1 + rr);
        return Math.max(ll, rr) + 1;
    }
}
```
