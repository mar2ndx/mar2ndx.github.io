---
title: "[NineChap 3.1] Binary Tree DFS and Divide Conquer"
category: NineChap
tags: []
comments: true
date: 2014-06-10 00:00
---


## DFS

#### Recursion or While-Loop?

We can use recursion, because unless it's pre-order traverse, binary tree questions can be difficult.

Solving the problem is more important.

#### Divide & Conquer Algorithm

1. Merge Sort
2. Quick Sort
3. Most of Binary tree questions

#### Solution modal

Generally, D&C questions would do 2 things at same time:

1. Divide - For binary tree, it mean solve left child, and solve right child
2. Conquer - return result value

A very common type would be validating the left/right children and return -1 if the validation failed. Otherwise, a result value is returned. In this way, by checking the positive/negative sign, we know whether this node is valid, and if valid, we know the returned value.

This idea is extensivelly used among all binary tree questions. See "Lowest Common Ancestor (LCA)" for more details.

#### Template

**Divide & Conquer**, [link](http://answer.ninechapter.com/solutions/dfs-template/)

    public class Solution {
        public ResultType traversal(TreeNode root) {
            // null or leaf
            if (root == null) {
                // do something and return;
            }

            // Divide
            ResultType left = traversal(root.left);
            ResultType right = traversal(root.right);

            // Conquer
            ResultType result = Merge from left and right.
            return result;
        }
    }

## Question list

**Traversal**

1. **[Binary Tree Preorder Traversal](/leetcode/2014-06-02-Binary-Tree-Preorder-Traversal)**

1. **[Binary Tree Inorder Traversal](/leetcode/2014-05-24-Binary-Tree-Inorder-Traversal)**

1. **[Binary Tree Postorder Traversal](/leetcode/2014-06-03-Binary-Tree-Postorder-Traversal)**

**Divide & Conquer**

1. **[Maximum Depth of Binary Tree](/leetcode/2014-05-25-Maximum-Depth-of-Binary-Tree)**

1. **[Minimum Depth of Binary Tree](/leetcode/2014-05-25-Minimum-Depth-of-Binary-Tree)**

1. **[Balanced Binary Tree](/leetcode/2014-05-26-Balanced-Binary-Tree)**

1. **[Binary Tree Maximum Path Sum](/leetcode/2014-05-28-Binary-Tree-Maximum-Path-Sum)** - the most important question for this category

#### Additional

1. **Lowest Common Ancestor Problem**

   [problem one](/leetcode_plus/2014-06-10-Lowest-Common-Ancestor-BST)

   [problem two](/leetcode_plus/2014-06-10-Lowest-Common-Ancestor-Tree)

   [problem three](/leetcode_plus/2014-06-10-Lowest-Common-Ancestor-Tree-II)

## Code

**Binary Tree Preorder Traversal**

    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> ans = new LinkedList<Integer>();
        if (root == null) return ans;
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode cur = stack.pop();
            ans.add(cur.val);
            if (cur.right != null) {
                stack.push(cur.right);
            }
            if (cur.left != null) {
                stack.push(cur.left);
            }
        }
        return ans;
    }

There is a not-recommended but good-to-know solution of Divide & Conquer (not written by me)

    public class Solution {
        public ArrayList<Integer> preorderTraversal(TreeNode root) {
            ArrayList<Integer> result = new ArrayList<Integer>();
            // null or leaf
            if (root == null) {
                return result;
            }

            // Divide
            ArrayList<Integer> left = preorderTraversal(root.left);
            ArrayList<Integer> right = preorderTraversal(root.right);

            // Conquer
            result.add(root.val);
            result.addAll(left);
            result.addAll(right);
            return result;
        }
    }

**Binary Tree Inorder Traversal**

Keep traversing left until a NULL is found. When it happens, pop one and traverse right once. **Remember this solution**!

    public ArrayList<Integer> inorderTraversal(TreeNode root) {
        ArrayList<Integer> ans = new ArrayList<Integer>();
    	if (root == null) {
    		return ans;
    	}
    	Stack<TreeNode> stack = new Stack<TreeNode>();
    	TreeNode p = root;
    	while (p != null || !stack.isEmpty()) {
    		if (p != null) {
    			stack.push(p);
    			p = p.left;
    		}
    		else {
    			p = stack.pop();
    			ans.add(p.val);
    			p = p.right;
    		}
    	}
    	return ans;
    }

**Binary Tree Postorder Traversal**

I failed to write the code even after reading the solution. I need to memorize this solution by heart.

    public List<Integer> postorderTraversal(TreeNode root) {
    	List<Integer> ans = new ArrayList<Integer>();
    	if (root == null) {
    		return ans;
    	}
    	Stack<TreeNode> stack = new Stack<TreeNode>();
    	stack.push(root);
    	TreeNode pre = null;
    	TreeNode cur = null;
    	while (!stack.isEmpty()) {
    		cur = stack.peek();
    		if (pre == null || pre.left == cur || pre.right == cur) {
    			if (cur.left != null) {
    				stack.push(cur.left);
    			} else if (cur.right != null) {
    				stack.push(cur.right);
    			}
    		} else if (cur.left == pre) {
    			if (cur.right != null) {
    				stack.push(cur.right);
    			}
    		} else if (cur.right == pre || cur == pre) {
    			// note that 'pre' and 'cur' are never going to be apart
    			// for more then 1 edge (they can overlap)
    			ans.add(stack.pop().val);
    		}
    		pre = cur;
    	}
    	return ans;
    }

**Maximum Depth of Binary Tree**

    // 1 minute
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }

**Minimum Depth of Binary Tree**

    public int minDepth(TreeNode root) {
        if (root == null) {
    		return 0;
    	}
    	return checkLeaf(root);
    }

    private int checkLeaf(TreeNode node) {
    	if (node.left == null && node.right == null) {
    		return 1;
    	}
    	int ll = Integer.MAX_VALUE;
    	int rr = Integer.MAX_VALUE;
    	if (node.left != null) ll = checkLeaf(node.left);
    	if (node.right != null) rr = checkLeaf(node.right);
    	return 1 + Math.min(ll, rr);
    }

After checking [the answer](http://answer.ninechapter.com/solutions/minimum-depth-of-binary-tree/), the code above can be optimized:

    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return getMin(root);
    }

    public int getMin(TreeNode root){
        if (root == null) {
            return Integer.MAX_VALUE; // important
        }

        if (root.left == null && root.right == null) {
            return 1;
        }

        return Math.min(getMin(root.left), getMin(root.right)) + 1;
    }

**Balanced Binary Tree**

    // 4 minutes
    public boolean isBalanced(TreeNode root) {
        return getDepth(root) != -1;
    }

    private int getDepth(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int ll = getDepth(node.left);
        int rr = getDepth(node.right);
        if (ll == -1 || rr == -1 || Math.abs(ll - rr) > 1) {
            return -1;
        }
        return 1 + Math.max(ll, rr);
    }

**Binary Tree Maximum Path Sum**

Although the following code works:

    int max = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        maxDepth(root);
    	return max;
    }

    private int maxDepth(TreeNode node) {
    	if (node == null) {
    		return 0;
    	}
    	int ll = maxDepth(node.left);
    	int rr = maxDepth(node.right);
    	int currentMaxPath = ll + rr + node.val;
    	max = Math.max(max, currentMaxPath);
    	return Math.max(0, node.val + Math.max(ll, rr));
    }

Mr. Huang said it's AN EXTREMELY BAD IDEA TO USE GLOBAL VARIABLE in Java. It's just terrible. Don't do it.

According to Mr. Huang's [suggestion](http://answer.ninechapter.com/solutions/binary-tree-maximum-path-sum/), I added another class called "ResultType". This can help me return 2 values at 1 single traversal.

Code is below. One 'catch-ya' is when NULL is found, the maxPath should return Integer.MIN_VALUE instead of 0.

This code is much easier for both me and anyone else to understand, so **stick to this solution, and never use global variable in Java**!

    private class ResultType {
        int singlePath, maxPath;
        ResultType(int singlePath, int maxPath) {
            this.singlePath = singlePath;
            this.maxPath = maxPath;
        }
    }

    public int maxPathSum(TreeNode root) {
        ResultType result = helper(root);
        return result.maxPath;
    }

    private ResultType helper(TreeNode node) {
        // null case
        if (node == null) {
            return new ResultType(0, Integer.MIN_VALUE);
        }
        // divide
        ResultType ll = helper(node.left);
        ResultType rr = helper(node.right);
        // conquer
        int curSinglePath = Math.max(0, node.val +
                Math.max(ll.singlePath, rr.singlePath));
        int childMaxPath = Math.max(ll.maxPath, rr.maxPath);
        int curMaxPath = Math.max(childMaxPath, node.val +
                ll.singlePath + rr.singlePath);
        // done
        return new ResultType(curSinglePath, curMaxPath);
    }

**Lowest Common Ancestor** - I wrote three new posts on this topic:

Problem 1: BST: top-down O(height) solution

Problem 2: Binary Tree: bottom-up O(n) solution

Problem 3: Binary Tree with a link to parent
