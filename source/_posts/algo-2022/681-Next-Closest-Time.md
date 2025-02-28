---
title: 681. Next Closest Time
category: Leetcode
tags: []
comments: true
date: 2022-11-12 00:21
---



Link: https://leetcode.cn/problems/next-closest-time/

# Question

difficulty: mid
adj diff: 4

    Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

    You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

    Example 1:

    Input: time = "19:34"
    Output: "19:39"
    Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
    It is not 19:33, because this occurs 23 hours and 59 minutes later.
    Example 2:

    Input: time = "23:59"
    Output: "22:22"
    Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
    It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

    Constraints:

    time.length == 5
    time is a valid time in the form "HH:MM".
    0 <= HH < 24
    0 <= MM < 60

# Code

[一个网友写的 穷举法 代码](https://leetcode.cn/problems/next-closest-time/solution/jian-dan-yi-dong-de-suan-fa-yi-kan-jiu-d-t7q2/)

```
class Solution {
    public String nextClosestTime(String time) {
    	List<String> possibleTimes = new ArrayList<>();  // 存储所有合理的事件
    	Set<Character> set = new HashSet<>();

    	List<String> hourList = new LinkedList<>();    // 存储合理的小时部分
    	List<String> monthList = new LinkedList<>();    // 存储合理的分钟部分
    	for(char digit: time.toCharArray()){
    		if(digit != ':') {
                set.add(digit);
            }
    	}

    	for(char ch1: set){
    		for(char ch2: set){
    			String str = ch1 + "" + ch2;
    			if (str.compareTo("24") < 0) {
                    hourList.add(str);
                }
    			if (str.compareTo("60") < 0) {
                    monthList.add(str);
                }
    		}
    	}

    	// 拼接小时与分钟部分
    	for(String h : hourList){
    		for(String m : monthList){
    			possibleTimes.add(h + ":" +m);
    		}
    	}
    	Collections.sort(possibleTimes);         // 排序
    	
        int i = possibleTimes.indexOf(time);   // 获取当前索引
    	if (i == possibleTimes.size() - 1) {
            return possibleTimes.get(0);
        } else {
            return possibleTimes.get(i + 1);
        }
    }
}
```
