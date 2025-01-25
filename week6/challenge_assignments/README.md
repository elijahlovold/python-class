# Game Assignments: Hangman, Dungeon Escape, and Word Scramble

## Overview

This document describes three interactive Python-based games: Hangman, Dungeon Escape, and Word Scramble. These games are designed to practice programming skills using functions, loops, and conditional statements. Each game operates independently and is accessed via a menu system.

## 1. Hangman

### Description:

Hangman is a word-guessing game where the player tries to guess a hidden word one letter at a time. The player has a limited number of incorrect guesses before losing.

### Gameplay:

The program randomly selects a word from a predefined list.

The player guesses letters to reveal the word.

Correct guesses reveal the positions of the guessed letter.

Incorrect guesses decrease the number of remaining attempts.

The game ends when the word is guessed completely or the player runs out of attempts.

### Requirements:

Python's random module to select random words.

A loop to handle multiple guesses.

Conditional statements to validate guesses and update the game state.

## 2. Dungeon Escape

### Description:

Dungeon Escape is a text-based adventure game where the player navigates through a dungeon to escape. The game features randomized outcomes for actions and simple decision-making.

### Gameplay:

The player starts at the dungeon's entrance and chooses between two paths (left or right).

If the player goes left, they encounter a monster and must choose to fight or run.

Fighting has a 50% chance of success.

Running sends the player back to the start.

If the player goes right, they find the dungeon exit and win.

The game ends when the player either escapes or loses to the monster.

### Requirements:

Randomized outcomes using random.random().

Loop and conditionals to handle player choices.

Input validation for user actions.

## 3. Word Scramble

### Description:

Word Scramble is a word-based puzzle game where the player must unscramble a randomly shuffled word. The game consists of multiple rounds with a scoring system.

### Gameplay:

The program selects a random word from a predefined list and scrambles its letters.

The player attempts to guess the original word.

Correct guesses increase the player's score.

The game runs for five rounds, after which the final score is displayed.

### Requirements:

Randomized word scrambling using random.sample().

A loop to handle multiple rounds.

Scoring system to track the player's performance.

## Arcade Menu 

### Description:

The program includes a menu system that allows the player to choose a game or quit. The menu operates in a loop until the player decides to exit.

### Options:

* Play Hangman.

* Play Dungeon Escape.

* Play Word Scramble.

* Quit the program.

### Requirements:

Loop to continuously display the menu.

Conditional statements to handle player choices.

Integration of the three games into the menu system.

Follow the on-screen menu to choose a game and play.

## Customization

Feel free to enhance the games by:

Adding difficulty levels (e.g., more/less guesses or rounds).

Expanding word lists or adding new features.

Implementing additional feedback or visuals.

