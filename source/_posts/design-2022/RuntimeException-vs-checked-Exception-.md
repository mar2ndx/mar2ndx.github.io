---
title: RuntimeException and checked Exception
category: Design
tags: []
comments: true
date: 2022-12-01 21:57
---


Java Exceptions are divided into 2 categories:

1. RuntimeException (also known as **unchecked Exception**) 
2. Checked Exception

# Checked exception

1. mandatory to try... catch...
2. otherwise: compile error

eg. ClassNotFoundException, IOException, SQLException and ParseException

# Unchecked exception

same as RuntimeException. 

eg. NullPointerException, ArrayIndexOutOfBoundException, IllegalArgumentException
