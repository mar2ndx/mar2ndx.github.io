---
title: 1628. Design an Expression Tree With Evaluate Function
category: Leetcode
tags: []
comments: true
date: 2022-11-20 05:41
---



Link: https://leetcode.cn/problems/design-an-expression-tree-with-evaluate-function/

# Question

difficulty: mid
adj diff: 4
    
    Given the postfix tokens of an arithmetic expression, build and return the binary expression tree that represents this expression.
    
    Postfix notation is a notation for writing arithmetic expressions in which the operands (numbers) appear before their operators. For example, the postfix tokens of the expression 4*(5-(7+2)) are represented in the array postfix = ["4","5","7","2","+","-","*"].
    
    The class Node is an interface you should use to implement the binary expression tree. The returned tree will be tested using the evaluate function, which is supposed to evaluate the tree's value. You should not remove the Node class; however, you can modify it as you wish, and you can define other classes to implement it if needed.
    
    A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes (nodes with two children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).
    
    It's guaranteed that no subtree will yield a value that exceeds 109 in absolute value, and all the operations are valid (i.e., no division by zero).
    
    Follow up: Could you design the expression tree such that it is more modular? For example, is your design able to support additional operators without making changes to your existing evaluate implementation?
    
     
    
    Example 1:
    
    Input: s = ["3","4","+","2","*","7","/"]
    Output: 2
    Explanation: this expression evaluates to the above binary tree with expression ((3+4)*2)/7) = 14/7 = 2.
    
    Example 2:
    
    Input: s = ["4","5","2","7","+","-","*"]
    Output: -16
    Explanation: this expression evaluates to the above binary tree with expression 4*(5-(2+7)) = 4*(-4) = -16.
    
     
    
    Constraints:
    
        1 <= s.length < 100
        s.length is odd.
        s consists of numbers and the characters '+', '-', '*', and '/'.
        If s[i] is a number, its integer representation is no more than 105.
        It is guaranteed that s is a valid expression.
        The absolute value of the result and intermediate values will not exceed 109.
        It is guaranteed that no expression will include division by zero.

这道题挺有意思，写完了不后悔。

## 首先：Java interface

abstract vs. interface

> An abstract class is declared when it has one or more abstract methods.
>
> Abstract class can have data members and non-abstract methods.

For more, read https://mar2ndx.github.io/2015/01/20/java-abstract-class-interface/

## 其次：如何写 Enum

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

## 最后，算法

1. build tree：用 Stack。
2. evaluate方法：递归计算。

# Code

```
/**
 * This is the interface for the expression tree Node.
 * You should not remove it, and you can define some classes to implement it.
 */
abstract class Node {
    NodeType nodeType;
    int number;
    Node left;
    Node right;

    protected enum NodeType {
        OPERAND,    // 操作数
        ADD,        // 加
        SUBTRACT,   // 减
        MULTIPLY,   // 乘
        DIVIDE      // 除
    }

    public abstract int evaluate();
};

// implementation class for the Node interface
class LeetcodeNode extends Node {
    public LeetcodeNode(boolean isNumber, String input) {
        if (isNumber) {
            this.nodeType = NodeType.OPERAND;
            this.number = Integer.parseInt(input);
        } else {
            if (input.equals("+")) {
                this.nodeType = NodeType.ADD;
            } else if (input.equals("-")) {
                this.nodeType = NodeType.SUBTRACT;
            } else if (input.equals("*")) {
                this.nodeType = NodeType.MULTIPLY;
            } else if (input.equals("/")) {
                this.nodeType = NodeType.DIVIDE;
            }
        }
    }

    @Override
    public int evaluate() {
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
    }
}

/**
 * Your TreeBuilder object will be instantiated and called as such:
 * TreeBuilder obj = new TreeBuilder();
 * Node expTree = obj.buildTree(postfix);
 * int ans = expTree.evaluate();
 */

class TreeBuilder {
    Node buildTree(String[] postfix) {
        Stack<LeetcodeNode> stack = new Stack<LeetcodeNode>();
        LeetcodeNode root = null;
        
        for (int i = 0; i < postfix.length; i++) {
            if (postfix[i].equals("+") || postfix[i].equals("-") 
            || postfix[i].equals("*") || postfix[i].equals("/")) {
                LeetcodeNode node = new LeetcodeNode(false, postfix[i]);
                node.right = stack.pop();
                node.left = stack.pop();
                stack.push(node);
            } else {
                LeetcodeNode node = new LeetcodeNode(true, postfix[i]);
                stack.push(node);
            }
        }
        return stack.peek();
    }
};
```
