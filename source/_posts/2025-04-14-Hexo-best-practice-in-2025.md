---
title: Hexo best practice in 2025
category: unknown
tags: []
comments: true
date: 2025-04-14 05:02:19
---

# Change _config.yml:

```
new_post_name: :year-:month-:day-:title.md
```

After this change, your default file name becomes `2025-04-14-Hexo-best-practice-in-2025` instead of `Hexo-best-practice-in-2025`

# Deploy

## CircleCI

Config:

```
version: 2.1
orbs:
  node: circleci/node@5.1 # Use a more specific minor version

jobs:
  hexo_deploy:
    executor: node/default
    steps:
      - checkout
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

Pipeline:

https://app.circleci.com/pipelines/circleci/FxEGXAp1cq3kkmTWi4tCSt


## TravisCI

Deprecated already since Travis stopped their free plan, but put config here for archiving:

```
sudo: false
language: node_js
node_js:
  - 22
cache: npm
branches:
  only:
    - hexo-source # build master branch only
script:
  - hexo generate # generate static files
deploy:
  provider: pages
  skip-cleanup: true
  github-token: $GITHUB_TOKEN
  keep-history: true
  target_branch: master # generate static files to master
  on:
#   branch: main
    branch: hexo-source
  local-dir: public
```
