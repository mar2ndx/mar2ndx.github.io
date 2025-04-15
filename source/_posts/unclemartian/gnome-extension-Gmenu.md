---
title: 【Tech】 Gnome extension - Gnomenu
category: unknown
tags: ubuntu
comments: true
date: 2022-04-24 00:00:00
---


# Gnomenu

[Gno-Menu](https://extensions.gnome.org/extension/608/gnomenu/) is a traditional styled __full featured Gnome-Shell apps menu__, that aims to offer all the essentials in a simple uncluttered intuitive interface.

Source Code: https://github.com/The-Panacea-Projects/Gnomenu

# Challenges

在 Pop!_OS上面，安装报错如下：

    pop-os gnome-shell[60693]: JS ERROR: Extension gnomenu@panacier.gmail.com: Error: Requiring GMenu, version none: Typelib file for namespace 'GMenu' (an>
        @/home/username/.local/share/gnome-shell/extensions/gnomenu@panacier.gmail.com/extension.js:22:15
        _callExtensionInit@resource:///org/gnome/shell/ui/extensionSystem.js:425:13
        loadExtension@resource:///org/gnome/shell/ui/extensionSystem.js:346:27
        callback@resource:///org/gnome/shell/ui/extensionDownloader.js:234:39
        gotExtensionZipFile/<@resource:///org/gnome/shell/ui/extensionDownloader.js:115:13

## 查看错误

用 journalctl 来查看报错：

    sudo journalctl /usr/bin/gnome-shell --since "2022-04-23 23:15:00"

Or:

    sudo journalctl /usr/bin/gnome-shell | grep 'gnomenu'

## GMenu

从报错看，是缺少了 GMenu。但是直接 apt install 是不行了。[原因在此](https://github.com/The-Panacea-Projects/Gnomenu/issues/125).

Quote: 

> With Pop_OS 19.04 you need package gir1.2-gmenu-3.0 and it dependency libgnome-menu-3-0 for this extension to work. After that "Download button" top right. Rename the extracted folder to " gnomenu@panacier.gmail.com " and move to your extensions folder. restart gnome-shell or logout/login.
>
> For the record the error message was:
> Aug 10 17:25:33 pop-os gnome-shell[3231]: Extension "gnomenu@panacier.gmail.com" had error: Error: Requiring GMenu, version none: Typelib file for namespace 'GMenu' (any version) not found
>
> methilnet commented on Aug 11, 2019

## Solution

安装依赖：

    sudo apt install gnome-menus
    sudo apt install gir1.2-gmenu-3.0

下载 zip，手动解压并重命名为“gnomenu@panacier.gmail.com”，移动到 /home/username/.local/share/gnome-shell/extensions/

https://github.com/The-Panacea-Projects/Gnomenu

最后，重启 gnome

Alt + F2，输入‘r’ ([This command mainly restarts the session without closing it.](https://ubunlog.com/en/restart-frozen-gnome-session/))

大功告成！
