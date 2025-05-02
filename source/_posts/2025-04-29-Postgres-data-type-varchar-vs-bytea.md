---
title: Postgres data type varchar vs bytea
category: unknown
tags: []
comments: true
date: 2025-04-29 20:25:57
---

I need to store some hash value with SHA-256 encryption. 

> SHA-256
>
> a cryptographic hash function that produces a **256-bit hash value** from any input data.

Whatr Data Type should I use? 

## Calculation

Base-16 = 十六进制 = Hexadecimal

Each hex digit can have 16 possible values (0-9, A-F), represented by 4 bits (2^4 = 16).

So, to store a 256-bit hash value, we need 32 bytes * 8 = 256-bit.

## BYTEA

For PostgreSQL raw output of SHA-256, it's exactly 32 bytes. Total bits: 32 × 8 = 256 bits.

This is clean and compact, no storage overhead.

## VARCHAR(64)

When storing hex string as text (e.g., "b1a89231..."), each char is a digit (using standard ASCII/UTF-8). 

So a 64-character hex string is 64 bytes. Thus VARCHAR(64)

# Conclusion

BYTEA: Use for best storage efficiency. Store the plain binary hash. (32bytes)

VARCHAR(64): if you need a hex string for human readability, it consumes twice the space. (64bytes)
