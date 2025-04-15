---
title: 【Tech】 Git Learning Notes
category: unknown
tags: technology
comments: true
date: 2015-04-26 00:00:00
---


# git remote

__Remote connections are more like bookmarks__. 

git remote command is really just an easier way to pass URLs.

When you clone a repository with git clone, it automatically creates a remote connection called __origin__.

# git fetch

The git fetch command imports commits from a remote repository into your local repo

The resulting commits are __stored as remote branches__ instead of the normal local branches

Fetching is what you do when you want to see what everybody else has been working on. Since fetched content is represented as a remote branch, it has absolutely no effect on your local development work.

## Remote branches

Remote branches are just like local branches, except they represent commits from somebody else’s repository. You can check out a remote branch just like a local one, but this __puts you in a detached HEAD state__ (just like checking out an old commit). You can think of them as __read-only branches__.

# git pull

This is the same as 

    git fetch <remote> 

followed by 

    git merge origin/<current-branch>

## alternative

    git pull --rebase <remote> 
    (eg. git pull --rebase origin)

Same as the above command, but __instead of using git merge__ to integrate the remote branch with the local one, use __git rebase__.

## rebase

--rebase option can be used to ensure a linear history by preventing unnecessary merge commits.

In fact, pulling with --rebase is such a common workflow that there is a dedicated configuration option for it:

    git config --global branch.autosetuprebase always

# git push

After you’re ready to share your commits with others, you (optionally) __clean them up with an interactive rebase__, then push them to the central repository.

You should only push to repositories that have been created with the __--bare flag__. It’s important to __never push to another developer’s repository__.

## Example

The following example describes one of the __standard methods__ for publishing local contributions to the central repository.

    git checkout master
    git fetch origin master
    git rebase -i origin/master
    # Squash commits, fix up commit messages etc.
    git push origin master

reference: [Atlassian Tutorials on Git](https://www.atlassian.com/git/tutorials/syncing)

# Pull request

__pull requests__ are a mechanism for a developer to notify team members that they have completed a feature. 

But, the pull request is more than just a notification—it’s a dedicated forum for discussing the proposed feature. If there are any problems with the changes, teammates can post feedback in the pull request.

## pull-request anatomy

You will need to provide 4 pieces of information to file a pull request: 

1. the source repository, 
1. the source branch, 
1. the destination repository, 
1. the destination branch.

# Example Process

Pull requests can be used in conjunction with the Feature Branch Workflow, the Gitflow Workflow, or the Forking Workflow. But a pull request requires either two distinct branches or two distinct repositories, so they will not work with the Centralized Workflow. 

1. A developer creates the feature in a dedicated branch in their local repo.

1. The developer pushes the branch to a public Bitbucket repository.

1. The developer files a pull request via Bitbucket.
The rest of the team reviews the code, discusses it, and alters it.

1. The project maintainer merges the feature into the official repository and closes the pull request.

reference: [Atlassian Tutorials on Git](https://www.atlassian.com/git/tutorials/making-a-pull-request)

# git branch

__git branch__ is a way to request a brand new working directory, staging area, and project history. 

## Git Vs. SVN

Git branches is more lightweight than SVN’s. 

Instead of __copying files from directory to directory__, Git stores a branch __as a reference to a commit__. In this sense, a branch represents the tip of a series of commits — not a container for commits. 

## branch basics

    git branch

List all branches

    git branch <branch>

Create a new branch called <branch> (but don't checkout).

    git checkout -b <new-branch>

Create and check out <new-branch>. 

    git branch -d <branch>

Delete the specified branch (safe).

    git branch -D <branch>

Force delete the specified branch, even if it has unmerged changes. 

    git branch -m <branch>

Rename current branch to <branch>.

## Detached HEADs

Remember that the HEAD is Git’s way of referring to the current snapshot. 

Internally, __git checkout__ command simply updates the HEAD to point to either the __specified branch or commit__.

When it points to a branch, Git doesn't complain, but __when you check out a commit__, it switches into a “detached HEAD” state.

{<1>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen-Shot-2015-05-11-at-8-53-09-PM.png)

If you were to start developing a feature while in a detached HEAD state, there would be no branch allowing you to get back to it.

However, if you’re just looking at an old commit, it doesn’t really matter if you’re in a detached HEAD state or not.

# git merge

## merge basics

    git merge <branch>

Merge the branch into the current branch. 

    git merge --no-ff <branch>

Merge the branch into the current branch, but always generate a merge commit (even if it was a fast-forward merge).

## fast forward

A fast-forward merge can occur when there is a linear path from the current branch tip to the target branch. 

{<2>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen-Shot-2015-05-11-at-9-53-17-PM.png)

Instead of “actually” merging the branches, Git only moves the current branch tip up to the target branch tip. 

## 3-way merge

When there is not a linear path to the target branch, Git will do __3-way merge__. It use a dedicated commit to tie together the two histories. 

{<3>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen-Shot-2015-05-11-at-9-57-48-PM.png)

Three commits are used to generate the merge commit: 

1. two branch tips
1. their common ancestor.

## Conflicts

When both branches modify the same file, you'll resolve the conflicts manually. After that, do a normal commit. 

Note that merge conflicts will only occur in the event of a 3-way merge.

## Conventions

While you can use either of these merge strategies, many developers like to use fast-forward merges (facilitated through rebasing) for __small features__ or bug fixes, while reserving 3-way merges for the integration of __longer-running features__. 

In the latter case, the resulting merge commit serves as a symbolic joining of the two branches.

## Example

3-way merge

    # Start a new feature
    git checkout -b new-feature master

    # Edit some files
    git add <file>
    git commit -m "Start a feature"

    # Edit some files
    git add <file>
    git commit -m "Finish a feature"

    # Develop the master branch
    git checkout master

    # Edit some files
    git add <file>
    git commit -m "Make some super-stable changes to master"

    # Merge in the new-feature branch
    git merge new-feature
    git branch -d new-feature

reference: [Atlassian Tutorials on Git](https://www.atlassian.com/git/tutorials/using-branches)

#  Git workflows

Remember this is guidelines rather than concrete rules. We'll cover the first 3:

1. Centralized Workflow

1. Feature Branch Workflow

1. Gitflow Workflow

1. Forking Workflow

# Centralized Workflow

1. Each developer modify and commit into __master branch__.

1. After the change, __fetch__ the updated central commits.

1. __rebase__ their changes.

1. If local changes directly conflict with upstream commits, Git will __pause the rebasing__ and asks you to manually resolve the conflicts.

## example

Mary:

    git clone ssh://user@host/path/to/repo.git
    git status # View the state of the repo
    git add <some-file> # Stage a file
    git commit # Commit a file</some-file>
    git push origin master

Bill:

    git push origin master
    error: failed to push some refs to '/path/to/repo.git'
    hint: Updates were rejected because the tip of your current branch is behind
    hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')
    hint: before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.

Then, Bill would do:

    git pull --rebase origin master
    CONFLICT (content): Merge conflict in <some-file>
    # Unmerged paths:
    # (use "git reset HEAD <some-file>..." to unstage)
    # (use "git add/rm <some-file>..." as appropriate to mark resolution)
    #
    # both modified: <some-file>

Bill solve some conflicts, then

    git add <some-file>
    git rebase --continue
    ## after rebase successful,
    git push origin master

# Feature Branch Workflow

The core idea is that __all feature development take place in a dedicated branch__ instead of the master branch. So that:

1. a branch is a feature, having highly-focused purpose.

1. master branch will never contain broken code

1. possible to leverage __pull requests__

Note: Feature branches can and should be __pushed to the central repository__.

## pull request

Once someone completes a feature, they don’t immediately merge it into master.

Instead, they push feature branch to central server and __file a pull request__.

Code review shall happen here.

## example

Mary creates and checkout a branch if it doesn’t already exist (with -b):

    git checkout -b marys-feature master
    # edits, stages, and commits changes
    git status
    git add <some-file>
    git commit
    git push -u origin marys-feature

-u is used to add it as a remote tracking branch. Now her feature is finished, she'll do:

    git push

Then a pull request.

After the code review, Mary still can work on this branch like she did before, or even Bill can pull marys-feature into his local repository and work on it. Until the pull request is accepted, either Mary or Bill do:

    git checkout master
    git pull
    git pull origin marys-feature
    git push

{<1>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-05-15%20at%2011.18.54%20AM.png)

> __git pull origin marys-feature__ merges central repository’s copy of marys-feature to local master. (You could also use a simple __git merge marys-feature__, but the command shown above makes sure you’re always pulling the most up-to-date version of the feature branch.)

> If you find it hard to understand, read [Pull for another Git branch without switching, from superuser.com](http://superuser.com/a/163048):

    git checkout live
    git pull origin master

>> This will attempt a merge of the remote master and your live branch.

## discussion: merge vs. rebase

This process often results in a merge commit. Some developers like this because it’s like __a symbolic joining of the feature__ with the rest of the code base. But, if you’re partial to a linear history, it’s possible to __rebase the feature__ onto the tip of master before executing the merge, resulting in a fast-forward merge.

# Gitflow Workflow

Gitflow Workflow defines a __strict branching model__ designed around the project release. It assigns __very specific roles__ to different branches and defines how and when they should interact.

## master and develop

The master branch stores the official release history, and the develop branch serves as an integration branch for features.

__Tag all commits__ in the master branch with __a version number__.

## feature branches

Each new feature should reside in its own branch, which can be pushed to the central repository for backup/collaboration. But, instead of branching off of master, __feature branches use develop as their parent branch__.

> Note that feature branches combined with the develop branch is, for all intents and purposes, the __Feature Branch Workflow__.

{<2>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-05-15%20at%204.19.16%20PM.png)

> branch off: develop
>
> merge into: develop

## release branches

For release, you fork a release branch off of develop, and prepare:

1. bug fixes
1. documentation generation
1. other release-oriented tasks

__No new features__ can be added after this point.

Once ready for release, this branch will get __merged into master__ and tagged with a version number. In addition, it should be __merged back into develop__.

{<3>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-05-15%20at%204.27.35%20PM.png)

> branch off: develop
>
> merge into: master, develop
>
> naming convention: release-* or release/*

## hotfix branches

Maintenance or “hotfix” branches are used to quickly patch production releases.

This is the only branch that should __fork directly off of master__.

Once fixed, it's __merged into both master and develop__ (or the current release branch), and master should be tagged with an updated version number.

You can think of maintenance branches as ad hoc release branches that work directly with master.

{<4>}![](https://dl.dropboxusercontent.com/u/23764314/ghost_immortalfish/Screen%20Shot%202015-05-15%20at%204.32.26%20PM.png)

> branch off: master
>
> merge into: master, develop

## example

### create master and develop

    git branch develop
    git push -u origin develop

__develop__ will contain the complete history of the project, whereas __master__ will contain an abridged version.

Bill now clone the central repository and create a tracking branch for develop:

    git clone ssh://user@host/path/to/repo.git
    git checkout -b develop origin/develop

### develop stage

Now Mary and Bill both work on their own features:

    git checkout -b some-feature develop
    # make changes
    git status
    git add <some-file>
    git commit

Once Mary finishes a feature, she can do a pull request, or this:

    git pull origin develop
    git checkout develop
    git merge some-feature
    git push
    git branch -d some-feature

### release stage

While Bill is still working on his feature, Mary starts to prepare the first official release

    git checkout -b release-0.1 develop

She'll clean up the release, test everything, update the documentation. Now the release is feature-frozen.

Once the release is ready, Mary merges it into master and develop, then deletes the release branch. (can also do pull request here)

    git checkout master
    git merge release-0.1
    git push
    git checkout develop
    git merge release-0.1
    git push
    git branch -d release-0.1

When merging something into master, you should tag the commit for easy reference:

    git tag -a 0.1 -m "Initial public release" master
    git push --tags

### maintenance stage

If a bug is found:

    git checkout -b issue-#001 master
    # Fix the bug
    git checkout master
    git merge issue-#001
    git push

Then include it in develop, and delete the branch:

    git checkout develop
    git merge issue-#001
    git push
    git branch -d issue-#001

# Final note on workflows

They are not hard-and-fast rules for using Git in the workplace. So, don't be afraid to adopt some aspects of a workflow and disregard others. The goal should always be to make Git work for you, not the other way around.

Reference: [Comparing Workflows by atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows)

# Forking

We have discussed about Centralized, Feature branch & Gitflow in [previous post](/git-workflows-feature-branch-gitflow-and-fork/). 

Now, Forking Workflow is __fundamentally different__ than the other workflows. Instead of using a single server-side repository to act as the "central" codebase, it gives every developer a server-side repository. 

Developers push to their own server-side repositories, and __only the project maintainer__ can push to the official repository. 

This allows the maintainer to __accept commits__ from any developer without giving them write access to the official codebase.

This is an ideal workflow for open source projects.

## How It Works

1. developer fork the official repository to create a copy of it on the server.

1. no other developers are allowed to push to it, but they can pull changes from it

1. after he makes changes, he commits and push the commit to their own public repository - not the official one. Then, they file a pull request with the main repository.

1. maintainer pulls the contributor’s changes into their local repository, checks to make sure it doesn’t break the project, merges it into his local master branch, then pushes the master branch to the official repository 

## example

For a thorough example, read the ref link below. 

Reference link: [Forking Workflow by atlassian.com](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow)
