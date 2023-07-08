import random

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    print("Enter your choice: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    choices = ["Rock", "Paper", "Scissors"]
    
    while True:
        player_choice = input("Enter your choice (1-3): ")
        
        if player_choice.isdigit() and 1 <= int(player_choice) <= 3:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
    
    player_choice = choices[int(player_choice) - 1]
    computer_choice = random.choice(choices)
    
    print("You chose:", player_choice)
    print("Computer chose:", computer_choice)
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!")
    else:
        print("Computer wins!")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break