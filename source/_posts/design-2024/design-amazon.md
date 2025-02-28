---
title: System Design 2024 - Amazon
category: Design
tags: []
comments: true
date: 2024-09-25 23:03
---


# Design Amazon

# 1. Requirements

1. 350 million products
1. 10 million orders per day, that's 100 orders per second
1. 1 MB of data per product, that is 1 PB needed to partition the product table. 

## Features

1. retail
2. concurrent edit of cart
3. inventory mgmt (out of stock monitor)

# 2. ProductDB

1. partition as much as possible
2. only 1 person write at 1 time
3. NoSQL, eg. MongoDB.



Reference：https://www.youtube.com/watch?v=F9lcK1jnAcs