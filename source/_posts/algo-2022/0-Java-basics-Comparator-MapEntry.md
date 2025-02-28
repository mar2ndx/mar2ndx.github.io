---
title: Java一些基础语法：Comparator, MapEntry, Iterator
category: Java Basic
tags: []
comments: true
date: 2022-11-20 05:37
---

**经验：尽量用 Comparator，不要用 Comparable。**

Comparator class 标准写法：

```
    Queue<ListNode> heap = new PriorityQueue(size, new NodeComparator());

    class NodeComparator implements Comparator<ListNode> {
        public int compare(ListNode n1, ListNode n2) {
            return n1.val - n2.val;
        }
    }
```

Comparator inline 简化写法：

```
    Collections.sort(freq, new Comparator<int[]>() {
    	public int compare(int[] keyValue1, int[] keyValue2) {
    		return keyValue1[1] - keyValue2[1];
    	}
    });
```

PriorityQueue inline 简化写法 ：

(这种写法只对 primitive type，比如 integer array，注意尽量少这么写！)

```
    PriorityQueue<int[]> queue = new PriorityQueue<int[]>(new Comparator<int[]>() {
    	public int compare(int[] m, int[] n) {
    		return m[1] - n[1];
    	}
    });
```

class implements Comparable<> 写法：

```
    class TeamVotes implements Comparable<TeamVotes> {
        char team;

        public int compareTo(TeamVotes tv) {
            return this.team - tv.team;
        }
    }
```

Iterate a Map：

```
    Map<Integer, Integer> group = new HashMap<Integer, Integer>();
    for (Map.Entry<Integer, Integer> entry : group.entrySet()) {
    	int a = entry.getKey();
    	int b = entry.getValue();
    	int keyValue = {entry.getKey(), entry.getValue()};
    }
```

Iterate a Map（简易版）：

```
    Map<String, Object> map = ...;
    for (String key : map.keySet()) {
    	key;
    }
```

Iterate a HashSet:

```
    HashSet<String> set = new HashSet<>();

    // Iterate throw a simple for loop
    for (String ele : set) {
    	// Print HashSet data
    	System.out.print(ele + " ");
    }
```

Or, using a Iterator:

```
    Iterator<String> itr = set.iterator();
    while (itr.hasNext()) {
       System.out.println(itr.next());
    }
```

Java Enum：

```
    enum NodeType {
        OPERAND,    // 操作数
        ADD,        // 加
        SUBTRACT,   // 减
        MULTIPLY,   // 乘
        DIVIDE      // 除
    }

    switch (this.nodeType) {
        case OPERAND:
            return this.number;
        case ADD:
            return left.evaluate() + right.evaluate();
        case SUBTRACT:
            return left.evaluate() - right.evaluate();
        case MULTIPLY:
            return left.evaluate() * right.evaluate();
        case DIVIDE:
            return left.evaluate() / right.evaluate();
        default:
            throw new AssertionError();
    }
```
