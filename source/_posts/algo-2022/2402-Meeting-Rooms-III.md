---
title: 2402. Meeting Rooms III
category: Leetcode
tags: []
comments: true
date: 2022-11-14 00:08
---



Link: https://leetcode.cn/problems/meeting-rooms-iii/

# Question

difficulty: hard
adj diff: 4

    You are given an integer n. There are n rooms numbered from 0 to n - 1.

    You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

    Meetings are allocated to rooms in the following manner:

    Each meeting will take place in the unused room with the lowest number.
    If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
    When a room becomes unused, meetings that have an earlier original start time should be given the room.
    Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

    A half-closed interval [a, b) is the interval between a and b including a and not including b.

     

    Example 1:

    Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
    Output: 0
    Explanation:
    - At time 0, both rooms are not being used. The first meeting starts in room 0.
    - At time 1, only room 1 is not being used. The second meeting starts in room 1.
    - At time 2, both rooms are being used. The third meeting is delayed.
    - At time 3, both rooms are being used. The fourth meeting is delayed.
    - At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
    - At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
    Both rooms 0 and 1 held 2 meetings, so we return 0.
    Example 2:

    Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
    Output: 1
    Explanation:
    - At time 1, all three rooms are not being used. The first meeting starts in room 0.
    - At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
    - At time 3, only room 2 is not being used. The third meeting starts in room 2.
    - At time 4, all three rooms are being used. The fourth meeting is delayed.
    - At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
    - At time 6, all three rooms are being used. The fifth meeting is delayed.
    - At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
    Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1.
     

    Constraints:

    1 <= n <= 100
    1 <= meetings.length <= 105
    meetings[i].length == 2
    0 <= starti < endi <= 5 * 105
    All the values of starti are unique.

这道题的算法并不算非常难：双 Heap。

1. 一个用来存放 空 room
1. 另一个用来存放 正在进行的 meeting

难点来了：那就是 自定义 comparator。

1. 对于正在进行 meeting 的 heap，implements Comparable<Meeting> 然后定义 compareTo 方法，根据 endTime 从小到大排列。
1. 对于空 room，需要重新自定义一个 comparator()，根据 Room Index 来排列。

## Comparable Vs Comparator

所以，看懂 Comparable 和 Comparator 的区别了吗？

1. Comparable 是一个**内比较器** 的接口。用于 object 自己跟自己比较。
1. Comparator 是一个**外比较器**，用于：
   1. 一个 object 没有 implement Comparable，例如 int[]
   1. 实现了 Comparable，但是我们还想自定义一下

# Code

Code 1 （同时使用 Comparable 和 Comparator，不太推荐）

```
class Solution {
    public int mostBooked(int n, int[][] meetings) {
        int[] usedTime = new int[n];

        // idleRooms: heap, ranked by room index number
        Queue<Meeting> idleRooms = new PriorityQueue<Meeting>(new Comparator<Meeting>() {
            public int compare(Meeting m1, Meeting m2) {
                return m1.roomNumber - m2.roomNumber;
            }
        });
        for (int i = 0; i < n; i++) {
            idleRooms.offer( new Meeting(i) );
        }

        // inProgress: heap, ranked by meeting endTime
        Queue<Meeting> inProgress = new PriorityQueue<Meeting>();
        Arrays.sort(meetings, new Comparator<int[]>() {
            public int compare(int[] meeting1, int[] meeting2) {
                return meeting1[0] - meeting2[0];
            }
        });

        // in time-order, do the following:
        // 1. get the next meeting (start time = T)
        // 2. end meetings in inProgress, whose endTime is before T
        // 3. fetch the next avaible room from idleRooms
        // 4. start the meeting
        for (int i = 0; i < meetings.length; i++) {
            Meeting temp;
            while (!inProgress.isEmpty() && inProgress.peek().endTime <= meetings[i][0]) {
                temp = inProgress.poll();
                idleRooms.offer(temp);
            }

            // if no room is idle, then meetings[i] would need to wait
            long currentMeetingWaitTime = 0;
            if (idleRooms.isEmpty()) {
                temp = inProgress.poll();
                idleRooms.offer(temp);
                currentMeetingWaitTime = temp.endTime - meetings[i][0];
            }
            temp = idleRooms.poll();
            ++usedTime[temp.roomNumber];

            temp.endTime = meetings[i][1] + currentMeetingWaitTime;
            inProgress.offer(temp);
        }

        // All meetings are finished, now count
        int mostUsedRoomNumber = 0;
        for (int i = 1; i < n; i++) {
            if (usedTime[i] > usedTime[mostUsedRoomNumber]) {
                mostUsedRoomNumber = i;
            }
        }
        return mostUsedRoomNumber;
    }
}

class Meeting implements Comparable<Meeting> {
    int roomNumber;
    long endTime;

    public Meeting(int num) {
        roomNumber = num;
    }

    public int compareTo(Meeting m) {
        if (this.endTime == m.endTime) {
            return this.roomNumber - m.roomNumber;
        }
        return Long.compare(this.endTime, m.endTime) ;
    }
}
```

Code 2 （只用 Comparator，推荐）

```
class Solution {
    public int mostBooked(int n, int[][] meetings) {
        int[] usedTime = new int[n];

        // idleRooms: heap, ranked by room index number
        Queue<Meeting> idleRooms = new PriorityQueue<Meeting>(new Comparator<Meeting>() {
            public int compare(Meeting m1, Meeting m2) {
                return m1.roomNumber - m2.roomNumber;
            }
        });
        for (int i = 0; i < n; i++) {
            idleRooms.offer( new Meeting(i) );
        }

        // inProgress: heap, ranked by meeting endTime
        Queue<Meeting> inProgress = new PriorityQueue<Meeting>(new Comparator<Meeting>() {
            public int compare(Meeting m1, Meeting m2) {
                if (m1.endTime == m2.endTime) {
                    return m1.roomNumber - m2.roomNumber;
                }
                return Long.compare(m1.endTime, m2.endTime);
            }
        });
        Arrays.sort(meetings, new Comparator<int[]>() {
            public int compare(int[] meeting1, int[] meeting2) {
                return meeting1[0] - meeting2[0];
            }
        });

        // in time-order, do the following:
        // 1. get the next meeting (start time = T)
        // 2. end meetings in inProgress, whose endTime is before T
        // 3. fetch the next avaible room from idleRooms
        // 4. start the meeting
        for (int i = 0; i < meetings.length; i++) {
            Meeting temp;
            while (!inProgress.isEmpty() && inProgress.peek().endTime <= meetings[i][0]) {
                temp = inProgress.poll();
                idleRooms.offer(temp);
            }

            // if no room is idle, then meetings[i] would need to wait
            long currentMeetingWaitTime = 0;
            if (idleRooms.isEmpty()) {
                temp = inProgress.poll();
                idleRooms.offer(temp);
                currentMeetingWaitTime = temp.endTime - meetings[i][0];
            }
            temp = idleRooms.poll();
            ++usedTime[temp.roomNumber];

            temp.endTime = meetings[i][1] + currentMeetingWaitTime;
            inProgress.offer(temp);
        }

        // All meetings are finished, now count
        int mostUsedRoomNumber = 0;
        for (int i = 1; i < n; i++) {
            if (usedTime[i] > usedTime[mostUsedRoomNumber]) {
                mostUsedRoomNumber = i;
            }
        }
        return mostUsedRoomNumber;
    }
}

class Meeting {
    int roomNumber;
    long endTime;

    public Meeting(int num) {
        roomNumber = num;
    }
}
```

Code 3，简略版。也就是 idleRooms 直接 = new PriorityQueue<Integer>() 。可以少写一个 Comparator），代码短很多。

```
class Solution {
    public int mostBooked(int n, int[][] meetings) {
        int[] usedTime = new int[n];
        Queue<Integer> idleRooms = new PriorityQueue<Integer>();
        for (int i = 0; i < n; i++) {
            idleRooms.offer(i);
        }

        // inProgress: heap, ranked by meeting endTime
        Queue<Meeting> inProgress = new PriorityQueue<Meeting>(new Comparator<Meeting>() {
            public int compare(Meeting m1, Meeting m2) {
                if (m1.endTime == m2.endTime) {
                    return m1.roomNumber - m2.roomNumber;
                }
                return Long.compare(m1.endTime, m2.endTime);
            }
        });

        Arrays.sort(meetings, new Comparator<int[]>() {
            public int compare(int[] meeting1, int[] meeting2) {
                return meeting1[0] - meeting2[0];
            }
        });

        // in time-order, do the following:
        // 1. get the next meeting (start time = T)
        // 2. end meetings in inProgress, whose endTime is before T
        // 3. fetch the next avaible room from idleRooms
        // 4. start the meeting
        for (int i = 0; i < meetings.length; i++) {
            while (!inProgress.isEmpty() && inProgress.peek().endTime <= meetings[i][0]) {
                idleRooms.offer(inProgress.poll().roomNumber);
            }

            // if no room is idle, then meetings[i] would need to wait
            long currentMeetingWaitTime = 0;
            if (idleRooms.isEmpty()) {
                currentMeetingWaitTime = inProgress.peek().endTime - meetings[i][0];
                idleRooms.offer(inProgress.poll().roomNumber);
            }
            Meeting startNewMeeting = new Meeting(
                idleRooms.poll(),
                meetings[i][1] + currentMeetingWaitTime
            );
            ++usedTime[startNewMeeting.roomNumber];
            inProgress.offer(startNewMeeting);
        }

        // All meetings are finished, now count
        int mostUsedRoomNumber = 0;
        for (int i = 1; i < n; i++) {
            if (usedTime[i] > usedTime[mostUsedRoomNumber]) {
                mostUsedRoomNumber = i;
            }
        }
        return mostUsedRoomNumber;
    }
}

class Meeting {
    int roomNumber;
    long endTime;

    public Meeting(int num, long endTime) {
        this.roomNumber = num;
        this.endTime = endTime;
    }
}
```
