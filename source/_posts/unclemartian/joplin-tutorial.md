---
title: 【Tech】 Joplin Tutorial
category: unknown
tags: technology
comments: true
date: 2022-05-28 00:00:00
---


# Joplin usage

我常用的Joplin commands如下：

    :mknote 'hello world'
    :rmnote $n
    :sync
    :exit

## 缩写

See below for [the full list of default shortcuts](https://joplinapp.org/terminal/):

    :                 enter_command_line_mode
    TAB               focus_next
    ENTER             activate
    DELETE, BACKSPACE delete
    (SPACE)           todo toggle $n
    n                 next_link
    b                 previous_link
    o                 open_link
    __tc__                toggle_console
    tm                toggle_metadata
    /                 search ""
    __mn__                mknote ""
    mt                mktodo ""
    mb                mkbook ""
    yn                cp $n ""
    dn                mv $n ""

## 如果不小心按了空格

如果不小心按了空格，会发现note title前面多了一个[x]。每次再按空格，就会变一下。

这个note实际上被 convert to 一个 todo item 了。

Quote：

    (SPACE)           todo toggle $n

还有：

    todo <todo-command> <note-pattern>

    <todo-command> can either be "toggle" or "clear". Use "toggle" to toggle
    the given to-do between completed and uncompleted state (If the target is
    a regular note it will be converted to a to-do). Use "clear" to convert
    the to-do back to a regular note.

所以，出现这种情况，这样就行：

    :todo clear $n

