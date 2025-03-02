---
title: <Coursera> Reinforcement Learning 1
category: unknown
tags: []
comments: true
date: 2025-03-02 13:58:56
---

# Different approach

RL is different from other ML methods, as RL:

1. start with a fully interactive, goal-driven agent
1. it will make decisions
1. it will pursue a goal

## Elements of RL

A policy, a reward signal , a value function, and optionally, a model of the environment.

1. Policy

    A map from {perceived states of environment} to {actions to be taken}

    It's called __stimulus-response rules__ in psychology. 

1. Reward signal

    The goal of RL problem. 

1. Value function

    Reward is for immediate, but value is the long-term desirability of states.

    eg. a state might yeild a low immediate reward, but still have hight value. 

1. Model

    mimics thebehaviour of environment.

# Multi-armed Bandits

多杆老虎机。

> Slot Machine（老虎机）, are sometimes called One-Armed Bandit. Because traditional slot machines have a single lever (arm) to pull and spin the reels.
>
> "Bandit" → Slot machines take people's money like robery, so they are metaphorically called "bandits."

![](/images/Multi-Armed-Bandit.jpeg)

