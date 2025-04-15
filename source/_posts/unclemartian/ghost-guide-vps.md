---
title: 【Tech】 Quick setup guide of Ghost on VPS
category: unknown
tags: technology
comments: true
date: 2015-04-27 00:00:00
---


# Motivation

Recently I figured [__Ghost__, just a blogging platform](https://ghost.org/) a pretty cool stuff. 

So I got myself a free account from a VPS provider with Ubuntu 14.04 installed and jumped right in. 

# Setup 

## download and install

    wget https://ghost.org/zip/ghost-latest.zip
    unzip -d ghost-folder ghost-zip

## set dependency

    ch ghost-folder
    sudo npm install —-production

## config

    cp config.example.js config.js  
    nano config.js

Now change the url of production to the public IP or domain name. 

## start ghost

    npm start —-production

# Configurations

to be continued..
