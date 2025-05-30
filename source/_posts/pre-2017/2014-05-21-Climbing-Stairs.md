---
title: "[LeetCode 70] Climbing Stairs"
category: Leetcode
tags: []
comments: true
date: 2014-05-21 00:00
---


### Question

[link](http://oj.leetcode.com/problems/climbing-stairs/)

<div class="question-content">
            <p></p><p>You are climbing a stair case. It takes <i>n</i> steps to reach to the top.</p>

<p>Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
</p><p></p>
          </div>

### Stats

<table border="2">
	<tr>
		<td>Frequency</td>
		<td bgcolor="red">5</td>
	</tr>
	<tr>
		<td>Difficulty</td>
		<td bgcolor="lime">2</td>
	</tr>
	<tr>
		<td>Adjusted Difficulty</td>
		<td bgcolor="white">1</td>
	</tr>
	<tr>
		<td>Time to use</td>
		<td bgcolor="lime">--------</td>
	</tr>
</table>

Ratings/Color = 1(white) 2(lime) 3(yellow) 4/5(red)

### Analysis

**This is an easy DP question**.

### Solution

My code is simple and concise, better than any other.

So I posted it below.

### My code

**Original code**

    public int climbStairs(int n) {
        if (n == 1) return 1;
        if (n == 2) return 2;
        int a = 1;
        int b = 2;
        int sum = 0;
        for (int i=3 ; i<=n ; i++){
            sum = a + b;
            a = b;
            b = sum;
        }
        return sum;
    }

**Optimized code**

    public int climbStairs(int n) {
        if (n == 1) return 1;
        int a = 1;
        int sum = 1;
        for (int i=2 ; i<=n ; i++){
            sum += a;
            a = sum - a;
        }
        return sum;
    }
