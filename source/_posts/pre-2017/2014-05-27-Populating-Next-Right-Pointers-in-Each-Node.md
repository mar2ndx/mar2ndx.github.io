---
title: "[LeetCode 116] Populating Next Right Pointers in Each Node"
category: Leetcode
tags: []
comments: true
date: 2014-05-27 00:00
---


### Question

[link](https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/)

<div class="question-content">
            <p></p><p>
Given a binary tree
</p><pre>    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
</pre>
<p></p>

<p>Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to <code>NULL</code>.</p>

<p>Initially, all next pointers are set to <code>NULL</code>.</p>

<p>
<b>Note:</b>
</p><ul>
<li>You may only use constant extra space.</li>
<li>You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).</li>
</ul>
<p></p>

<p>
For example,<br>
Given the following perfect binary tree,<br>
</p><pre>         1
       /  \
      2    3
     / \  / \
    4  5  6  7
</pre>
<p></p>
<p>
After calling your function, the tree should look like:<br>
</p><pre>         1 -&gt; NULL
       /  \
      2 -&gt; 3 -&gt; NULL
     / \  / \
    4-&gt;5-&gt;6-&gt;7 -&gt; NULL
</pre>
<p></p><p></p>
          </div>

### Stats

<table border="2">
	<tr>
		<td>Frequency</td>
		<td bgcolor="yellow">3</td>
	</tr>
	<tr>
		<td>Difficulty</td>
		<td bgcolor="yellow">3</td>
	</tr>
	<tr>
		<td>Adjusted Difficulty</td>
		<td bgcolor="lime">2</td>
	</tr>
	<tr>
		<td>Time to use</td>
		<td bgcolor="yellow">--------</td>
	</tr>
</table>

Ratings/Color = 1(white) 2(lime) 3(yellow) 4/5(red)

### Analysis

**Although this question is not hard, it needs a bit thinking**.

The important point is, how to effectively make use of the 'next link' generated before, to help us solve this problem.

### Solution

**My solution is actually very good**. It pass current node and next node into a method, and then generate links for current node's children.

**There is a even [better solution](http://leetcode.com/2010/03/first-on-site-technical-interview.html)**, which directly make use of the 'next link' generated already. In fact, it's same as my solution, except it uses one less variable. Great idea it is!

### Code

**First, my solution**

    public void connect(TreeLinkNode root) {
        link(root, null);
    }

    private void link(TreeLinkNode node, TreeLinkNode rr){
        if (node == null || node.left == null) return;
        node.left.next = node.right;
        if (rr == null) node.right.next = null;
        else node.right.next = rr.left;

        link(node.left, node.left.next);
        link(node.right, node.right.next);
    }

**Second, better solution**

    public void connect(TreeLinkNode root) {
    	if (root == null || root.left == null || root.right == null)
    	    return;
    	root.left.next = root.right;
    	root.right.next = root.next == null ? null : root.next.left;
    	connect(root.left);
    	connect(root.right);
    }
