---
title: 1254. Number of Closed Islands
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link: https://leetcode.cn/problems/number-of-closed-islands/

# Question

difficulty: mid
adj diff: 4

    Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

    Return the number of closed islands.

    Example 1:

    Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
    Output: 2
    Explanation:
    Islands in gray are closed because they are completely surrounded by water (group of 1s).

    Example 2:

    Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
    Output: 1

    Example 3:

    Input: grid = [[1,1,1,1,1,1,1],
    			   [1,0,0,0,0,0,1],
    			   [1,0,1,1,1,0,1],
    			   [1,0,1,0,1,0,1],
    			   [1,0,1,1,1,0,1],
    			   [1,0,0,0,0,0,1],
    			   [1,1,1,1,1,1,1]]
    Output: 2

    Constraints:

    	1 <= grid.length, grid[0].length <= 100
    	0 <= grid[i][j] <=1

代码有点长，有点复杂。

好在逻辑简单。单纯的 bfs。

# Code

```
    List<int[]> list = new LinkedList<int[]>();

    public int closedIsland(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int islands = 0;

        // first, mark all border to '1's
        for (int i = 0; i < m; i++) {
            addToQueue(grid, m, n, i, 0);
            addToQueue(grid, m, n, i, n - 1);
        }
        for (int j = 1; j + 1 < n; j++) {
            addToQueue(grid, m, n, 0, j);
            addToQueue(grid, m, n, m - 1, j);
        }
        startDfs(grid, m, n);

        // start to find islands
        for (int i = 1; i + 1 < m; i++) {
            for (int j = 1; j + 1 < n; j++) {
                if (grid[i][j] == 1) {
                    continue;
                }
                // found an '0', which means a valid island
                addToQueue(grid, m, n, i, j);
                islands++;
                startDfs(grid, m, n);
            }
        }

        return islands;
    }

    private void startDfs(int[][] grid, int m, int n) {
        while (!list.isEmpty()) {
            int[] cur = list.remove(0);
            addToQueue(grid, m, n, cur[0] - 1, cur[1]);
            addToQueue(grid, m, n, cur[0] + 1, cur[1]);
            addToQueue(grid, m, n, cur[0], cur[1] - 1);
            addToQueue(grid, m, n, cur[0], cur[1] + 1);
        }
    }

    private void addToQueue(int[][] grid, int m, int n, int x, int y) {
        if (0 <= x && x < m && 0 <= y && y < n && grid[x][y] == 0) {
            list.add(new int[]{x, y});
            grid[x][y] = 1;
        }
    }
```
