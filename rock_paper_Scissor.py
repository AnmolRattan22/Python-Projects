import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.")
    
    while True:
        user_choice = input("\nYour choice: ").lower()
        
        if user_choice == "exit":
            print("Thanks for playing! Goodbye!")
            break
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)

play_game()
