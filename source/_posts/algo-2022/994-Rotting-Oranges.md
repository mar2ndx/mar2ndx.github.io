---
title: 994. Rotting Oranges
category: Leetcode
tags: []
comments: true
date: 2022-11-02 13:36
---



Link: https://leetcode.cn/problems/rotting-oranges/

# Question

difficulty: mid
adj diff: 3

    You are given an m x n grid where each cell can have one of three values:

		0 representing an empty cell,
		1 representing a fresh orange, or
		2 representing a rotten orange.

	Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

	Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

	 

	Example 1:

	Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
	Output: 4

	Example 2:

	Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
	Output: -1
	Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

	Example 3:

	Input: grid = [[0,2]]
	Output: 0
	Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

	 

	Constraints:

		m == grid.length
		n == grid[i].length
		1 <= m, n <= 10
		grid[i][j] is 0, 1, or 2.

老是写错,后来发现是 for (int i = queue.size(); i > 0; i--) 写成 for (int i = 0; i < queue.size(); i++) 了. 

怎么debug都发现不了, 哎...

# Code

```
class Solution {
    public int orangesRotting(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        List<int[]> queue = new LinkedList<int[]>();
        int totalFresh = 0;
        int minutesElapse = 0;

        // 1. find all rotten, count total fresh
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    queue.add(new int[]{i, j});
                } else if (grid[i][j] == 1) {
                    totalFresh++;
                }
            }
        }

        // start bfs using queue
        while (true) {
            int currentFresh = totalFresh;
            // try 4 directions
            for (int i = queue.size(); i > 0; i--) {
                int[] pos = queue.remove(0);
                currentFresh += traverse(grid, queue, pos[0] - 1, pos[1], m, n);
                currentFresh += traverse(grid, queue, pos[0] + 1, pos[1], m, n);
                currentFresh += traverse(grid, queue, pos[0], pos[1] + 1, m, n);
                currentFresh += traverse(grid, queue, pos[0], pos[1] - 1, m, n);
            }
            if (currentFresh == totalFresh) {
                // NO fresh oragne is rotten today, return
                break;
            }
            totalFresh = currentFresh;
            minutesElapse++;
        }
        return totalFresh == 0 ? minutesElapse : -1;
    }

    private int traverse(int[][] grid, List<int[]> queue, int x, int y, int m, int n) {
        // return value: how many fresh turn rotten
        if (x < 0 || x == m || y < 0 || y == n) {
            return 0;
        } else if (grid[x][y] == 1) {
            // a fresh orange turns rotten here. 
            queue.add(new int[]{x, y});
            grid[x][y] = 2;
            return -1;
        } else {
            return 0;
        }
    }
}
```
