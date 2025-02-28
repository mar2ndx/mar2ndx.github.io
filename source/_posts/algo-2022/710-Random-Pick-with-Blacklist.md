---
title: 710. Random Pick with Blacklist
category: Leetcode
tags: []
comments: true
date: 2022-11-08 21:39
---



Link: https://leetcode.cn/problems/random-pick-with-blacklist/

# Question

    difficulty: hard
    adj diff: 5

    You are given an integer n and an array of unique integers blacklist. Design an algorithm to pick a random integer in the range [0, n - 1] that is not in blacklist. Any integer that is in the mentioned range and not in blacklist should be equally likely to be returned.

    Optimize your algorithm such that it minimizes the number of calls to the built-in random function of your language.

    Implement the Solution class:

    	Solution(int n, int[] blacklist) Initializes the object with the integer n and the blacklisted integers blacklist.
    	int pick() Returns a random integer in the range [0, n - 1] and not in blacklist.

    Example 1:

    Input
    ["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
    [[7, [2, 3, 5]], [], [], [], [], [], [], []]
    Output
    [null, 0, 4, 1, 6, 1, 0, 4]

    Explanation
    Solution solution = new Solution(7, [2, 3, 5]);
    solution.pick(); // return 0, any integer from [0,1,4,6] should be ok. Note that for every call of pick,
    				 // 0, 1, 4, and 6 must be equally likely to be returned (i.e., with probability 1/4).
    solution.pick(); // return 4
    solution.pick(); // return 1
    solution.pick(); // return 6
    solution.pick(); // return 1
    solution.pick(); // return 0
    solution.pick(); // return 4
    Constraints:

    	1 <= n <= 109
    	0 <= blacklist.length <= min(105, n - 1)
    	0 <= blacklist[i] < n
    	All the values of blacklist are unique.
    	At most 2 * 104 calls will be made to pick.

这道题，代码比较难写。

思路如下：

    // n = 11 & blacklist = {7, 9}
    // 0 1 2 3 4 5 6 (7) 8 (9) 10

在 11 - 2 = 9 的位置，做一下切割：

    // 0 1 2 3 4 5 6 (7) 8 ||| (9) 10

然后，在 map 种，放入整个 k-v：

    // map = { 7 => 10}

这样，我 generate 一个[0, 9) 范围内的 int rand = generateRandom()。如果 rand == 7，则返回 10；否则直接返回 rand。

# Code

```
class Solution {

    Random random = new Random();
    Map<Integer, Integer> map = new HashMap<Integer, Integer>();
    int range;

    public Solution(int n, int[] blacklist) {
        // eg. 0 1 2 3 4 5 6 (7) 8 (9) 10 (n = 11 & blacklist = {7, 9})
        // generate random number in the range of [0, 8]
        // if got 8, return 8; if got 7, return 10;
        Arrays.sort(blacklist);
        range = n - blacklist.length;

        if (blacklist.length == 0) return;

        // eg. 0 1 2 3 4 5 6 (7) 8 || (9) 10 (range = 9)
        // need to put into the map [7 -> 10]
        int left = 0, right = blacklist.length - 1;
        int validNum = n - 1;

        while (left <= right && blacklist[left] < range) {
            while (blacklist[right] == validNum) {
                right--;
                validNum--;
            }
            map.put(blacklist[left], validNum);
            left++;
            validNum--;
        }
    }

    public int pick() {
        int genRand = random.nextInt(range);
        if (map.containsKey(genRand)) {
            return map.get(genRand);
        } else {
            return genRand;
        }
    }
}
```
