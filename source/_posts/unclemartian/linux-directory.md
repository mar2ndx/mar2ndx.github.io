---
title: 【Tech】 Linux Directory Structure
category: unknown
tags: technology
comments: true
date: 2015-04-28 00:00:00
---


# Overview

## a brief introduction

1. bin - user binary
2. boot - boot loader
3. dev - device (manipulate your hard drives)
4. etc - config files
5. home - user home dir except root
6. initrd.img 
7. lib - system library
8. lib64
9. lost+found
10. media - removable devices (CD, USB etc)
11. mnt - mount file systems
12. opt - optional (eg. desktop environment)
13. proc - process info
14. root - root user's home
15. run
16. sbin - system binary (runnable only by root)
17. srv - service data
18. sys
19. tmp - temporary (delete on restart)
20. usr - Unix System Resources (user programs)
	1. usr/bin - user programs
	1. usr/lib - user system lib
	1. usr/local -  programs that's __manually compiled__ rather than install from package
	1. usr/sbin - root programs
21. var - variables, application data (eg. MySQL db, cached files)

Reference: <cite>Linux Directory Structure (File System Structure) Explained with Examples</cite>[1]

# Some important folders

## bin, sbin, usr/bin, usr/sbin

__bin/__ stores commands needed during boot-up that might be needed by normal users. eg. cat, tar...

> Applications __such as Firefox__ are stored in /usr/bin, while important system programs and utilities such as the __bash shell__ are located in /bin. 

__sbin/__ is like bin but commands are not intended for normal users. Commands run by LINUX. eg. ifconfig, fdisk...

__/usr/bin__ is all user commands, while __/usr/sbin__ is system admin commands not needed on the root filesystem. e.g. most server programs.

## proc

This filesystem is not on a disk. Exists in the kernels imagination (virtual). 

It holds information about kernel parameters and system configuration.

## usr

__/usr__ usually contains by far the largest share of data on a system. Hence, this is [one of the most important directories](http://www.tldp.org/LDP/Linux-Filesystem-Hierarchy/html/usr.html) in the system as it contains all the __user binaries, their documentation, libraries, header files__, etc.... 

Reference: [Linux Directory Structure](http://www.comptechdoc.org/os/linux/usersguide/linux_ugfilestruct.html)

# A brief history

> Originally, there was /bin for programs, /dev for device files and /lib for extra executable code and /usr for user data. 

> The source code was also often provided somewhere under /usr.

> And there were a few files in the operating system that didn't fit in any of the existing categories. This included __a passwd file containing users' passwords__, and __an mtab file written by mount__. 

> At first, there was no connotation that files in __/etc__ were configuration files. In these very early days, if you wanted to customize something, you'd be recompiling that part of the system. As Unix got more powerful, there were more and more things you could do without recompiling. As Unix got used more widely, there were more and more things people wanted to do, and they found ways of doing them without going through the trouble of recompiling. 

> So __/etc__ filled up with more and more text files that people could and did customize, hence it gradually became the configuration directory.

> With the creation of __/sbin__ to contain programs intended only for the system administrator, __/etc__ ended up containing only text files, many of which can be customized by the system administrator. 

Reference: [Answer by Gilles on StackExchange](http://unix.stackexchange.com/a/56172)

[1]: http://www.thegeekstuff.com/2010/09/linux-file-system-structure/
