---
title: 339. Nested List Weight Sum
category: Leetcode
tags: []
comments: true
date: 2022-11-18 07:07
---



Link: https://leetcode.cn/problems/nested-list-weight-sum/

# Question

difficulty: mid
adj diff: 3

	You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

	The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

	Return the sum of each integer in nestedList multiplied by its depth.

	Example 1:

	Input: nestedList = [[1,1],2,[1,1]]
	Output: 10
	Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.

	Example 2:

	Input: nestedList = [1,[4,[6]]]
	Output: 27
	Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.

	Example 3:

	Input: nestedList = [0]
	Output: 0

	 

	Constraints:

		1 <= nestedList.length <= 50
		The values of the integers in the nested list is in the range [-100, 100].
		The maximum depth of any integer is less than or equal to 50.

主要难点在于 理解题意。

# Code

这是来自[官方的代码](https://leetcode.cn/problems/nested-list-weight-sum/solution/qian-tao-lie-biao-quan-zhong-he-by-leetcode-2/)


```
public int depthSum(List<NestedInteger> nestedList) {
    return depthSum(nestedList, 1);
}

public int depthSum(List<NestedInteger> list, int depth) {
    int sum = 0;
    for (NestedInteger n : list) {
        if (n.isInteger()) {
            sum += n.getInteger() * depth;
        } else {
            sum += depthSum(n.getList(), depth + 1);
        }
    }
    return sum;
}
```
