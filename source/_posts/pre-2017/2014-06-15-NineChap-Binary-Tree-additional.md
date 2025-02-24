---
layout: post
title: "[NineChap 3.4] Binary Tree Additional"
comments: true
category: NineChap
---

These are some additional questions that are not covered in previous NineChap posts. Some questions are non-standard and difficult to solve, and some are not found in OJ websites. But these are real questions that has been asked during interviews.

## Question list

1. **[Binary Search Tree find upper/lower bound](/question/2014-06-15-BST-find-upper-lower-bound)**

1. **[Implement iterator of Binary Search Tree](/question/2014-06-14-Iterator-of-Tree)**

1. **[Binary Tree Serialize and Deserialize](/leetcode_plus/2014-06-16-Binary-tree-serialize-deserialize)**

1. **[Populating Next Right Pointers in Each Node](/leetcode/2014-05-27-Populating-Next-Right-Pointers-in-Each-Node)**

1. **[Populating Next Right Pointers in Each Node II](/leetcode/2014-05-27-Populating-Next-Right-Pointers-in-Each-Node-II)** - difficult

1. **[Symmetric Tree](/leetcode/2014-05-26-Symmetric-Tree)**

1. **[Same Tree](/leetcode/2014-05-25-Same-Tree)**

## Code

**Binary Search Tree find upper/lower bound**

Find the new post.

**Implement iterator of Binary Search Tree**

Find the new post.

**Binary Tree Serialize and Deserialize**

Find the new post.

**Populating Next Right Pointers in Each Node**

    public void connect(TreeLinkNode root) {
    	TreeLinkNode dummy = new TreeLinkNode(0);
    	dummy.left = root;
    	helper(dummy, root);
    }

    private void helper(TreeLinkNode parent, TreeLinkNode child) {
    	if (child == null) {
    		return;
    	}
    	if (child == parent.left) {
    		child.next = parent.right;
    	} else if (child == parent.right) {
    		if (parent.next != null) {
    			child.next = parent.next.left;
    		}
    	}
    	helper(child, child.left);
    	helper(child, child.right);
    }

**Populating Next Right Pointers in Each Node II**

This is a very tricky variant of DFS where the left sub-tree is making use of right sub-tree. I did not solve it even at second time.

    public void connect(TreeLinkNode root) {
        if (root == null) return;
        if (root.left == null && root.right == null) return;
        TreeLinkNode levelNext = root.next;
        TreeLinkNode lowerNext = null;
        while (levelNext != null && lowerNext == null) {
            if (levelNext.left != null) {
                lowerNext = levelNext.left;
                break;
            } else if (levelNext.right != null) {
                lowerNext = levelNext.right;
                break;
            } else {
                // if there is no child node of levelNext
                levelNext = levelNext.next;
            }
        }
        if (root.left == null) {
            root.right.next = lowerNext;
        } else if (root.right == null) {
            root.left.next = lowerNext;
        } else {
            root.left.next = root.right;
            root.right.next = lowerNext;
        }
        connect(root.right);
        connect(root.left);
    }

**Symmetric Tree**

    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
    		return true;
    	}
    	return mirror(root.left, root.right);
    }

    private boolean mirror(TreeNode left, TreeNode right) {
    	if (left == null && right == null) {
    		return true;
    	}
    	if (left == null || right == null) {
    		return false;
    	}
    	return (left.val == right.val)
    		& mirror(left.left, right.right)
    		& mirror(left.right, right.left);
    }

**Same Tree**

    public boolean isSameTree(TreeNode left, TreeNode right) {
    	if (left == null && right == null) {
    		return true;
    	}
    	if (left == null || right == null) {
    		return false;
    	}
    	return (left.val == right.val)
    		& isSameTree(left.left, right.left)
    		& isSameTree(left.right, right.right);
    }
