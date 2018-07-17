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