---
title: "[LeetCode 54] Spiral Matrix"
category: Leetcode
tags: []
comments: true
date: 2014-05-16 00:00
---


### Question

[link](http://oj.leetcode.com/problems/spiral-matrix/)

<div class="question-content">
            <p></p><p>Given a matrix of <i>m</i> x <i>n</i> elements (<i>m</i> rows, <i>n</i> columns), return all elements of the matrix in spiral order.
</p>

<p>
For example,<br>
Given the following matrix:
</p>
<pre>[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
</pre>
<p>
You should return <code>[1,2,3,6,9,8,7,4,5]</code>.
</p><p></p>
          </div>

### Stats

<table border="2">
	<tr>
		<td>Frequency</td>
		<td bgcolor="lime">2</td>
	</tr>
	<tr>
		<td>Difficulty</td>
		<td bgcolor="red">4</td>
	</tr>
	<tr>
		<td>Adjusted Difficulty</td>
		<td bgcolor="yellow">3</td>
	</tr>
	<tr>
		<td>Time to use</td>
		<td bgcolor="yellow">----------</td>
	</tr>
</table>

Ratings/Color = 1(white) 2(lime) 3(yellow) 4/5(red)

### Analysis

**This question is basic mathematics**. The difficulty is the coding part.

### My code

    public class Solution {
        public List<Integer> spiralOrder(int[][] matrix) {
    		List<Integer> ans = new ArrayList<Integer>();
    		if (matrix == null || matrix.length == 0
    			|| matrix[0] == null || matrix[0].length == 0) {
    			return ans;
    		}
    		int m = matrix.length;
    		int n = matrix[0].length;
    		int a = 0;
    		int b = 0;
    		while (a < (m + 1) / 2 && b < (n + 1) / 2) {
    			// special cases
    			if (2 * a + 1 == m && 2 * b + 1 == n) {
    				ans.add(matrix[a][b]);
    				break;
    			} else if (2 * a + 1 == m) {
    				for (int j = b; j <= n - 1 - b; j++) {
    					ans.add(matrix[a][j]);
    				}
    				break;
    			} else if (2 * b + 1 == n) {
    				for (int i = a; i <= m - 1 - a; i++) {
    					ans.add(matrix[i][b]);
    				}
    				break;
    			}
    			// now is the general case
    			// first horizontal row without last element
    			for (int j = b; j < n - 1 - b; j++) {
    				ans.add(matrix[a][j]);
    			}
    			// vertical column on right-hand side
    			for (int i = a; i < m - 1 - a; i++) {
    				ans.add(matrix[i][n - 1 - b]);
    			}
    			for (int j = n - 1 - b; j > b; j--) {
    				ans.add(matrix[m - 1 - a][j]);
    			}
    			for (int i = m - 1 - a; i > a; i--) {
    				ans.add(matrix[i][b]);
    			}
    			a++;
    			b++;
    		}
    		return ans;
        }
    }

**Updated Oct 29, 2022**

```
    public List<Integer> spiralOrder(int[][] matrix) {
        int[][] direct = {
            {0, 1},
            {1, 0},
            {0, -1},
            {-1, 0}
        };
        int m = matrix.length;
        int n = matrix[0].length;
        List<Integer> ans = new LinkedList<Integer>();
        boolean[][] visited = new boolean[m][n];

        int x = 0;
        int y = 0;
        int k = 0;
        while (ans.size() < m * n) {
            visited[x][y] = true;
            ans.add(matrix[x][y]);
            int nextX = x + direct[k][0];
            int nextY = y + direct[k][1];
            if (nextX < 0 || nextX >= m
                    || nextY < 0 || nextY >= n
                    || visited[nextX][nextY]) {
                k = (k + 1) % 4;
                x += direct[k][0];
                y += direct[k][1];
            } else {
                x = nextX;
                y = nextY;
            }
        }
        return ans;
    }
```
