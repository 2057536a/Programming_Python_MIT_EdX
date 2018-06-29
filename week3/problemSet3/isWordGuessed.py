#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 08:12:44 2018

@author: yannis
"""

#implement the function isWordGuessed that takes in two 
#parameters - a string, secretWord, and a list of letters, 
#lettersGuessed. This function returns a boolean - True if 
#secretWord has been guessed (ie, all the letters of secretWord 
#are in lettersGuessed) and False otherwise.

#Example Usage:

#>>> secretWord = 'apple' 
#>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#>>> print(isWordGuessed(secretWord, lettersGuessed))
#False

#For this function, you may assume that all the letters in 
#secretWord and lettersGuessed are lowercase.


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    #A boolean flag initially set to true
    foundAll = True
    
    #Loop over the letters in the word
    #if the letter is not in the list, change the flag
    #and return its value in the end
    for l in secretWord:
        if l not in lettersGuessed:
            foundAll = False
    return foundAll