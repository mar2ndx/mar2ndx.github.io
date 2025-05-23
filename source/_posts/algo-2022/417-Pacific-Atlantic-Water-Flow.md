---
title: 417. Pacific Atlantic Water Flow
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link: https://leetcode.cn/problems/pacific-atlantic-water-flow/

# Question

difficulty: mid
adj diff: 4

    There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

    The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

    The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

    Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

    Example 1:

    Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
    [0,4]: [0,4] -> Pacific Ocean
    	   [0,4] -> Atlantic Ocean
    [1,3]: [1,3] -> [0,3] -> Pacific Ocean
    	   [1,3] -> [1,4] -> Atlantic Ocean
    [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
    	   [1,4] -> Atlantic Ocean
    [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
    	   [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
    [3,0]: [3,0] -> Pacific Ocean
    	   [3,0] -> [4,0] -> Atlantic Ocean
    [3,1]: [3,1] -> [3,0] -> Pacific Ocean
    	   [3,1] -> [4,1] -> Atlantic Ocean
    [4,0]: [4,0] -> Pacific Ocean
    	   [4,0] -> Atlantic Ocean
    Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

    Example 2:

    Input: heights = [[1]]
    Output: [[0,0]]
    Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

    Constraints:

    	m == heights.length
    	n == heights[r].length
    	1 <= m, n <= 200
    	0 <= heights[r][c] <= 105

标准的 dfs，比 bfs 代码要简洁一些。

用了两个 visited mask，最后 merge 成一个结果。很巧妙。

# Code

```
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length;
        int n = heights[0].length;
        boolean[][] pacific = new boolean[m][n];
        boolean[][] atlantic = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            dfs(pacific, m, n, heights, i, 0, 0); // first column
        }
        for (int i = 1; i < n; i++) {
            dfs(pacific, m, n, heights, 0, i, 0); // first row
        }
        for (int i = 0; i < m; i++) {
            dfs(atlantic, m, n, heights, i, n - 1, 0); // last column
        }
        for (int i = 0; i + 1 < n; i++) {
            dfs(atlantic, m, n, heights, m - 1, i, 0); // last row
        }

        List<List<Integer>> ans = new LinkedList<List<Integer>>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    List<Integer> coordinate = new LinkedList<Integer>();
                    coordinate.add(i);
                    coordinate.add(j);
                    ans.add(coordinate);
                }
            }
        }
        return ans;
    }

    private void dfs(boolean[][] ocean, int m, int n, int[][] heights, int x, int y, int lastAltitude) {
        if (x < 0 || x >= m || y < 0 || y >= n) {
            return;
        } else if (heights[x][y] < lastAltitude) {
            return;
        } else if (ocean[x][y] == true) {
            return;
        }
        ocean[x][y] = true;
        int newAltitude = heights[x][y];
        dfs(ocean, m, n, heights, x + 1, y, newAltitude);
        dfs(ocean, m, n, heights, x - 1, y, newAltitude);
        dfs(ocean, m, n, heights, x, y - 1, newAltitude);
        dfs(ocean, m, n, heights, x, y + 1, newAltitude);
    }
```
