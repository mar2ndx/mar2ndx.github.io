---
title: 【Tech】 Vi tutorial
category: unknown
tags: technology
comments: true
date: 2015-04-24 00:00:00
---


# About Vi

Vi is a text editor built written in C, for Unit/Linux since 1976. It is default for Unix systems.

> Over the years since its creation, vi became the de facto standard Unix editor and a nearly undisputed hacker favorite[citation needed] outside of MIT until the rise of Emacs after about 1984.
>
>-- <cite>Wikipedia[1]</cite>

# Why Vi

I have to use Vi when I setup my VPS for web hosting. Vi confuses me a while since I have no prior experience. Over time, I came to realize that using Vi is a must for a developer, so let's don't hesitate to jump at it!

We'll get started by learning some of the basics.

# Getting started

First of all, Vi have 2 modes: __Command Mode__ and __Insert Mode__.

Remember how to switch mode:

1. press 'i' for Insert Mode
2. press "Esc" for Command Mode

## 3 basic file commands

1. :w - save
2. :q - quit
3. :q! - quit without saving

## Move the cursor

When in command mode, the key h, j, k and l can move the cursor, just like your arrow key.

1. h - Cursor left
1. j - Cursor down
1. k - Cursor up
1. l - Cursor right

## Delete

In command mode:

1. x - delete 1 char
1. dd - delete 1 line

Difference between 'backspace' and 'x':

1. backspace - works in insert mode. Can only delete chars inserted in current session.
1. x - works in command mode. Can delete anything.

## Repeat operation

In command mode, input a number then the command, the command with be repeat corresponding number of times. Eg "20dd" deletes 20 lines.

# Last word

This definitely is not a thorough tutorial, but it's enough for basic needs of a system admin. I learn these from the 2 tutorials from [unix-manuals](http://www.unix-manuals.com/tutorials/vi/vi-in-10-1.html)

Hope it helps you.

[1]:http://en.wikipedia.org/wiki/Vi
