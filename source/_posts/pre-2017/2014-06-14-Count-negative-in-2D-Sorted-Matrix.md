---
title: "[Question] Count negative in a 2D Sorted Matrix"
category: Question
tags: []
comments: true
date: 2014-06-14 00:00
---


### Question

[link](http://leetcode.com/2010/10/searching-2d-sorted-matrix.html)

<blockquote>
<p class="font-color">Write an efficient algorithm that searches for a value in an <i>n</i> x <i>m</i> table (two-dimensional array). This table is sorted along the rows and columns — that is,</p><p class="font-color">Table[i][j] ≤ Table[i][j + 1], <br>Table[i][j] ≤ Table[i + 1][j]</p>
</blockquote>

### Related questions

**[Search a 2D Matrix](/leetcode/2014-05-21-Search-a-2D-Matrix)**.

**[Searching a 2D Sorted Matrix](/leetcode_plus/2014-06-10-Searching-a-2D-Sorted-Matrix)**.

**[Count negative in a 2D Sorted Matrix](/question/2014-06-14-Count-negative-in-2D-Sorted-Matrix)**.

### Analysis

This is a very similar question as prevous one. The solution is O(n) with a linear walk from top-right to bottom-left.

### Code

    int countNegatives(int array[][], int size) {
        int col = size - 1, row = 0;
        int count = 0;

        while(row &lt; size && col &gt;= 0) {
            if(array[row][col] &lt; 0 ) {
                count = count + (col + 1);
                row = row + 1;
            }
            else {
                col = col - 1;
            }
        }
        return count;
    }
