---
title: 【Tech】 Install Node/npm using Nvm
category: unknown
tags: ubuntu
comments: true
date: 2021-09-01 00:00:00
---


# Install Node.js using nvm

Use 'nvm' to manage node versions

## Bash Install

1. Install nvm thru [nvm bash](https://github.com/nvm-sh/nvm#install--update-script)
    
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
	
    Or:

	    wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

    Or (from this blog):

	    wget -qO- https://mar2ndx.github.io/files/nvm-0391-install.sh | bash

1. You may be stuck here, right after you saw this:

        => Downloading nvm from git to '/home/ubuntu/.nvm'
        => Cloning into '/home/ubuntu/.nvm'...
        remote: Enumerating objects: 354, done.
        remote: Counting objects: 100% (354/354), done.
        remote: Compressing objects: 100% (302/302), done.
        remote: Total 354 (delta 40), reused 156 (delta 27), pack-reused 0
        Receiving objects: 100% (354/354), 207.03 KiB | 2.52 MiB/s, done.
        Resolving deltas: 100% (40/40), done.

1. Wait patiently for a bit. If still no luck, manually paste this to ~/.bashrc

        export NVM_DIR="$HOME/.nvm"
        [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
        [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

1. Run the following. You are all set!

        source ~/.bashrc

## Alternative: Git Install

Bash install might fail for network reasons. 

Thus do this: 

    cd ~/ from anywhere then git clone https://github.com/nvm-sh/nvm.git .nvm
    cd ~/.nvm and check out the latest version with git checkout v0.39.1
    activate nvm by sourcing it from your shell: . ./nvm.sh

    Now add these lines to your ~/.bashrc, ~/.profile, or ~/.zshrc file to have it automatically sourced upon login: (you may have to add to more than one of the above files)

    export NVM_DIR="$HOME/.nvm"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

Reference: https://github.com/nvm-sh/nvm#git-install

## Basic Usage

1. Check current node versions

        nvm ls
        nvm ls-remote

1. Install node and npm

        nvm install v12

1. Use the following command

        nvm use 12

## Please Note

You may need to uninstall the system version node/npm, otherwise sudo have issues.

A pretty simple work-around would be:

    sudo vi ~/.bashrc

Content：

    alias node='$NVM_BIN/node'
    alias npm='$NVM_BIN/npm'
    alias sudo='sudo env PATH=$PATH:$NVM_BIN'

# Change node registry to taobao

    npm config get registry
    npm config set registry https://registry.npm.taobao.org/
    npm config set registry https://registry.npmjs.org/

## To check

    npm info underscore
    npm --registry https://registry.npm.taobao.org info underscore
    npm config get registry

# Useful npm packages

You might need to install these just in case you need them:

    npm install -g eslint yarn @vue/cli
    npm install -g npx
    npm install -g now truffle
    npm install -g hexo-cli

To check your globally-installed packges:

    npm list -g --depth 0
