---
title: 652. Find Duplicate Subtrees
category: Leetcode
tags: []
comments: true
date: 2022-10-29 19:34
---


Link: https://leetcode.cn/problems/find-duplicate-subtrees/

# Question

difficulty: mid
adj diff: 4

    Given the root of a binary tree, return all duplicate subtrees.

    For each kind of duplicate subtrees, you only need to return the root node of any one of them.

    Two trees are duplicate if they have the same structure with the same node values.

    Example 1:

    Input: root = [1,2,3,4,null,2,4,null,null,4]
    Output: [[2,4],[4]]

    Example 2:

    Input: root = [2,1,1]
    Output: [[1]]

    Example 3:

    Input: root = [2,2,2,3,null,3,null]
    Output: [[2,3],[3]]

    Constraints:

    	The number of the nodes in the tree will be in the range [1, 5000]
    	-200 <= Node.val <= 200

# Code

```
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        Set<TreeNode> ans = new HashSet<TreeNode>(); // to avoid duplicated
        Map<String, TreeNode> memory = new HashMap<String, TreeNode>();
        helper(ans, root, memory);
        return new LinkedList<TreeNode>(ans); // construct a new list for return
    }

    private String helper(Set<TreeNode> ans, TreeNode node, Map<String, TreeNode> memory) {
        if (node == null) {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        sb.append("(");
        sb.append(helper(ans, node.left, memory));
        sb.append(")");
        sb.append(node.val);
        sb.append("(");
        sb.append(helper(ans, node.right, memory));
        sb.append(")");
        String serializedTree = sb.toString();
        if (memory.containsKey(serializedTree)) {
            ans.add(memory.get(serializedTree));
        } else {
            memory.put(serializedTree, node);
        }
        return serializedTree;
    }
```
