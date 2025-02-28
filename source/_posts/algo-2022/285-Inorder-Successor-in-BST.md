---
title: 285. Inorder Successor in BST
category: Leetcode
tags: []
comments: true
date: 2022-11-18 16:23
---


Link: https://leetcode.cn/problems/inorder-successor-in-bst/

# Question

difficulty: mid
adj diff: 4

    Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

    The successor of a node p is the node with the smallest key greater than p.val.

    Example 1:

    Input: root = [2,1,3], p = 1
    Output: 2
    Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

    Example 2:

    Input: root = [5,3,6,2,4,null,null,1], p = 6
    Output: null
    Explanation: There is no in-order successor of the current node, so the answer is null.

    Constraints:

    	The number of nodes in the tree is in the range [1, 104].
    	-105 <= Node.val <= 105
    	All Nodes will have unique values.

主要是学会怎么用 Stack 来写 binary tree 的中序遍历。

key：每次都推整个 left branch 入栈。

# Code

```
class Solution {
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        // push the entire left branches
        while (root != null) {
            stack.push(root);
            root = root.left;
        }

        boolean foundPreNode = false;
        while (!stack.isEmpty()) {
            TreeNode nextNode = stack.pop();
            if (foundPreNode) {
                return nextNode;
            } else if (nextNode == p) {
                foundPreNode = true;
            }
            // if have right child, push left branches of right child
            if (nextNode.right != null) {
                stack.push(nextNode.right);
                while (stack.peek().left != null) {
                    stack.push(stack.peek().left);
                }
            }
        }
        return null;
    }
}
```
