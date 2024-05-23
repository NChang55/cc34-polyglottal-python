import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors, lizard, Spock): ")
    possible_actions = ["rock", "paper", "scissors", "lizard", "Spock"]
    computer_action = random.choice(possible_actions)
    print(f"You chose {user_action}, computer chose {computer_action}.")
    if user_action not in possible_actions:
        print("Invalid input! Please enter rock, paper, scissors, lizard or Spock:")
        continue
    
    if user_action == computer_action:
        print(f"It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print(f"Rock crushes scissors, you win!")
        elif computer_action == "paper":
            print(f"Paper covers rock. You lose :(")
        elif computer_action == "lizard":
            print(f"Rock crushes lizard, you win!")
        elif computer_action == "Spock":
            print(f"Spock vaporizes rock. You lose :(")
    elif user_action == "paper":
        if computer_action == "scissors":
            print(f"Scissors cut paper. You lose :(")
        elif computer_action == "rock":
            print(f"Paper covers rock, you win!")
        elif computer_action == "lizard":
            print(f"Lizard eats paper. You lose:(")
        elif computer_action == "Spock":
            print(f"Paper disproves Spock, you win!")
    elif user_action == "scissors":
        if computer_action == "rock":
            print(f"Rock crushes scissors. You lose :(")
        elif computer_action == "paper":
            print(f"Scissors cut paper, you win!")
        elif computer_action == "lizard":
            print(f"Scissors decapitate lizard, you win!")
        elif computer_action == "Spock":
            print(f"Spock smashes scissors. You lose :(")
    elif user_action == "lizard":
        if computer_action == "rock":
            print(f"Rock crushes lizard. You lose :(")
        elif computer_action == "paper":
            print(f"Lizard eats paper, you win!")
        elif computer_action == "scissors":
            print(f"Scissors decapitate lizard. You lose :(")
        elif computer_action == "Spock":
            print(f"Lizard poisons Spock, you win!")
    elif user_action == "Spock":
        if computer_action == "rock":
            print(f"Spock vaporizes rock, you win!")
        elif computer_action == "paper":
            print(f"Paper disproves Spock. You lose :(")
        elif computer_action == "scissors":
            print(f"Spock smashes scissors, you win!")
        elif computer_action == "lizard":
            print(f"Lizard poisons Spock. You lose :(")
    
    play_again = input("Play again? (y/n): ").lower()
    if play_again.lower() not in ["y", "yes", "Y", "YES"]:
        break