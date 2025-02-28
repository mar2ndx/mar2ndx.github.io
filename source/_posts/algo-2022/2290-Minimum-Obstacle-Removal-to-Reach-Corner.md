---
title: 2290. Minimum Obstacle Removal to Reach Corner
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link: https://leetcode.cn/problems/minimum-obstacle-removal-to-reach-corner/

# Question

difficulty: hard
adj diff: 4

    You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

    	0 represents an empty cell,
    	1 represents an obstacle that may be removed.

    You can move up, down, left, or right from and to an empty cell.

    Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).
    Example 1:

    Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
    Output: 2
    Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
    It can be shown that we need to remove at least 2 obstacles, so we return 2.
    Note that there may be other ways to remove 2 obstacles to create a path.

    Example 2:

    Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
    Output: 0
    Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.
    Constraints:

    	m == grid.length
    	n == grid[i].length
    	1 <= m, n <= 105
    	2 <= m * n <= 105
    	grid[i][j] is either 0 or 1.
    	grid[0][0] == grid[m - 1][n - 1] == 0

这道题没有想象的那么难：就是基础的 bfs。

只不过，涉及到一个路线长短的问题。也就是：

1. 不遇到障碍物（即 grid[i][j] == 0 情况），则路线长度为 0；
1. 如遇到了障碍（即 grid[i][j] == 1 情况），则路线长度为 1；
1. BFS + 算出最短长度。

# Code

代码是我参考的：

```
    public int minimumObstacles(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        // int[][] dist is the visited map + distance from [0, 0]
        int[][] dist = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // first, all distances are very very far
                if (i + j == 0) dist[i][j] = 0;
                else dist[i][j] = Integer.MAX_VALUE;
            }
        }

        // start BFS
        List<int[]> q = new LinkedList<int[]>();
        q.add(new int[]{0, 0});
        while (!q.isEmpty()) {
            int[] pos = q.remove(0);
            int x = pos[0];
            int y = pos[1];
            for (int[] ttt: dirs) {
                int nextX = x + ttt[0];
                int nextY = y + ttt[1];

                // 从dist[x][y]走到dist[nextX][nextY]，需要跨过grid[nextX][nextY]
                if (nextX < 0 || nextX >= m || nextY < 0 || nextY >= n) {
                    continue;
                } else {
    				// [nextX][nextY] is a valid position,
                    // Now I need to update distance[nextX][nextY]
    				int stepDistance = dist[x][y] + grid[nextX][nextY];
                    if (stepDistance < dist[nextX][nextY]) {
                        dist[nextX][nextY] = stepDistance;
                        q.add(new int[]{nextX, nextY});
                    }
                }
            }
        }
        return dist[m - 1][n - 1];
    }
```
