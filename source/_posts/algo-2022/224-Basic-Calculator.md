---
title: 224. Basic Calculator
category: Leetcode
tags: []
comments: true
date: 2022-11-01 05:08
---


Link: https://leetcode.cn/problems/basic-calculator/

# Question

difficulty: hard
adj diff: 5

    Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

	Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

	 

	Example 1:

	Input: s = "1 + 1"
	Output: 2

	Example 2:

	Input: s = " 2-1 + 2 "
	Output: 3

	Example 3:

	Input: s = "(1+(4+5+2)-3)+(6+8)"
	Output: 23

	 

	Constraints:

		1 <= s.length <= 3 * 105
		s consists of digits, '+', '-', '(', ')', and ' '.
		s represents a valid expression.
		'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
		'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
		There will be no two consecutive operators in the input.
		Every number and running calculation will fit in a signed 32-bit integer.

Too hard. 太难了，不会写。

2条Stack，一个存 number，一个存operator。看代码吧。

# Code

Solution reference: https://leetcode.cn/problems/basic-calculator/solution/shuang-zhan-jie-jue-tong-yong-biao-da-sh-olym/

```
class Solution {

    Stack<Integer> numbers = new Stack<Integer>();
    Stack<Character> operators = new Stack<Character>();

    public int calculate(String s) {
        numbers.push(0);
        char[] expression = s.replace(" ", "").toCharArray();

        for (int i = 0; i < expression.length; i++) {
            char ch = expression[i];
            if (ch == '(') {
                operators.push(ch);
            } else if (ch == ')') {
                while (!operators.isEmpty()) {
                    // 计算到最近一个左括号为止
                    if (operators.peek() == '(') {
                        operators.pop();
                        break;
                    } else {
                        calculateOnce();
                    }
                }
            } else if ('0' <= ch && ch <= '9') {
                int u = 0;
                int j = i;
                // 将从 i 位置开始后面的连续数字整体取出，加入 numbers
                while (j < expression.length 
                        && ('0' <= expression[j] && expression[j] <= '9')
                    ) {
                    u = u * 10 + (int)(expression[j++] - '0');
                }
                numbers.push(u);
                i = j - 1;
            } else { // is an operator, namely: + or -
                if (i > 0 
                    && (expression[i - 1] == '(' 
                        || expression[i - 1] == '+' 
                        || expression[i - 1] == '-')
                    ) {
                    numbers.push(0);
                }
                // 有一个新操作要入栈时，先把栈内可以算的都算了
                while (!operators.isEmpty() && operators.peek() != '(') {
                    calculateOnce();
                }
                operators.push(ch);
            }
        }

        while (!operators.isEmpty()) {
            calculateOnce();
        }
        return numbers.peek();
    }

    private void calculateOnce() {
        if (numbers.isEmpty() || numbers.size() < 2) return;
        if (operators.isEmpty()) return;
        int b = numbers.pop(), a = numbers.pop();
        char op = operators.pop();
        numbers.push(op == '+' ? a + b : a - b);
    }
}
```
