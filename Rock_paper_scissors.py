from random import choice
#ROCK PAPER SCISSORS ZURI TASK

#create a list of possible choices
possible_choices = ["ROCK", "PAPER", "SCISSOR"]


GAME_ON = True
while GAME_ON:
    player_choice = input("Please choose 'R' for ROCK, 'P' for PAPER or 'S' for SCISSOR: ").upper()
    for word in possible_choices:
        if word[0] == player_choice:
            player_choice = word
            continue
            
            
    #Loop Until user's choice is in the list of possible choices
    if player_choice not in possible_choices:
        print('invalid choice')
        player_choice = input("Please choose 'R' for ROCK, 'P' for PAPER or 'S' for SCISSOR: ").upper()
        for word in possible_choices:
            if word[0] == player_choice:
                player_choice = word
                
            
    computer_choice = choice(possible_choices)
    
    
    print(f"Player ({player_choice}): CPU ({computer_choice})")

    #compare player moves
    if player_choice == computer_choice:
        print("It's a tie!")
        continue
    elif player_choice == "ROCK" and computer_choice == "SCISSOR":
        print("Player wins!")
        GAME_ON = False
    elif player_choice == "PAPER" and computer_choice == "ROCK":
        print("Player wins!")
        GAME_ON = False
    elif player_choice == "SCISSOR" and computer_choice == "PAPER":
        print("Player wins!")
        GAME_ON = False
    else:
        print("Computer wins!")
        GAME_ON = False
    

