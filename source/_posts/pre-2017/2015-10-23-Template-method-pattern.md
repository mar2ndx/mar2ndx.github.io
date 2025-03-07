---
title: "[Java OOP] Template method pattern (abstract class) "
category: Java OOP
tags: []
comments: true
date: 2015-10-23 00:00
---


# Overview

**[Template method pattern](https://en.wikipedia.org/wiki/Template_method_pattern) is a behavioral design pattern** that defines the program skeleton of an algorithm in a method, called template method, which **defers some steps to subclasses**.

It lets one **redefine** certain steps of an algorithm without changing the algorithm's structure.

## Usage

The template method is used in frameworks, where each implements the invariant parts of a domain's architecture.

## Example in Java

Refer to [code from WIKI](https://en.wikipedia.org/wiki/Template_method_pattern#Example_in_Java):

    /**
     * An abstract class that is common to several games in
     * which players play against the others, but only one is
     * playing at a given time.
     */

    abstract class Game {
     /* Hook methods. Concrete implementation may differ in each subclass*/
        protected int playersCount;
        abstract void initializeGame();
        abstract void makePlay(int player);
        abstract boolean endOfGame();
        abstract void printWinner();

        /* A template method : */
        public final void playOneGame(int playersCount) {
            this.playersCount = playersCount;
            initializeGame();
            int j = 0;
            while (!endOfGame()) {
                makePlay(j);
                j = (j + 1) % playersCount;
            }
            printWinner();
        }
    }

    //Now we can extend this class in order
    //to implement actual games:

    class Monopoly extends Game {

        /* Implementation of necessary concrete methods */
        void initializeGame() {
            // Initialize players
            // Initialize money
        }
        void makePlay(int player) {
            // Process one turn of player
        }
        boolean endOfGame() {
            // Return true if game is over
            // according to Monopoly rules
        }
        void printWinner() {
            // Display who won
        }
        /* Specific declarations for the Monopoly game. */

        // ...
    }

    class Chess extends Game {

        /* Implementation of necessary concrete methods */
        void initializeGame() {
            // Initialize players
            // Put the pieces on the board
        }
        void makePlay(int player) {
            // Process a turn for the player
        }
        boolean endOfGame() {
            // Return true if in Checkmate or
            // Stalemate has been reached
        }
        void printWinner() {
            // Display the winning player
        }
        /* Specific declarations for the chess game. */

        // ...
    }
