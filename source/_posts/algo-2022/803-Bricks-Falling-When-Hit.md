---
title: 803. Bricks Falling When Hit
category: Leetcode
tags: []
comments: true
date: 2022-11-14 13:27
---



Link: https://leetcode.cn/problems/all-paths-from-source-to-target/

# Question

difficulty: mid
adj diff: 3

    You are given an m x n binary grid, where each 1 represents a brick and 0 represents an empty space. A brick is stable if:

    It is directly connected to the top of the grid, or
    At least one other brick in its four adjacent cells is stable.
    You are also given an array hits, which is a sequence of erasures we want to apply. Each time we want to erase the brick at the location hits[i] = (rowi, coli). The brick on that location (if it exists) will disappear. Some other bricks may no longer be stable because of that erasure and will fall. Once a brick falls, it is immediately erased from the grid (i.e., it does not land on other stable bricks).

    Return an array result, where each result[i] is the number of bricks that will fall after the ith erasure is applied.

    Note that an erasure may refer to a location with no brick, and if it does, no bricks drop.

     

    Example 1:

    Input: grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
    Output: [2]
    Explanation: Starting with the grid:
    [[1,0,0,0],
    [1,1,1,0]]
    We erase the underlined brick at (1,0), resulting in the grid:
    [[1,0,0,0],
    [0,1,1,0]]
    The two underlined bricks are no longer stable as they are no longer connected to the top nor adjacent to another stable brick, so they will fall. The resulting grid is:
    [[1,0,0,0],
    [0,0,0,0]]
    Hence the result is [2].
    Example 2:

    Input: grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
    Output: [0,0]
    Explanation: Starting with the grid:
    [[1,0,0,0],
    [1,1,0,0]]
    We erase the underlined brick at (1,1), resulting in the grid:
    [[1,0,0,0],
    [1,0,0,0]]
    All remaining bricks are still stable, so no bricks fall. The grid remains the same:
    [[1,0,0,0],
    [1,0,0,0]]
    Next, we erase the underlined brick at (1,0), resulting in the grid:
    [[1,0,0,0],
    [0,0,0,0]]
    Once again, all remaining bricks are still stable, so no bricks fall.
    Hence the result is [0,0].
     

    Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    grid[i][j] is 0 or 1.
    1 <= hits.length <= 4 * 104
    hits[i].length == 2
    0 <= xi <= m - 1
    0 <= yi <= n - 1
    All (xi, yi) are unique.

这道题**只能用** union find 并查集来做。

我不会。

So，我写了一个 BFS 搜素方法，代码除了 exceed run time，逻辑完全是 work 的。

# Code

每敲一次，就 bfs 搜索一次。(exceed timing)

```
class Solution {

    int[][] fourDirections = {
        {1, 0},
        {0, 1},
        {-1, 0},
        {0, -1}
    };

    public int[] hitBricks(int[][] grid, int[][] hits) {
        int m = grid.length;
        int n = grid[0].length;
        int w = hits.length;
        int[] ans = new int[w];

        // hit the grid 'w' times
        int preVal = 1;
        for (int i = 0; i < w; i++) {
            // Step 1. hit it!
            if (grid[hits[i][0]][hits[i][1]] == preVal) {
                grid[hits[i][0]][hits[i][1]] = 0;
            }
            // Step 2. do BFS with the entire grid
            int postVal = -1 - i;
            bfsMark(grid, preVal, postVal);
            preVal = postVal;
        }

        // Step 3. count the postVal and return answer
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    ans[0]++;
                } else if (grid[i][j] < 0) {
                    int p = 0 - grid[i][j];
                    if (p < w) ans[p]++;
                }
            }
        }
        return ans;
    }

    private void bfsMark(int[][] grid, int preVal, int postVal) {
        // from the top row, do bfs and mark all preVal to postVal
        List<int[]> queue = new LinkedList<int[]>();

        // Step 1. add top row coordinates
        for (int i = 0; i < grid[0].length; i++) {
            if (grid[0][i] == preVal) {
                grid[0][i] = postVal;
                queue.add( new int[]{0, i} );
            }
        }

        // Step 2. flood the adjacent coordinates
        while (!queue.isEmpty()) {
            int[] pos = queue.remove(0);
            for (int i = 0; i < 4; i++) {
                if (bfsHelper(grid, pos[0] + fourDirections[i][0], pos[1] + fourDirections[i][1], preVal, postVal)) {
                    queue.add( new int[]{pos[0] + fourDirections[i][0], pos[1] + fourDirections[i][1]} );
                }
            }
        }
    }

    private boolean bfsHelper(int[][] grid, int x, int y, int preVal, int postVal) {
        if (0 <= x && x < grid.length && y >= 0 && y < grid[0].length) {
            if (grid[x][y] == preVal) {
                grid[x][y] = postVal;
                return true;
            }
        }
        return false;
    }
}
```
