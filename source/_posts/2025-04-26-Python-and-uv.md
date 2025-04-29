---
title: Python and uv
category: unknown
tags: []
comments: true
date: 2025-04-26 09:46:21
---

Properly install Python on Mac OS:

```
brew install python
```

Homebrew recommends modifying the ~/.zprofile file by adding the following line as the last line in the ~/.zprofile file:

```
export PATH="$(brew --prefix python)/libexec/bin:$PATH"
```

Check current Python versions:

`uv python list`

To run a specifc version of python:

```
uvx python@3.12 -c "print('hello world')"
```

(if the version you specify does not exist, uv will install it for you)

Remove a python version using uv:

```
uv python uninstall cpython-3.11.12-macos-x86_64-none
```

