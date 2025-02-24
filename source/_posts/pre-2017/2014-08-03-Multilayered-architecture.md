---
layout: post
title: "[Design] Multilayered architecture"
comments: true
category: Design
---

### First Word

A [multilayered software architecture](http://en.wikipedia.org/wiki/Multilayered_architecture) is a software architecture that uses many layers for allocating the different responsibilities of a software product.

### Layers

1. **Presentation layer**
   a. UI layer, view layer
   a. presentation tier in multitier architecture
1. **Application layer**
   a. also called service layer/GRASP Controller Layer
1. **Business layer**
   a. also called business logic layer/domain layer
1. Infrastructure layer
   1. data access layer/**persistence layer**
   1. logging, networking, and other services which are required to support a particular business layer

### Conventions

**Application layer** (or service layer) is sometimes considered a sublayer of **business layer**.

If there's no explicit distinction between first 3 tiers, then it's a **traditional client-server(two-tier) model**.

The **application/business layers** can, in fact, be further subdivided to emphasize distinct responsibility (eg. MVC).

Sometimes there's **business infrastructure layer(BI)**, located between the business layer and infrastructure layer.

Infrastructure layer can be partitioned into different levels (high-level or low-level). **Developers focus on only the persistence capabilities**, therefore only talk about persistence layer or data access layer.
