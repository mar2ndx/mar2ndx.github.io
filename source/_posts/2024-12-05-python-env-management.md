---
title: Python environment management
category: unknown
tags:
comments: true
date: 2024-12-05
---

## TL;DR

* Want simplicity? Use venv.
* Want to look cool in front of your team? Use Poetry.
* Stuck in a conservative workplace or older project? Go Pipenv.
* Need data science tools? Embrace Conda.

# Difference

## pipenv

Pipenv is a tool that only manage dependency, and automatically create a virtual environment.

You manage dependencies with __Pipfile and Pipfile.lock__, and it works well if you also maintain requirements.txt files.

## Poetry

Poetry is designed to handle dependencies, packaging, and project setup in one tool. 

You manage dependencies with __pyproject.toml files__, which are becoming a standard in Python projects.
