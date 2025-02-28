---
title: "[Design] Virtual Memory, Page Fault and Thrashing"
category: Design
tags: []
comments: true
date: 2014-08-26 00:00
---


### Terminologies

#### Paging

[Paging](http://whatis.techtarget.com/definition/paging) is a method of writing data to, and reading it from, **secondary storage** for use in **primary storage**, also known as main memory. Paging plays a role in memory management for a operating system.

#### Page table

[A page table](http://en.wikipedia.org/wiki/Page_table) is the data structure used by a virtual memory system to store the mapping between **virtual addresses** and **physical addresses**.

#### Page fault

A [page fault](http://en.wikipedia.org/wiki/Page_fault) is a trap to the software raised by the hardware when a program **accesses a page that is mapped in the virtual address space**, but **not loaded in physical memory**. In the typical case the operating system tries to handle the page fault by making the required page accessible at a location in physical memory or terminates the program in the case of an illegal access.

An **invalid page fault** or **page fault error** occurs when the operating system cannot find the data in virtual memory. This usually happens when the virtual memory area, or the table that maps virtual addresses to real addresses, becomes corrupt.

#### Logical address

[Logical address](http://en.wikipedia.org/wiki/Logical_address) is the address at which an item (memory cell, storage element, network host) appears to reside from the perspective of an executing application program.

#### Physical address

[Physical address](http://en.wikipedia.org/wiki/Physical_address) (also real address, or binary address), is a memory address that is represented in the form of a binary number for accessing main memory.

[In general](http://www.geekinterview.com/question_details/3186), Logical address is the address generated **by the CPU**. Where as physical address is the **actual address of the process in the memory**. The CPU generates the logical address that is added with the **offset value** to get the actual address of the process inthe memory.

#### Thrashing

[Thrashing](http://www.computerhope.com/jargon/t/thrash.htm) or disk thrashing is a term used to describe when the hard drive is **being overworked by moving information** between the system memory and virtual memory excessively.

### Demand Paging

Virtual memory is implemented (mostly) using demand paging. **[Demand Paging](http://www.webopedia.com/TERM/D/demand_paging.html)** is a type of swapping in which pages of data are not copied from disk to RAM until they are needed. This is an example of a [lazy loading technique](http://en.wikipedia.org/wiki/Demand_paging).

Pros:

1. less RAM needed
1. more users
1. less I/O

When a pages is needed, if **invalid referernce**, abort the process. else **if valid**, it's called page fault.

Page fault time:

1. servicing the page fault interrupt
1. read in new page (major part)
1. restart the process

### Page Replacement

1. FIFO
2. Optimal Algorithm
3. LRU
4. LRU Approximation
   1. Additional-Reference-Bits algorithm
   2. Second-Chance (Clock) algorithm

Refer to another post **"Cache and Page Replacement Algorithms"**.

### Solution to Thrashing

1. More RAM
1. Less program running together
1. Assign working priorities
1. Improve [spatial locality](<http://en.wikipedia.org/wiki/Thrashing_(computer_science)#Solutions>) by replacing loops, i.e.

Replace

    // recall that in C, arrays use Row-major order
    int m[256][256];
    for (k=0; k<256; k++) {
    	for (i=0; i<256; i++) {
    		m[i][k] = something();
    	}
    }

with

    int m[256][256];
    for (i=0; i<256; i++) {
    	for (k=0; k<256; k++) {
    		// consecutive values of k reside in adjacent memory locations
    		m[i][k] = something();
    	}
    }

So that the use of data elements is within relatively [close storage locations](http://en.wikipedia.org/wiki/Locality_of_reference).
