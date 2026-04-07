import random

def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors:)")
    options = ["rock" , "paper" , "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice,"computer":computer_choice }

    return choices

choices = get_choices()
#print("You chose:" , choices["player"])
#print("Computer chose:" , choices["computer"])

def check_win(player,computer):
    #print(f"You chose {player}, Computer chose {computer}")
    print(f"You chose:", choices["player"])
    print(f"Computer chose:", choices["computer"])
    
    if player == computer:
        return "Its a tie"

    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    
    if win_conditions[player] == computer:
        return "You win"
    else:
        return "Computer wins"

result = check_win(choices["player"],choices["computer"])
print(f"\nResult: {result}")
