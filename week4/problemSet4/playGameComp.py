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