---
title: 【Tech】 Install Joplin on Linux
category: unknown
tags: ubuntu
comments: true
date: 2021-11-04 00:00:00
---


# Joplin Terminal

这里只讲 terminal 版的 joplin, 不涉及桌面app。

https://joplinapp.org/terminal/

## Instruction

按照官方的说法，是这样的：

1. Install Node/npm
1. Run this：

	NPM_CONFIG_PREFIX=~/.joplin-bin npm install -g joplin
	sudo ln -s ~/.joplin-bin/bin/joplin /usr/bin/joplin
	
也就是，Joplin 没有编译好的 deb 包，相当于安装了一个 npm 包。

问题是，很多依赖都在github上面，需要翻墙才能取到。

	:~# npm config get registry
	https://registry.npm.taobao.org/

实际多次测试表明，换taobao源不能解决问题：

	~/.joplin-bin# NPM_CONFIG_PREFIX=~/.joplin-bin npm install -g joplin
	npm ERR! code 128
	npm ERR! An unknown git error occurred
	npm ERR! command git --no-replace-objects ls-remote ssh://git@github.com/laurent22/uslug.git
	npm ERR! command-line line 0: unsupported option "accept-new".
	npm ERR! fatal: Could not read from remote repository.
	npm ERR! 
	npm ERR! Please make sure you have the correct access rights
	npm ERR! and the repository exists.

	npm ERR! A complete log of this run can be found in:
	npm ERR!     /root/.npm/_logs/2021-11-03T18_33_32_725Z-debug.log

这样也无济于事：

	npm i -g uslug

看来只能路由器翻墙解决了~

## Solution

