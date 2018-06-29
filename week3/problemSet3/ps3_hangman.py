# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string


WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    #The string representing what letters have been guessed so far, initially empty
    guessedSoFar = ""
    
    #If the letter of the word is in the list of letters, then add it to the guessedSoFar string
    # otherwise, put an underscore in that place to show that the letter is yet to be found
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            guessedSoFar += secretWord[i]
        else:
            guessedSoFar += "_ "
    return guessedSoFar




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





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
