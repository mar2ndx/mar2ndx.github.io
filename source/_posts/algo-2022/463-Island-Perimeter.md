---
title: 463. Island Perimeter
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link: https://leetcode.cn/problems/island-perimeter/

# Question

difficulty: easy
adj diff: 3

    You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

    Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

    The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

    Example 1:

    Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    Output: 16
    Explanation: The perimeter is the 16 yellow stripes in the image above.

    Example 2:

    Input: grid = [[1]]
    Output: 4

    Example 3:

    Input: grid = [[1,0]]
    Output: 4

    Constraints:

    	row == grid.length
    	col == grid[i].length
    	1 <= row, col <= 100
    	grid[i][j] is 0 or 1.
    	There is exactly one island in grid.

比较 tricky，但是代码很简单。

基本思路：碰壁了之后，就 +1，否则继续 dfs。

# Code

```
    public int islandPerimeter(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    return dfs(grid, m, n, i, j);
                }
            }
        }
        // did not find any '1's, no Perimeter
        return 0;
    }

    private int dfs(int[][] grid, int m, int n, int x, int y) {
        if (x < 0 | x == m || y < 0 || y == n) {
            return 1; // board edge
        } else if (grid[x][y] == 0) {
            return 1; // internal edge
        } else if (grid[x][y] == 99) {
            return 0; // visited already
        }
        // mark the position (x, y) from 1 to 99 (means visited)
        grid[x][y] = 99;
        return dfs(grid, m, n, x + 1, y)
            + dfs(grid, m, n, x - 1, y)
            + dfs(grid, m, n, x, y + 1)
            + dfs(grid, m, n, x, y - 1);
    }
```
