---
title: 210. Course Schedule II
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---


Link: https://leetcode.cn/problems/course-schedule-ii/

这道题跟 [269. Alien Dictionary](https://leetcode.cn/problems/alien-dictionary/) 基本一样。

# Question

difficulty: mid
adj diff: 5

    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    	For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

    Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

    Example 1:

    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: [0,1]
    Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

    Example 2:

    Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,2,1,3]
    Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
    So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

    Example 3:

    Input: numCourses = 1, prerequisites = []
    Output: [0]
    Constraints:

    	1 <= numCourses <= 2000
    	0 <= prerequisites.length <= numCourses * (numCourses - 1)
    	prerequisites[i].length == 2
    	0 <= ai, bi < numCourses
    	ai != bi
    	All the pairs [ai, bi] are distinct.

经典的「拓扑排序」问题。

# Code

代码是我参考的。

```
    class Solution {
    	// 这个代码不是我写的。
    	public int[] findOrder(int numCourses, int[][] prerequisites) {
    		if (numCourses <= 0) {
    			return new int[0];
    		}

    		HashSet<Integer>[] adj = new HashSet[numCourses];
    		for (int i = 0; i < numCourses; i++) {
    			adj[i] = new HashSet<>();
    		}

    		// [1,0] 0 -> 1
    		int[] inDegree = new int[numCourses];
    		for (int[] p : prerequisites) {
    			adj[p[1]].add(p[0]);
    			inDegree[p[0]]++;
    		}

    		Queue<Integer> queue = new LinkedList<>();
    		for (int i = 0; i < numCourses; i++) {
    			if (inDegree[i] == 0) {
    				queue.offer(i);
    			}
    		}

    		int[] res = new int[numCourses];
    		// 当前结果集列表里的元素个数，正好可以作为下标
    		int count = 0;

    		while (!queue.isEmpty()) {
    			// 当前入度为 0 的结点
    			Integer head = queue.poll();
    			res[count] = head;
    			count++;

    			Set<Integer> successors = adj[head];
    			for (Integer nextCourse : successors) {
    				inDegree[nextCourse]--;
    				// 马上检测该结点的入度是否为 0，如果为 0，马上加入队列
    				if (inDegree[nextCourse] == 0) {
    					queue.offer(nextCourse);
    				}
    			}
    		}

    		// 如果结果集中的数量不等于结点的数量，就不能完成课程任务，这一点是拓扑排序的结论
    		if (count == numCourses) {
    			return res;
    		}
    		return new int[0];
    	}
    }
```
