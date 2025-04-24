---
title: Module-Level Configuration vs Pydantic-Based Configuration
category: unknown
tags: []
comments: true
date: 2025-04-25 01:35:11
---

# Module-Level Configuration

Defined at the top-level of a Python module (file), typically as global variables or constants. For example:

```python
# settings.py
API_KEY = 'your-key-here'
DEBUG = True
TIMEOUT = 30
```

Usage:

```python
from settings import API_KEY, DEBUG, TIMEOUT
```

# Pydantic-Based Configuration

Pydantic is a data validation and parsing library.

define config (or any data model) as a class with type annotations, validation, and parsing built-in.

```
from pydantic import BaseSettings

class Settings(BaseSettings):
    api_key: str
    debug: bool = False
    timeout: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
```
