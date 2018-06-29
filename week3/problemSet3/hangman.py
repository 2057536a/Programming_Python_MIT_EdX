#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 09:05:01 2018

@author: yannis
"""

#   Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. 
#   This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of 
#   the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the 
#   previous part.

#   You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load 
#   the words and pick a random one. Note that the functions loadWords and chooseWord should only be used on your 
#   local machine, not in the tutor. When you enter in your solution in the tutor, you only need to give your 
#   hangman function.

#   Consider using lower() to convert user input to lower case. For example:

#   guess = 'A'
#   guessInLowerCase = guess.lower()

#   Consider writing additional helper functions if you need them!

#   There are four important pieces of information you may wish to store:

#   secretWord: The word to guess.
#   lettersGuessed: The letters that have been guessed so far.
#   mistakesMade: The number of incorrect guesses made so far.
#   availableLetters: The letters that may still be guessed. Every time a player guesses a letter, 
#   the guessed letter must be removed from availableLetters (and if they guess a letter that is not 
#   in availableLetters, you should print a message telling them they've already guessed that - so try again!).


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    #The initial list with the guessed letters and the number of guesses
    lettersGuessed = []
    availableGuesses = 8
    
    #Introductory lines to the game
    print("Welcome to the game, Hangman!\nI am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-------------")
    
    #If the word is not guessed, then keep playing
    while not isWordGuessed(secretWord,lettersGuessed):
        #Let pleyer know the number of guesses left and the letters to choose from. Then ask for input letter
        print("You have " + str(availableGuesses) + " guesses left.\nAvailable letters: " + getAvailableLetters(lettersGuessed))    
        guessingLetter = input("Please guess a letter: ")
    
        #If the input has not been guessed yet, then add it to the list
        if guessingLetter not in lettersGuessed:
            lettersGuessed.append(guessingLetter)
            
            #If the letter is part of the secret word, let user know that the guess was correct
            #Otherwise decrease the number of guesses he/she has left
            if guessingLetter in secretWord:
                print("Good guess: " + getGuessedWord(secretWord,lettersGuessed))
            else:
                print("Oops! That letter is not in my word: "+getGuessedWord(secretWord,lettersGuessed) )
                availableGuesses -= 1           
            print("-------------")
            
            #If the word is guessed entirely, print the victory statement
            if isWordGuessed(secretWord,lettersGuessed): 
                print("Congratulations, you won!")
            
            #In case no more available guesses have left, let user know and force a game over
            if availableGuesses <=0:
                print("Sorry, you ran out of guesses. The word was " + secretWord)
                break
        
        #If the input letter has been picked before, let user know and do not penalise the available guesses left
        else:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord,lettersGuessed)  )
            print("-------------")
    