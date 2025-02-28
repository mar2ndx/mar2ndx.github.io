---
title: 250. Count Univalue Subtrees
category: Leetcode
tags: []
comments: true
date: 2022-11-04 18:25
---



Link: https://leetcode.cn/problems/count-univalue-subtrees/

# Question

    difficulty: mid
    adj diff: 3

    Given the root of a binary tree, return the number of uni-value subtrees.

    A uni-value subtree means all nodes of the subtree have the same value.

    

    Example 1:

    Input: root = [5,1,5,5,5,null,5]
    Output: 4

    Example 2:

    Input: root = []
    Output: 0

    Example 3:

    Input: root = [5,5,5,5,5,null,5]
    Output: 6

    

    Constraints:

        The number of the node in the tree will be in the range [0, 1000].
        -1000 <= Node.val <= 1000

标准 tree 的 dfs()。

我的代码不是很巧妙，因为 return value 搞出来了 2种特殊情况。

下面的更新版代码更好。

# Code

```
class Solution {

    Map<Integer, Integer> map = new HashMap<Integer, Integer>();
    int total = 0;

    public int countUnivalSubtrees(TreeNode root) {
        if (root != null) {
            dfs(root);
        }
        return total;
    }

    private int dfs(TreeNode node) {
        if (node == null) return -10000;
        int leftVal = dfs(node.left);
        int rightVal = dfs(node.right);

        if (leftVal + rightVal == -20000) {
            total++;
            map.put(node.val, map.getOrDefault(node.val, 0) + 1);
            return node.val;
        } else if (rightVal == -10000 && node.val == leftVal) {
            total++;
            map.put(node.val, map.getOrDefault(node.val, 0) + 1);
            return node.val;
        } else if (leftVal == -10000 && node.val == rightVal) {
            total++;
            map.put(node.val, map.getOrDefault(node.val, 0) + 1);
            return node.val;
        } else if (node.val == leftVal && node.val == rightVal) {
            total++;
            map.put(node.val, map.getOrDefault(node.val, 0) + 1);
            return node.val;
        }
        return 10000;
    }
}
```

可以 simply 成如下短代码。

（相当于把 return value 当作 parameter 传到下一级 dfs function）

```
class Solution {
    
    int total = 0;

    public int countUnivalSubtrees(TreeNode root) {
        dfs(root, 0);
        return total;
    }

    private boolean dfs(TreeNode node, int val) {
        if (node == null) return true;

        boolean leftCheck = dfs(node.left, node.val);
        boolean rightCheck = dfs(node.right, node.val);
        if (leftCheck && rightCheck) {
            total++;
        } else {
            return false;
        }
        // [IMPORTANT] Can't simply say: 
        // if (!dfs(node.left, node.val) || !dfs(node.right, node.val)) return false;
        // beceause if (left consider) is checked, (right consider) won't check

        return node.val == val;
    }
}
```
