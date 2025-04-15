---
title: 【Tech】 Tmux and Mosh
category: unknown
tags: ubuntu
comments: true
date: 2022-03-11 00:00:00
---


# Why

The combination of Tmux and Mosh can increase your life happiness by 15%. 

# Mosh

In a very nutshell;

## Server side

	mosh-server new -c 256 -s -l LANG=en_US.UTF-8 -p 60000
	mosh -v
	nc -lu 60001
	iptables -I INPUT -p udp --dport 60001 -j ACCEPT
	iptables -I INPUT -p udp --dport 60002 -j ACCEPT

## Client side

	mosh root@x.x.x.x
	Or
	export LC_ALL="en_US.UTF-8" && mosh root@x.x.x.x

To debug:

	nc -zvu 124.223.5.33 60001

很多时候，问题就是防火墙。参考上面 iptables 那个 command。

# Tmux

## Tmux Usage

    tmux ls
    tmux attach -t 0 (or simply tmux attach)
    tmux detach -a

窗口操作：

	Ctrl+b % Split current pane horizontally
	Ctrl+b " Split current pane vertically
	Ctrl+b 0 Switch to window 0 (by number)
	Ctrl+b o Go to the next pane
	Ctrl+b ; Toggle between the current and previous pane
	Ctrl+b x Close the current pane
	Ctrl+b d detach current pane

最常用的：

1. % 左右平分出两个窗格

1. " 上下平分出两个窗格

1. x 关闭当前窗格

1. { 当前窗格前移

1. } 当前窗格后移

1. ; 选择上次使用的窗格

1. o 选择下一个窗格，也可以使用上下左右方向键来选择

1. space 切换窗格布局，tmux 内置了五种窗格布局，也可以通过 ⌥1 至 ⌥5来切换

1. z 最大化当前窗格，再次执行可恢复原来大小

1. tmux at [-t 会话名]

参考 https://linuxize.com/post/getting-started-with-tmux/

# Common Practise

At facebook: 

	alias m='mosh -6'
	alias x='mosh -6 dev -- tmux attach -d'

Common Usage: 

	mosh root@x.x.x.x
	tmux ls
	tmux at
