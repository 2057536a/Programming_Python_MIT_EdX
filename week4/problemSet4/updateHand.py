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