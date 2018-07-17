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
