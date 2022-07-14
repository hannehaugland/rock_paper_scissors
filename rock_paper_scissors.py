import random 

user_wins = 0
comp_wins = 0 

options = ["rock", "paper", "scissors"]
users_choice = ""

while users_choice != 'q': 
    user_input = input("Rock/paper/scissors or Q to quit: ").lower()

    if user_input not in options: 
        continue
    
    #computers choice made by random: rock: 0, paper: 1, scissor: 2 
    random_number = random.randint(0, 2)
    computers_choice = options[random_number]
    print("Computer picked {}.").format(computers_choice)


