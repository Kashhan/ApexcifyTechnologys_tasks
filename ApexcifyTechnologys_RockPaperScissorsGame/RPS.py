import random

# Initialize counters for user's choices
user_choices = {'rock': 0, 'paper': 0, 'scissors': 0}

def get_computer_choice():
    """Select the computer's choice, either based on user's patterns or randomly."""
    learning_probability = 0.6  # 60% chance AI will "learn" from user's past choice, 40% chance to choose randomly

    if random.random() < learning_probability:
        # If the AI is "learning", predict the next move
        if sum(user_choices.values()) == 0:
            return random.choice(['rock', 'paper', 'scissors'])  # First time, random choice
        
        # Predict the user's next choice based on their past choices
        most_chosen = max(user_choices, key=user_choices.get)
        
        # AI counters (not always, but often)
        if most_chosen == 'rock':
            return random.choice(['paper', 'scissors'])  # 50% chance to choose paper or scissors
        elif most_chosen == 'paper':
            return random.choice(['rock', 'scissors'])  # 50% chance to choose rock or scissors
        else:
            return random.choice(['rock', 'paper'])  # 50% chance to choose rock or paper
    else:
        # Otherwise, make a random choice
        return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Play the game repeatedly until the user types 'exit'."""
    print("Welcome to Rock-Paper-Scissors with AI Learning!")
    
    while True:
        # User input
        user_choice = input("Enter 'rock', 'paper', or 'scissors' (or type 'exit' to quit): ").lower()
        
        # Check if the user wants to exit the game
        if user_choice == 'exit':
            print("Thanks for playing!")
            break
        
        # Ensure the user input is valid
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue
        
        # Track user's choice
        user_choices[user_choice] += 1
        
        # Computer input (AI learns from user input)
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

# Start the game
play_game()
