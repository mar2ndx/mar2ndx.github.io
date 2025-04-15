---
title: 【Tech】 Check Folder Size on Linux
category: unknown
tags: ubuntu
comments: true
date: 2022-04-27 00:00:00
---


# Command

Go to the folder and: 

    du -ah --max-depth=1

To view the sorted result: 

    du -a --max-depth=1 | sort -n -r
