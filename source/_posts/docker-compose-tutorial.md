---
title: Docker compose tutorial
date: 2024-12-03
tags:
---

Let's start with a simple example.

## Example 1: Postgres

`docker-compose.yml`:

```yaml
version: '3.8'

name: project_name # Container Name
services:
  postgres: # Service Name
    image: postgres:latest
    container_name: dushexuezhang-postgres # This isn't important
    environment:
      POSTGRES_USER: TODO
      POSTGRES_PASSWORD: TODO
      POSTGRES_DB: TODO
    ports:
      - "5458:5432"
    volumes:
      - persist_data:/var/lib/postgresql/data
    restart: unless-stopped

volumes:
  persist_data:
    name: dushe_postgres_data # This can be shared between containers
    driver: local
```

Note that:

1. Make sure to set `name`, otherwise, Docker will use folder name as container name.
1. `postgres` is the service name, displayed under 'project_name' in Docker Desktop. A container can have multiple services.
1. ports: <local_port>:<container_port>, that means your postgres runs on localhost:5458.
1. volumes is used to persist data.
    * `persist_data` is an identifier for the volume. It's like an alias.
    * `name` is the actual name of the Docker volume, which will be displayed in Docker Desktop. 

## On Volume name

If you do not specify a `name`, Docker will use `[project_name]_[service_name]_data` as the volume name. For example, `dushexuezhang_postgres_data`. So, I recommend setting a `name` for your volume.

If you reuse the same `name` as another container, Docker will reuse the same volume, essentially you get same DB data.

## Docker commands

To see all containers, run `docker ps`.

To see all images, run `docker images`.

To see all volumes, run `docker volume ls`.

To remove orphaned volumes, run `docker volume prune`.
