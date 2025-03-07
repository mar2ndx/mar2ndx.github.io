---
title: "[Design] Database Indexing "
category: Design
tags: []
comments: true
date: 2014-12-27 00:00
---


[ref 1](http://stackoverflow.com/a/1130) [ref 2](http://www.interspire.com/content/2006/02/15/introduction-to-database-indexes/)

### Why Indexing?

In database disks (we're talking about disk-based storage devices), data is stored as blocks. These blocks are accessed atomically. It's like a linked list with pointers to the blocks.

Because of this, searching in database is linear time. That's why we need indexing.

**Indexing is a way of sorting a number of records on multiple fields**. Creating an index on a field in a table creates another data structure which holds the field value, and pointer to the record it relates to. This index structure is then sorted, allowing Binary Searches to be performed on it.

In other words, indexing speed up search.

### Downside

First disadvantage is **the additional space usage**. For example, in MyISAM engine, indexes are stored together with the data in one table. So the indexing files can quickly reach the size limits if many fields are indexed.

Second disadvantage is that **using too many indexes can actually slow your database down**. Each time a page or database row is updated or removed, the reference or index also has to be updated.

So indexes speed up finding data, but slow down inserting, updating or deleting data.

### Primary keys

**Some fields are automatically indexed**.

A primary key or a field marked as ‘unique’ – for example an email address, a userid or a social security number – are **automatically indexed** so the database can quickly check to make sure that you’re not going to introduce bad data.

### When to use

Since indexes are **only** used to speed up the searching, it's not wise to have indexing used only for output.

**The general rule** is, anything that is used to limit the number of results you’re trying to find. For more details, read [ref 2](http://www.interspire.com/content/2006/02/15/introduction-to-database-indexes/).

### How to create index

[The following](http://stackoverflow.com/a/1157) is SQL92 standard that's supported by major RDMBSs:

    CREATE INDEX [index name] ON [table name] ( [column name] )
