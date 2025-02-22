---
title: Blocking/non-blocking in Python with async/await
date: 2024-12-01
tags:
---

# When to use async/await in Python

## TL;DR

Traditionally, use async/await in Python when we are doing IO-bound operations (e.g. HTTP requests, database queries, file operations, etc.).

Do not use async/await when we are doing CPU-bound operations (e.g. data processing, calculations, etc.).

## Conclusion

Use async for Non-Blocking IO:

```python
# Asynchronous operations prevent blocking the CPU during IO tasks.
import httpx

async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/data")
        return response.json()
```

Handle CPU-Bound Tasks with run_in_executor:

```python
# Offload CPU-intensive tasks to a separate thread to avoid blocking the event loop.
import asyncio

def compute_heavy_task():
    # CPU-intensive computation
    ...

async def handle_task():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, compute_heavy_task)
    return result
```

Consistency with async:
```python
# Define all endpoints as asynchronous for uniformity and future-proofing.
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```

Scalability and Maintenance:

```python
# Asynchronous code enhances scalability and maintains consistency across the codebase.
async def scalable_function():
    # Asynchronous logic for scalability
    ...
```

# References

[Dead Simple: When to Use Async in FastAPI](https://hughesadam87.medium.com/dead-simple-when-to-use-async-in-fastapi-0e3259acea6f)
