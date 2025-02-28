---
title: 1710. Maximum Units on a Truck
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:51
---


Link: https://leetcode.cn/problems/maximum-units-on-a-truck/

# Question

difficulty: easy
adj diff: 2

    You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

    numberOfBoxesi is the number of boxes of type i.
    numberOfUnitsPerBoxi is the number of units in each box of the type i.
    You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

    Return the maximum total number of units that can be put on the truck.

     

    Example 1:

    Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
    Output: 8
    Explanation: There are:
    - 1 box of the first type that contains 3 units.
    - 2 boxes of the second type that contain 2 units each.
    - 3 boxes of the third type that contain 1 unit each.
    You can take all the boxes of the first and second types, and one box of the third type.
    The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
    Example 2:

    Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
    Output: 91
     

    Constraints:

    1 <= boxTypes.length <= 1000
    1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
    1 <= truckSize <= 106

排序 + 贪心。

# Code

```
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        Arrays.sort(boxTypes, new Comparator<int[]>() {
            public int compare(int[] array1, int[] array2) {
                // sort boxes by numberOfUnitsPerBox (descending order)
                return array2[1] - array1[1];
            }
        });

        int totalUnits = 0;
        int p = 0;
        while (p < boxTypes.length) {
            int takeBoxes = Math.min(boxTypes[p][0], truckSize);
            totalUnits += takeBoxes * boxTypes[p][1];
            truckSize -= takeBoxes;
            if (truckSize == 0)
                break;
            p++;
        }
        return totalUnits;
    }
```
