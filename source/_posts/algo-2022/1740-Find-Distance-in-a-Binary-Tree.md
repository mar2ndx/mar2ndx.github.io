---
title: 1740. Find Distance in a Binary Tree
category: Leetcode
tags: []
comments: true
date: 2022-11-04 19:41
---


Link: https://leetcode.cn/problems/find-distance-in-a-binary-tree/

# Question

difficulty: mid
adj diff: 2

    Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p and value q in the tree.

    The distance between two nodes is the number of edges on the path from one to the other.

    

    Example 1:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0
    Output: 3
    Explanation: There are 3 edges between 5 and 0: 5-3-1-0.

    Example 2:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 7
    Output: 2
    Explanation: There are 2 edges between 5 and 7: 5-2-7.

    Example 3:

    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 5
    Output: 0
    Explanation: The distance between a node and itself is 0.

    

    Constraints:

        The number of nodes in the tree is in the range [1, 104].
        0 <= Node.val <= 109
        All Node.val are unique.
        p and q are values in the tree.

应该不难。LCA变体。

# Code

代码来自于：https://leetcode.cn/problems/find-distance-in-a-binary-tree/solution/bi-ren-he-ren-du-hao-de-jie-ti-by-java08-dusc/

```
class Solution {
    public int findDistance(TreeNode root, int p, int q) {
        if(p == q){
            return 0;
        }
        // 公共祖先
        TreeNode parent = findCommonParent(root,p,q);
        // 节点到公共祖先的距离
        return getNodeDepth(parent,p) + getNodeDepth(parent,q);
    }

    // 首先寻找公共祖先
    private TreeNode findCommonParent(TreeNode root, int p, int q){
        if(root == null){
            return null;
        }
        if(root.val == p || root.val == q){
            return root;
        }
        TreeNode left = findCommonParent(root.left,p,q);
        TreeNode right = findCommonParent(root.right,p,q);
        if(left != null && right != null){
            return root;
        }
        return left == null ? right : left;
    }

    // 到root节点的距离
    private int getNodeDepth(TreeNode root,int p){
        if(root == null){
            // -1表示当前路径不是p的路径
            return -1;
        }
        if(root.val == p){
            return 0;
        }
        int left = getNodeDepth(root.left,p);
        int right = getNodeDepth(root.right,p);
        int ans = Math.max(left,right);
        // 最大值是-1的话，表示不是p的路径，>= 0则表示找到的p的路径，再加上自己本身的距离
        return ans >= 0 ? ans + 1 : -1;
    }

}
```
