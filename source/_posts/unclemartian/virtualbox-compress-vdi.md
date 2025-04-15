---
title: 【Tech】 How to compress VDI file for VirtualBox
category: unknown
tags: ubuntu
comments: true
date: 2020-12-01 00:00:00
---


# Problem

The growing VirtualBox VDI file is very annoying. 

以下是压缩 vdi 文件的方法。

## On linux VM

Run

	 dd if=/dev/zero of=/var/tmp/bigemptyfile bs=4096k ; rm /var/tmp/bigemptyfile

## On windows host

Run

	cd 'C:\Program Files\Oracle\VirtualBox\'
	
	.\VBoxManage.exe modifymedium --compact D:\VMs\abc.vdi

Done.

# Reference

https://superuser.com/questions/529149/how-to-compact-virtualboxs-vdi-file-size
