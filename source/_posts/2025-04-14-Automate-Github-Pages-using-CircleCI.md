---
title: CircleCI auto deploy Github Pages
category: unknown
tags: []
comments: true
date: 2025-04-14 04:40:37
---

CircleCI Script: 

CircleCI does not check out submodules. If your project requires submodules, modify script: 

(this does not work, I ended up hardcode theme and removed any submodules)

```
version: 2.1
orbs:
  node: circleci/node@5.1 # Use a more specific minor version

jobs:
  hexo_deploy:
    executor: node/default
    steps:
      - checkout
          submodules: true # This is the key line!
      
      - run: git submodule sync
      - run: git submodule update --init

      - node/install-packages:
          cache-path: node_modules # Simplified cache path
          override-ci-command: npm install

      - run:
          name: Install Hexo CLI
          command: npm install -g hexo-cli # Removed sudo

      - run:
          name: Clean public folder
          command: rm -rf public # Added clean step

      - run:
          name: Generate Hexo Site
          command: hexo generate

      - run:
          name: Install gh-pages package
          command: npm install gh-pages --save-dev

      - run:
          name: Configure Git
          command: |
            git config --global user.email "ci-build@circleci.com"
            git config --global user.name "CircleCI Build"

      - run:
          name: Deploy to GitHub Pages
          command: |
            npx gh-pages -d public -b gh-pages -m "Build generated [skip ci]"

workflows:
  version: 2
  build-and-deploy:
    jobs:
      - hexo_deploy
```
