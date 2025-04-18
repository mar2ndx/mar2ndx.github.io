---
title: 241. Different Ways to Add Parentheses
category: Leetcode
tags: []
comments: true
date: 2022-11-09 18:33
---



Link: https://leetcode.cn/problems/different-ways-to-add-parentheses/

# Question

difficulty: mid
adj diff: 5

    Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

    The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.

    Example 1:

    Input: expression = "2-1-1"
    Output: [0,2]

    Explanation:

        ((2-1)-1) = 0
        (2-(1-1)) = 2

    Example 2:

    Input: expression = "2*3-4*5"
    Output: [-34,-14,-10,-10,10]

    Explanation:

        (2*(3-(4*5))) = -34
        ((2*3)-(4*5)) = -14
        ((2*(3-4))*5) = -10
        (2*((3-4)*5)) = -10
        (((2*3)-4)*5) = 10

    Constraints:

    1 <= expression.length <= 20
    expression consists of digits and the operator '+', '-', and '*'.
    All the integer values in the input expression are in the range [0, 99].

这道题好难，不会。

用 dfs + divide and concur，方法很巧妙。看代码

# Code

参考了：https://leetcode.cn/problems/different-ways-to-add-parentheses/solution/by-ac_oier-z07i/

```
    public List<Integer> diffWaysToCompute(String expression) {
        return dfs(expression.toCharArray(), 0, expression.length() - 1);
    }

    private List<Integer> dfs(char[] input, int start, int end) {
        List<Integer> ans = new LinkedList<Integer>();

        for (int i = start; i <= end; i++) {
            if (isDigit(input[i])) {
                // we only look for operator, skip all numbers
                continue;
            } else {
                // is an operator: {+, -, *}, divide and concur
                List<Integer> leftChildren = dfs(input, start, i - 1);
                List<Integer> rightChildren = dfs(input, i + 1, end);
                for (Integer v: leftChildren) {
                    for (Integer w: rightChildren) {
                        ans.add(calculate(v, input[i], w));
                    }
                }
            }
        }

        // if no operator is found? it's just number
        if (ans.isEmpty()) {
            int num = 0;
            for (int i = start; i <= end; i++) {
                num = num * 10 + input[i] - '0';
            }
            ans.add(num);
        }
        return ans;
    }

    private int calculate(int num1, char operator, int num2) {
        switch (operator) {
            case '+': return num1 + num2;
            case '-': return num1 - num2;
            case '*': return num1 * num2;
        }
        return 0;
    }

    private boolean isDigit(char ch) {
        if ('0' <= ch && ch <= '9') {
            return true;
        }
        return false;
    }
```
