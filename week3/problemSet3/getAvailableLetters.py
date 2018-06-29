#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 08:41:36 2018

@author: yannis
"""

#Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, 
#lettersGuessed. This function returns a string that is comprised of lowercase English letters - all 
#lowercase English letters that are not in lettersGuessed.

#Example Usage:

#>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#>>> print(getAvailableLetters(lettersGuessed))
#abcdfghjlmnoqtuvwxyz


#Note that this function should return the letters in alphabetical order, as in the example above.

#For this function, you may assume that all the letters in lettersGuessed are lowercase.

#Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters:

#>>> import string
#>>> print(string.ascii_lowercase)
#abcdefghijklmnopqrstuvwxyz

import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    #the string of all letters in the alphabet in lowercase
    availableLetters = string.ascii_lowercase
    
    #loop over the letters in the lettersGuessed and delete its
    #occurence in the alphabet. In the end the availableLetters will contain only the
    #letters that are not guessed yet, i.e. all the available letters so far
    for letter in lettersGuessed:
        
        availableLetters = availableLetters.replace(letter, "")
        
    return availableLetters
    