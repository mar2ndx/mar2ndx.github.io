---
title: One-line launch anything from Mac OS
date: 2024-12-01
tags:
---

# One-line Launch Next.js and FastAPI

Consider you have a monorepo with Next.js frontend and FastAPI backend:

```
gitww/
├── backend-fastapi/
├── frontend-nextjs/
```

## 1. Run Backend (FastAPI)

`run-backend.sh`

```bash
echo -ne "\033]0;gitww-backend\007"
cd /usr/local/hub/gitww/backend-fastapi
docker compose up -d
poetry install
poetry run uvicorn app.main:app --host 0.0.0.0 --port 3463 --reload
```

## 2. Run Frontend (Next.js)

`run-frontend.sh`

```bash
echo -ne "\033]0;gitww-frontend\007"
cd /usr/local/hub/gitww/frontend-nextjs
pnpm install
pnpm dev
```
### Permissions

You must add 'x' permission to the scripts, in order to run on Mac:

```bash
chmod +x /usr/local/hub/gitww/backend-fastapi/run-backend.sh
chmod +x /usr/local/hub/gitww/frontend-nextjs/run-frontend.sh
```

Now, test:

```bash
open -a iTerm /usr/local/hub/gitww/frontend-nextjs/run-frontend.sh \
& open -a iTerm /usr/local/hub/gitww/backend-fastapi/run-backend.sh
```

Important to note that, **you launched 2 iTerm with 1 line, with the help of `&`.**

## 3. One-line Launch

Make a top-level script:

`run-gitww.sh`

```bash
cursor /usr/local/hub/gitww/ \
& open -a iTerm /usr/local/hub/gitww/frontend-nextjs/run-frontend.sh \
& open -a iTerm /usr/local/hub/gitww/backend-fastapi/run-backend.sh \
& open "http://localhost:3462/"
```

## 4. Alias

Edit your `vi ~/.zshrc` or `vi ~/.bashrc`:

```bash
alias gitww="zsh /usr/local/hub/gitww/run-gitww.sh"
```

Or, if you don't mind long command:

```bash
alias gitww="cursor /usr/local/hub/gitww/ && open -a iTerm /usr/local/hub/gitww/frontend-nextjs/run-frontend.sh && open -a iTerm /usr/local/hub/gitww/backend-fastapi/run-backend.sh && open 'http://localhost:3462/'"
```

Now, simply run `gitww` to launch frontend, backend, Chrome, and Cursor.

# Final Notes

`&` = run parallelly.

* `run-gitww.sh` must be **1-line command with `&` concatenation**. 
  * Need everything to be launched simultaneously.

* `run-backend.sh` and `run-frontend.sh` are multi-step commands
  * It's mimicing a human's workflow.
