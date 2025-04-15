---
title: 【Tech】 Armbian day to day 使用教程
category: unknown
tags: ubuntu
comments: true
date: 2021-10-19 09:00:00
---



# SSH 登陆

WKY

    export LC_ALL="en_US.UTF-8" && mosh root@192.168.123.215
    a***

wky上面有两个账户：root和wky，密码一样。

## Tmux

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

参考 https://linuxize.com/post/getting-started-with-tmux/

# WKY控制台

Webmin 在 10,000 端口。

https://192.168.123.215:10000

    wky
    a***

## Resilio 同步

https://192.168.123.215:8888/gui/

    wky
    a***

## Syncthing

https://192.168.123.215:8384

    wky
    a***

# N1桌面系统

（deprecated）

RDP：192.168.123.242:3389
