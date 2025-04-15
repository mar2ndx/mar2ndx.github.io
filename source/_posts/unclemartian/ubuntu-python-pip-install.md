---
title: 【Tech】 Install Python/pip on Ubuntu 20.04
category: unknown
tags: ubuntu
comments: true
date: 2021-09-04 00:00:00
---


# Installation

Replace python2 with python3: 

    python --version 
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.8
    python --version 
    which python3
    sudo apt install python-is-python3

## Updated March 2022

其实可以直接跑这个，安装最新版 python （as of this writing, latest stable is v3.9.2）:

    sudo apt install python3 python3-pip

Got:

    chrx@penguin:~/$ python3 --version
    Python 3.9.2
    chrx@penguin:~/$ pip --version 
    pip 20.3.4 from /usr/lib/python3/dist-packages/pip (python 3.9)

Reference: https://www.how2shout.com/linux/install-python-3-x-or-2-7-on-debian-11-bullseye-linux/

## pip

To install pip on python3:

    python --version 
    pip
    pip3
    sudo apt install python3-pip
    pip
    pip --version 

Now you have python3 and pip installed on Ubuntu. 
