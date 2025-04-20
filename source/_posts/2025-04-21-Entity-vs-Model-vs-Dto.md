---
title: Entity vs Model vs Dto
category: unknown
tags: []
comments: true
date: 2025-04-21 04:09:31
---

# Core Concepts

1. Entities: Database-focused objects that represent tables/collections
1. Domain Models: Business logic containers with rules and behaviors
1. DTOs: Data carriers optimized for specific interfaces and operations

```
Database ⟷ Entities ⟷ Domain Models ⟷ DTOs ⟷ Client/API
```

# Details

Entities

1. Persistence-oriented
1. ORM/database annotations
1. Database relations and constraints
1. Example: UserEntity with JPA annotations mapping to user table

Domain Models

1. Business logic-oriented
1. Behavior and validation rules
1. Independent of persistence mechanisms
1. Example: User with methods like isEligibleForDiscount()

DTOs

1. Transfer-oriented
1. Purpose-specific shapes
1. Simple data containers
1. Example: UserProfileDto with only public-facing user information

## When Data Crosses Boundaries

* Repository Layer: Converts database rows to Entities
* Service Layer: Maps between Entities and Domain Models
* Controller/API Layer: Transforms Domain Models to/from DTOs

## Chart

![](/images/Entity-vs-Model-vs-Dto.png)

### Read Path (Database to Client)

1. Database Layer: Raw data exists as rows/documents
1. Repository Layer: Converts database rows into Entity objects
1. Service Layer: Maps Entities to Domain Models and applies business logic
1. Controller/API Layer: Transforms Domain Models to DTOs for external consumption
1. Client: Receives serialized DTOs (typically as JSON/XML)

### Write Path (Client to Database)

1. Client: Sends data (typically JSON/XML)
1. Controller/API Layer: Deserializes into DTOs and validates input
1. Service Layer: Converts DTOs to Domain Models and applies business rules
1. Repository Layer: Transforms Domain Models to Entities
1. Database Layer: Persists Entities as database rows/documents
