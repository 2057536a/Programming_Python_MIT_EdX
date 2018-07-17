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