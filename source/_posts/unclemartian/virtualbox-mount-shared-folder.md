---
title: 【Tech】 How to mount shared folder for VirtualBox
category: unknown
tags: ubuntu
comments: true
date: 2022-01-10 00:00:00
---


# Problem

Mount shared folders in VirtualBox.

## Install guest add-on

Run

	 cd /media/osboxes/VBox_GAs_6.1.28
	 sudo ./VBoxLinuxAdditions.run
	 sudo reboot

## config shared folder

这里我们可以把共享文件夹名称设置成：“virtualbox-shared”。

![](/images/tech/virtualbox-mount-shared-folder.png)

对于 Linux 系统，无需写 “挂载点”。

## Auto mount

Windows下，自动挂在。

Linux下，不会自动加载。这样操作手动加载：

	  cd ~/Desktop/
	  mkdir shared-folder
	  sudo mount -t vboxsf virtualbox-shared ~/Desktop/shared/

之后就行了。

如果权限出了问题，可以这样：

	sudo adduser $USER vboxsf
