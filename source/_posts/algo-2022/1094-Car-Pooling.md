---
title: 1094. Car Pooling
category: Leetcode
tags: []
comments: true
date: 2024-07-16 01:20
---


Link: https://leetcode.cn/problems/car-pooling/

# Question

difficulty: mid
adj diff: 2

    There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).
    
    You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.
    
    Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.
    
     
    
    Example 1:
    
    Input: trips = [[2,1,5],[3,3,7]], capacity = 4
    Output: false
    
    Example 2:
    
    Input: trips = [[2,1,5],[3,3,7]], capacity = 5
    Output: true
    
     
    
    Constraints:
    
        1 <= trips.length <= 1000
        trips[i].length == 3
        1 <= numPassengersi <= 100
        0 <= fromi < toi <= 1000
        1 <= capacity <= 105

既然 length 只有1000，那就用 extra space来做吧！

# Code

    class Solution {
        public boolean carPooling(int[][] trips, int capacity) {
            int[] tracker = new int[1001];
            for (int[] trip: trips) {
                tracker[trip[1]] -= trip[0];
                tracker[trip[2]] += trip[0];
            }
            int cap = capacity;
            for (int i: tracker) {
                cap += i;
                if (cap < 0) return false;
            }
            return true;
        }
    }
