import random 

user_wins = 0
comp_wins = 0 

options = ["rock", "paper", "scissors"]
user_input = ""

while user_input != "q": 
    user_input = input("Rock/paper/scissors or Q to quit: ").lower()

    if user_input not in options: 
        continue
    
    #computers choice made by random: rock: 0, paper: 1, scissor: 2 
    random_number = random.randint(0, 2)
    computers_choice = options[random_number]
    print("Computer picked {}.".format(computers_choice))

    if user_input == "rock" and computers_choice == "scissors": 
        user_wins += 1 
        print("You won!")
    elif user_input == "paper" and computers_choice == "rock":
        user_wins += 1
        print("You won!")
    elif user_input == "scissors" and computers_choice == "paper": 
        user_wins += 1
        print("You won!")
    else: 
        comp_wins += 1
        print("You lost!")

print("\nYou won {} time(s), the computer won {} time(s).".format(user_wins, comp_wins))
print("Thanks for playing!")
