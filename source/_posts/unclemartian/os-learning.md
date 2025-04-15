---
title: 【Tech】Operating System learning notes
category: unknown
tags: technology
comments: true
date: 2015-08-10 00:00:00
---


# Definition

## Top-down: hardware abstraction layer

__Turn hardware into something that applications can use__. “standard library” “OS as virtual machine”

1. eg. printf(“hello world”), shows up on screen, App issue system calls to use OS abstractions

1. eg. each app doesn’t have to write a graphics driver.

1. eg. consistent interface: support for scsi/ide/flash disks

## Bottom-up: resource manager/coordinator

Manage your computer’s resources. Resource = CPU, Memory, disk, device, bandwidth... 

1. sharing/multiplexing more than 1 app.

1. protect, who gets what when.

1. performance: fair and efficient.

# OS abstraction: Process

A key OS abstraction: the applications you use are
built of processes. 

## Processes are protected from each other

__In computing, a [virtual address space (VAS)](https://en.wikipedia.org/wiki/Virtual_address_space) or address space__ is the set of ranges of virtual addresses that an operating system makes available to a process.

This provides several benefits, one of which is, if each process is given a separate address space, __security through process isolation__.

## Unix process-related system calls

    int fork(void) 

create a copy of the invoking process

    int execv (const char* prog, const char* argv[]) 

replace current process with a new one

    int wait(int *status) 

wait for a child to exit

## process communication: pipe

    int pipe(int fds[2])

1. Creates a one way communication channel

1. fds[2] is used to return two file descriptors

1. Bytes written to fds[1] will be read from fds[0]

# Kernel: most interesting part of OS

Unix System Architecture: 

{<1>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-07-25%20at%2010.14.54%20PM.png)

## virtual machine

Export a fake hardware interface so that
multiple OS can run on top.

{<2>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-07-25%20at%2010.39.50%20PM.png)


## batch processing

ordered, bad but high utilization

## spooling

> The most common spooling application is print spooling. In print spooling, documents are loaded into a buffer (usually an area on a disk), and then the printer pulls them off the buffer at its own rate. 

> Because the documents are in a buffer where they can be accessed by the printer, you can perform other operations on the computer while the printing takes place in the background. 

## Multiprogramming

Several programs are run at the same time __on a uniprocessor__. Since there is only one processor , there can be no true simultaneous execution of different programs. Instead, the operating system executes part of one program, then part of another. 

OS chooses which to run.

Ref: http://www.cs.columbia.edu/~junfeng/13fa-w4118/lectures/l02-os-intro.pdf

