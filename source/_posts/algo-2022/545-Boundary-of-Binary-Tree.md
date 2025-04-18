---
title: 545. Boundary of Binary Tree
category: Leetcode
tags: []
comments: true
date: 2022-11-12 00:06
---



Link: https://leetcode.cn/problems/boundary-of-binary-tree/

# Question

difficulty: mid
adj diff: 4

    The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

    The left boundary is the set of nodes defined by the following:

        The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
        If a node in the left boundary and has a left child, then the left child is in the left boundary.
        If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
        The leftmost leaf is not in the left boundary.

    The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

    The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

    Given the root of a binary tree, return the values of its boundary.

    Example 1:

![](/images/leetcode-545-1.jpg)

    Input: root = [1,null,2,3,4]
    Output: [1,3,4,2]
    Explanation:
    - The left boundary is empty because the root does not have a left child.
    - The right boundary follows the path starting from the root's right child 2 -> 4.
    4 is a leaf, so the right boundary is [2].
    - The leaves from left to right are [3,4].
    Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].

    Example 2:

![](/images/leetcode-545-2.jpg)

    Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
    Output: [1,2,4,7,8,9,10,6,3]
    Explanation:
    - The left boundary follows the path starting from the root's left child 2 -> 4.
    4 is a leaf, so the left boundary is [2].
    - The right boundary follows the path starting from the root's right child 3 -> 6 -> 10.
    10 is a leaf, so the right boundary is [3,6], and in reverse order is [6,3].
    - The leaves from left to right are [4,7,8,9,10].
    Concatenating everything results in [1] + [2] + [4,7,8,9,10] + [6,3] = [1,2,4,7,8,9,10,6,3].

    Constraints:

        The number of nodes in the tree is in the range [1, 104].
        -1000 <= Node.val <= 1000

这个题其实很难，code 很tricky，记录一些 左右boundary 是true 还是 false 就好了。

# Code

```
class Solution {

    List<Integer> res = new LinkedList<Integer>();
    List<Integer> leaf = new LinkedList<Integer>();
    List<Integer> rightBoundary = new LinkedList<Integer>();
    
    public List<Integer> boundaryOfBinaryTree(TreeNode root) {
        res.add(root.val);
        helper(root.left, true, false);
        helper(root.right, false, true);
        res.addAll(leaf);
        res.addAll(rightBoundary);
        return res;
    }

    private void helper(TreeNode node, boolean isLeftBound, boolean isRightBound) {
        if (node == null) return;

        if (node.left == null && node.right == null) {
            // this is a leaf node
            leaf.add(node.val);
        } else {
            // either left or right boundary
            if (isLeftBound) res.add(node.val);
            if (isRightBound) rightBoundary.add(0, node.val);
             
            if (node.left == null || node.right == null) {
                // only have 1 child node
                helper(node.left, isLeftBound, isRightBound);
                helper(node.right, isLeftBound, isRightBound);
            } else {
                // have 2 child nodes: left and right
                if (isLeftBound) {
                    helper(node.left, isLeftBound, isRightBound);
                    helper(node.right, false, false);
                } else if (isRightBound) {
                    helper(node.left, false, false);
                    helper(node.right, isLeftBound, isRightBound);
                } else {
                    helper(node.left, false, false);
                    helper(node.right, false, false);
                }
            }
        }
    }
}
```
