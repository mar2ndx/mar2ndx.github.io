---
title: 695. Max Area of Island
category: Leetcode
tags: []
comments: true
date: 2022-11-15 00:40
---



Link: https://leetcode.cn/problems/max-area-of-island/

# Question

difficulty: mid
adj diff: 2

	You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

	The area of an island is the number of cells with a value 1 in the island.

	Return the maximum area of an island in grid. If there is no island, return 0.

	 

	Example 1:

	Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
	Output: 6
	Explanation: The answer is not 11, because the island must be connected 4-directionally.

	Example 2:

	Input: grid = [[0,0,0,0,0,0,0,0]]
	Output: 0

	 

	Constraints:

		m == grid.length
		n == grid[i].length
		1 <= m, n <= 50
		grid[i][j] is either 0 or 1.

纯粹代码题。

# Code

[代码来自这里](https://leetcode.cn/problems/max-area-of-island/solution/dao-yu-de-zui-da-mian-ji-by-leetcode-solution/)

```
class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int ans = 0;
        for (int i = 0; i != grid.length; ++i) {
            for (int j = 0; j != grid[0].length; ++j) {
                ans = Math.max(ans, dfs(grid, i, j));
            }
        }
        return ans;
    }

    public int dfs(int[][] grid, int cur_i, int cur_j) {
        if (cur_i < 0 || cur_j < 0 || cur_i == grid.length || cur_j == grid[0].length || grid[cur_i][cur_j] != 1) {
            return 0;
        }
        grid[cur_i][cur_j] = 0;
        int[] di = {0, 0, 1, -1};
        int[] dj = {1, -1, 0, 0};
        int ans = 1;
        for (int index = 0; index != 4; ++index) {
            int next_i = cur_i + di[index], next_j = cur_j + dj[index];
            ans += dfs(grid, next_i, next_j);
        }
        return ans;
    }
}
```
