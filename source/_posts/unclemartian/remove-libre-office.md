---
title: 【Tech】 Remove Libre Office from Linux
category: unknown
tags: ubuntu
comments: true
date: 2022-04-19 00:00:00
---


# Libre Office

虽然，Draw 和 Math 好像还挺有用的。

删掉大概能节省 500M 空间。

# Steps

注意：星号。

    sudo apt remove libreoffice*
    sudo apt purge libreoffice*
    sudo apt autoremove
    sudo apt update && sudo apt upgrade -y
