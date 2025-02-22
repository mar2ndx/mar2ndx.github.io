---
title: How to deploy to Github pages in Year 2025
date: 2025-02-23 01:35:43
tags:
---

I have a love-hate relationship with Github Pages. 

For it's free, stable and deployed automatic with git, but also for it's complexity when switching laptops, and its inaccessibility in mainland China. 

Here's how to do it anyways:

## Setup a Hexo

    pnpm install -g hexo
    hexo --version
    hexo init tech-blog
    cd tech-blog/
    pnpm i
    hexo server
    cd themes/
    git clone https://github.com/xbmlz/hexo-theme-maple.git maple

Change blog config at: ./_config.yml

## Commit master

    git remote add origin https://github.com/mar2ndx/mar2ndx.github.io.git
    git push -u origin master

This would fail, you need to go to https://github.com/settings/personal-access-tokens and add a new access token.

You need to choose __Repository permissions__ and __Account permissions__.

![](/images/github-pages-1-access-token-github.png)

Choose "Contents" and "Pages" under __Repository permissions__. Nothing under __Account permissions__.

Then change remote origin like this:


    git remote set-url origin https://the_user_name:the_github_token@github.com/mar2ndx/mar2ndx.github.io.git
    git push -u origin master


## Commit gh-pages

Change config first:

    deploy:
    type: git
    repo: https://github.com/mar2ndx/mar2ndx.github.io.git
    branch: gh-pages

Install [hexo-deployer-git](https://github.com/hexojs/hexo-deployer-git):

    pnpm install hexo-deployer-git --save

Should work now:

    hexo clean
    hexo g
    hexo d

![](/images/github-pages-2-hexo-deploy.png)

Lastly, change the deploy branch at https://github.com/mar2ndx/mar2ndx.github.io/settings/pages

![](/images/github-pages-3-pages-source-branch.png)
