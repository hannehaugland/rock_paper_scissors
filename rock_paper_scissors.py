import random 

user_wins = 0
comp_wins = 0 

options = ["rock", "paper", "scissors"]
users_choice = ""

while users_choice != 'q': 
    user_input = input("Rock/paper/scissors or Q to quit: ").lower()

