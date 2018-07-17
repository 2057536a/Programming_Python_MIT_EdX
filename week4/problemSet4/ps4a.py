# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	


#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """

    score = 0	#Variable to hold the score value, initialised to 0
    # If no word is made, score remains 0
    if len(word) == 0:
    	return score

   #Otherwise, count the score as the sum of the points
   # multiplied by the length of the word in the end
    else:
    	for letter in word:
    		score += SCRABBLE_LETTER_VALUES[letter]
    	score *= len(word)

    	#Check if all letters are used to make the word
    	# If true then add an extra 50 points to the final score
    	if len(word) == n:
    		score += 50
    	return score



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand



#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    #Make a copy of the original hand , so it is not mutated
    updated_hand = dict(hand)

    # Loop over the word's letters, and for each one
    # reduce the value of the key that represents the letter
    # If, in the end, the value is 0, remove the key from the dict
    for letter in word:
    	updated_hand[letter] -= 1
    	if updated_hand[letter] == 0:
    		del updated_hand[letter]
    return updated_hand




#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    
    #Make a copy of the original dictionary
    tempHand = hand.copy()

    #Keep count of how many letters are consumed from the dictionary
    count = 0

    #Check that word is in the word list
    # If it is, for each of its letters, check that there are
    # available letters in the dictionary to be used and increment the count
    # In the end the count should be the same length as the word
    if word in wordList:
        for letter in word:
            if letter in tempHand and tempHand[letter] >= 1:
                count += 1
                tempHand[letter] -= 1
        return count == len(word)
    else:
        return False



#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """

    length = 0
    for letter in hand:
    	length += hand[letter]
    return length



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of the total score
    total_score = 0    
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
    
        # Display the hand
        print("Current Hand: ", end='')
        displayHand(hand)
        
        # Ask user for input
        response = input('Enter word, or a "." to indicate that you are finished: ')
        
        # If the input is a single period:
        if response == ".":
        
            # End the game (break out of the loop)
            break
            
           
        # Otherwise (the input is not a single period):
        else:
        
            # If the word is not valid:
            if isValidWord(response, hand, wordList) == False:
            
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.")

            # Otherwise (the word is valid):
            else:

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                total_score += getWordScore(response,n)
                print('"' + response + '"' + ' earned ' + str(getWordScore(response,n)) + ' points. Total: ' + str(total_score) + ' points')

                
                # Update the hand
                hand = updateHand(hand,response)            

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if calculateHandlen(hand) <=0 :
        print()
        print("Run out of letters. Total score: " + str(total_score) + " points.")
    
    if response == ".":
        print("Goodbye! Total score: " + str(total_score) + " points.")



#
# Problem #5: Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    
    #Keep track of games played
    #This will be used when a player enters 'r' without
    # any prior games played. If number of games is 0 then he will
    #be prompted to select a new game or exit
    games = 0
    
    #Keep playing until players notifies that he wants to stop
    while True:
        #Ask for user input
        game_response = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    
        
        #Evaluate inputs
        if game_response == "n":
            #Need a new hand to be dealt through the dealHand function
            # It will be used as aparameter in the playHand function so
            # the game is initiated
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
            games += 1
        
        #If the player chooses to repeat a hand, call the playHand
        # function again but without re-defining a new hand
        elif game_response == "r":
            if games <=0:
                print("You have not played a hand yet. Please play a new hand first!")
            else:
                playHand(hand, wordList, HAND_SIZE)
         
        #Player wants to exit the game
        elif game_response == "e":
            break       
        else:
            print("Invalid command.")
    print()

        

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
