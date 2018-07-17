from ps4a import *
import time


#
#
# Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
            # find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
    # return the best word you found.
    return bestWord

#
# Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0) :
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else :
            # If the word is not valid:
            if (not isValidWord(word, hand, wordList)) :
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else :
                # Tell the user how many points the word earned, and the updated total score 
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')

    
#
# Problem #6: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """




    # #Keep track of number of games
    # # to be used when the player chooses
    # # to repeat a game. If the number is 0 
    # # then he will be notified that there is no
    # # previous hand to be repeated
    games = 0

    #Keep playing until players notifies that he wants to stop
    while True:
        #Ask for user input
        game_response = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    
        
        #Evaluate inputs
        if game_response == "n":
            hand = dealHand(HAND_SIZE)
            player_choice = input("Enter u to have yourself play, c to have the computer play: ")
            while True:

                #player_choice = input("Enter u to have yourself play, c to have the computer play: ")

                if player_choice == "u":


                    #Need a new hand to be dealt through the dealHand function
                     # It will be used as aparameter in the playHand function so
                    # the game is initiated

                    playHand(hand, wordList, HAND_SIZE)
                    games += 1
                    break

                elif player_choice == "c":
                    compPlayHand(hand,wordList,HAND_SIZE)
                    games += 1
                    break

                else:
                    player_choice = input("Enter u to have yourself play, c to have the computer play: ")

        
        #If the player chooses to repeat a hand, call the playHand
        # function again but without re-defining a new hand
        elif game_response == "r":
            if games <=0:
                print("You have not played a hand yet. Please play a new hand first!")
            else:

                player_choice = input("Enter u to have yourself play, c to have the computer play: ")

                while True:

                #player_choice = input("Enter u to have yourself play, c to have the computer play: ")

                    if player_choice == "u":


                    #Need a new hand to be dealt through the dealHand function
                     # It will be used as aparameter in the playHand function so
                    # the game is initiated

                        playHand(hand, wordList, HAND_SIZE)
                        games += 1
                        break

                    elif player_choice == "c":
                        compPlayHand(hand,wordList,HAND_SIZE)
                        games += 1

                    else:
                        player_choice = input("Enter u to have yourself play, c to have the computer play: ")
         
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


