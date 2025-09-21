import random

# Score Tracking (Optional)
user_score = 0
computer_score = 0

print("🎮 Welcome to Rock-Paper-Scissors Game! 🎮")

while True:
    # User Input
    user_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()

    # Computer Selection
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    # Display Choices
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Game Logic
    if user_choice == computer_choice:
        print("👉 It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("✅ You win this round!")
        user_score += 1
    elif user_choice in choices:
        print("❌ Computer wins this round!")
        computer_score += 1
    else:
        print("⚠️ Invalid input! Please choose rock, paper, or scissors.")
        continue  # Skip score update if invalid input

    # Display Result + Scores
    print(f"📊 Score -> You: {user_score}, Computer: {computer_score}")

    # Play Again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\n🏁 Final Score:")
        print(f"You: {user_score}, Computer: {computer_score}")
        print("🎉 Thanks for playing! Goodbye 👋")
        break
