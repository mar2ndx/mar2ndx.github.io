---
layout: post
title: "[NineChap 2.1] Binary Search"
comments: true
category: NineChap
---

## Binary Search

#### Recursion or While-Loop?

In general, it's never a good idea to do binary search with recursion, because that'll make the interview too boring.

#### Template

[link](http://answer.ninechapter.com/solutions/binary-search/)

This template is able to locate the first (or last) occurance of an element **when array contains duplications**.

If item too small/large, left/right boundary is returned.

Read Question "Search for a Range" for more details.

    int binarySearch(vector<int> &A, int target) {
        if (A.size() == 0) {
            return -1;
        }

        int start = 0;
        int end = A.size() - 1;
        int mid;

        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (A[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (A[start] == target) {
            return start;
        }
        if (A[end] == target) {
            return end;
        }

        return -1;
    }

#### Keypoints

1. start + 1 < end
2. start + (end-start)/2
3. A[mid] ==, <, >
4. A[start/end] == target

## Question list

**Binary search**

1. **[Search Insert Position](/leetcode/2014-05-12-Search-Insert-Position)**

2. **[Search for a Range](/leetcode/2014-05-12-Search-for-a-Range)**

3. **[Search in Rotated Sorted Array](/leetcode/2014-05-12-Search-in-Rotated-Sorted-Array)**

4. **[Search in Rotated Sorted Array II](/leetcode/2014-05-22-Search-in-Rotated-Sorted-Array-II)**

5. **[Search a 2D Matrix](/leetcode/2014-05-21-Search-a-2D-Matrix)**

**Additional**

1. **[Search a 2D Matrix II](/leetcode_plus/2014-06-10-Searching-a-2D-Sorted-Matrix)** - A tricky question

2. **Find the First Bad Version**

   The code base version is an integer and start from 0 to n. One day, someone commit a bad version in the code case, so it caused itself and the following versions are all failed in the unittests. You can determine whether a version is bad by the following interface:

   > boolean isBadVersion(int version);

   Find the first bad version.

3. **Find a peek**

   There is an array which we can assume the numbers in adjcent positions are different. and A[0] < A[1] && A[A.length - 2] > A[A.length - 1]. We consider a position P is a peek if A[P] > A[P-1] && A[P] > A[P+1]. Find a peek in this array.

## Code

All following code are written with the template provided above.

**Search Insert Position**

    public int searchInsert(int[] A, int target) {
        // 6 minutes
        if (A == null || A.length == 0) {
            return 0;
        }
        int left = 0, right = A.length - 1;
        int mid;
        while (left + 1 < right) {
            mid = left + (right - left) / 2;
            if (A[mid] < target) {
                left = mid;
            }
            else {
                right = mid;
            }
        }
        if (target <= A[left]) {
            // equal or less than first element
            return left;
        }
        else if (A[left] < target && target <= A[right]) {
            return right;
        }
        else {
            // bigger than largest element
            return right + 1;
        }
    }

**Search for a Range**

    public int[] searchRange(int[] A, int target) {
        // 6 minutes
        int[] result = new int[2];
        result[0] = -1;
        result[1] = -1;
        if (A == null || A.length == 0) {
            return result;
        }
        // find the start point of target
        int left = 0, right = A.length - 1, mid;
        while (left + 1 < right) {
            mid = left + (right - left) / 2;
            if (A[mid] < target) {
                left = mid;
            }
            else {
                right = mid;
            }
        }
        if (A[left] == target) {
            result[0] = left;
        }
        else if (A[right] == target) {
            result[0] = right;
        }
        else {
            return result;
        }
        // find the end point of target
        left = 0;
        right = A.length - 1;
        while (left + 1 < right) {
            mid = left + (right - left) / 2;
            if (A[mid] <= target) {
                left = mid;
            }
            else {
                right = mid;
            }
        }
        if (A[right] == target) {
            result[1] = right;
        }
        else if (A[left] == target) {
            result[1] = left;
        }
        return result;
    }

**Search in Rotated Sorted Array**

Note: this is an high-freq qeustion. Every company will ask this question.

The solution is using 4 if-conditions. It takes long time first, because I compare A[mid] with target. It become complex.

We should compared A[left] and A[mid] first, then it'll be much easier for coding.

    public int search(int[] A, int target) {
        // this is the 4th time that I do this question
        // 7 minutes
        if (A == null || A.length == 0) {
    		return -1;
    	}
    	int left = 0;
    	int right = A.length - 1;
    	int mid;
    	while (left + 1 < right) {
    		mid = left + (right - left) / 2;
    		if (A[mid] == target) {
    			return mid;
    		} else if (A[left] < A[mid]) {
    			if (A[left] <= target && target < A[mid]) {
    				right = mid;
    			} else {
    				left = mid;
    			}
    		} else {
    			if (A[mid] < target && target <= A[right]) {
    				left = mid;
    			} else {
    				right = mid;
    			}
    		}
    	}
    	if (A[left] == target) {
    		return left;
    	} else if (A[right] == target) {
    		return right;
    	}
    	return -1;
    }

**Search in Rotated Sorted Array II**

There are multiple ways to remove duplications. My previous solution is removing duplicate before entering the while-loop, which is a very good idea.

Binary can't be used, because there might be: value of start = mid = end. In this case, the entire list needs to be search. Impossible!

The worse case will anyway take O(n) time. To indicate the time complexity is regardless of binary search, Mr. Huang suggests the following code:

    public boolean search(int[] A, int target) {
        for (int i = 0; i < A.length; i ++) {
            if (A[i] == target) {
                return true;
            }
        }
        return false;
    }

**Search a 2D Matrix**

my code (2D search):

    public boolean searchMatrix(int[][] matrix, int target) {
        // 13 miniutes
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }
        int m = matrix.length;
        int n = matrix[0].length;
        // find target vertically from matrix[0] to matrix[m-1]
        int top = 0, bottom = m - 1;
        int mid;
        while (top + 1 < bottom) {
            mid = top + (bottom - top) / 2;
            if (matrix[mid][0] < target) {
                top = mid;
            }
            else {
                bottom = mid;
            }
        }
        // locate the row number
        int row = -1;
        if (matrix[top][0] <= target && target <= matrix[top][n-1]) {
            row = top;
        }
        else if (matrix[bottom][0]<=target && target <= matrix[bottom][n-1]) {
            row = bottom;
        }
        else {
            return false;
        }
        // now find target from matrix[row]
        int left = 0, right = n - 1;
        while (left + 1 < right) {
            mid = left + (right - left) / 2;
            if (matrix[row][mid] < target) {
                left = mid;
            }
            else {
                right = mid;
            }
        }
        return (matrix[row][left] == target || matrix[row][right] == target);
    }

better code (1D search):

    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        int start = 0;
        int end = rows * cols - 1;
        while (start <= end) {
            int mid = (start + end) / 2;
            // Tricks to treat it as a 1-D array
            int digit = matrix[mid / cols][mid % cols];
            if (target == digit) {
                return true;
            } else if (target > digit) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return false;
    }

**Search a 2D Matrix II**

Read my new post for details.

**Find the First Bad Version**

A simple binary search.

**Find a peek**

A binary search, and for each 'mid' point, judge weather it's a peek, or it's upward sloping, or downward sloping.

Code skipped.

## Conclusion

#### Always try to exclude a half.
