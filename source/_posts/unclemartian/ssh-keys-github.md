---
title: 【Tech】 SSH keys setup for GitHub
category: unknown
tags: technology
comments: true
date: 2015-05-14 00:00:00
---


# Setup for the first Github

This is the standard procedure for generating SSH and connect to GitHub:

check current SSH:

    ls -al ~/.ssh

generate new:

    ssh-keygen -t rsa -b 4096 -C "theimmortalfish@gmail.com"

(-t for type, -b for number of bits, -C for comment)

__then press Enter__, then set passphrase.

set SSH-agent:

    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_rsa

add SSH to GitHub:

    pbcopy < ~/.ssh/id_rsa.pub

put it into GitHub settings

test SSH:

    ssh -T git@github.com

# Setup for the second Github

## generate a second SSH key

Same steps untli the "__then press Enter__", we'll instead give it another name like "id\_rsa\_fish":

    Fishs-MacBook-Pro:.ssh Fish$ ssh-keygen -t rsa -b 4096 -C "theimmortalfish@gmail.com"
    Generating public/private rsa key pair.
    Enter file in which to save the key (/Users/Fish/.ssh/id_rsa): id_rsa_fish
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in id_rsa_fish.
    Your public key has been saved in id_rsa_fish.pub.
    The key fingerprint is:
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx theimmortalfish@gmail.com
    The key's randomart image is:
    +--[ RSA 4096]----+
    |       xxxxx     |
    |       xxxxx     |
    |       xxxxx     |
    |       xxxxx     |
    |       xxxxx     |
    |       xxxxx     |
    |       xxxxx     |
    |       xxxxx     |
    |       xxxxx     |
    +-----------------+
    Fishs-MacBook-Pro:.ssh Fish$ ls -al ~/.ssh/
    total 40
    drwx------   7 Fish  staff   238 May 14 12:43 .
    drwxr-xr-x+ 45 Fish  staff  1530 May 13 23:01 ..
    -rw-------   1 Fish  staff  1766 Jul 28  2014 id_rsa
    -rw-r--r--   1 Fish  staff   402 Jul 28  2014 id_rsa.pub
    -rw-------   1 Fish  staff  3326 May 14 12:43 id_rsa_fish
    -rw-r--r--   1 Fish  staff   751 May 14 12:43 id_rsa_fish.pub
    -rw-r--r--   1 Fish  staff  2828 May 13 22:47 known_hosts

Again, we'll do

    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_rsa_fish

And also, add public key to the second GitHub account. 

## SSH configuration

Now this is the key step: go to .ssh folder and __create a config file__: 

    touch config

And put in the following configuration:

    Host github-old
      HostName github.com
      User git
      IdentityFile ~/.ssh/id_rsa

    Host github.com
      HostName github.com
      User git
      IdentityFile ~/.ssh/id_rsa_fish

Depending on your preference, change one of the host from "github.com" to some other names. In my case, I give the name "github-old" to my first SSH, and the second one would just stay the same (cuz I use the second GitHub more frequently). 

The next step is the most important!

## configure ssh-agent

Now restart your ssh-agent:

    killall ssh-agent; eval `ssh-agent -s`

Now if you give it a try, you notice something fishy:

    ssh -T git@github.com

    ssh -T git@github-old

You notice that only the default SSH key (id\_rsa) is being used. You are essentially querying the same GitHub account. 

__This is wrong__. Because we have not added both SSH keys to ssh-agent yet. Immediately, do this: 

    ssh-add ~/.ssh/id_rsa_fish

    ssh-add ~/.ssh/id_rsa

Now if you test connection again, you shall see no problem. 

## Last step, change remote url

The last step is to make changes to the git repository so that your computer works with both GitHub account. 

Whenever we clone or "remote add origin", we shall replace "github-old" with "github.com" in the remote url. 

Example: go to your first GitHub account and create a new repo called "hello". Then,

    mkdir hello
    cd hello
    git init
    git remote add origin git@github-old:old-name/hello.git
    touch testing-file.txt
    git add .
    git commit -m 'first commit'
    git push origin master

You should see it works fine. Notice how we changed the remote url from "github.com" to "github-old", which matches our host configuration in the .ssh folder. 

Your second GitHub shall work just like a normal GitHub account. 3 hours of hard work, all done! 

Thanks to [Jeffrey Way from tutsplus.com](http://code.tutsplus.com/tutorials/how-to-work-with-github-and-multiple-accounts--net-22574) for the nice tutorial. 