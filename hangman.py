""" HANGMAN GAME BUILT AS A CodeAlpha PROJECT """

import random


# List of exactly 5 predefined words (Electronics/Engineering theme)
WORD_LIST = ["diode", "relay", "chips", "motor", "cables"]
    
# Game state variables 
MAX_ATTEMPTS = 6

# Custom ASCII Hangman stages (0 to 6 wrong guesses)
HANGMAN_STAGES = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """
]

def play_hangman(score):
    """ MAIN GAME LOOP FOR HANGMAN GAME
     
    Args:
        score (int): The current score of the player.
    """

    # Pick a random secret word
    secret_word = random.choice(WORD_LIST)
    
    # Game state variables cont`d
    incorrect_guesses = 0
    guessed_letters = []

    print("\n" + "=" * 45)
    print("=== Welcome to CodeAlpha Hangman Game! ======")
    print("=== Try to guess the secret word ============")
    print("=== You have", MAX_ATTEMPTS, "attempts to guess the word ===")
    print("=== Category: Electronics & Engineering =====")
    print("=" * 45)

    # While loop to keep the game running while lives remain
    while incorrect_guesses < MAX_ATTEMPTS:
        # Display current ASCII art stage
        print(HANGMAN_STAGES[incorrect_guesses])
        
        # Generate the word display (blanks or guessed letters)
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("Current Word:", display_word.strip())
        print(f"Lives left: {MAX_ATTEMPTS - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
                
        # Get player input
        guess = input("Guess a letter: ").lower().strip()
        
        # Reject invalid input without costing a life
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input! Please enter a single alphabetical letter\n")
            continue
            
        # Reject repeated letters without costing a life
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter! Try a different one\n")
            continue
            
        # Add valid new guess to our list
        guessed_letters.append(guess) 
        
        # Check if the guess is right or wrong
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word\n")

            # Check if player has won immediately
            if all(letter in guessed_letters for letter in secret_word):
                print(HANGMAN_STAGES[incorrect_guesses])
                print(f"\n🎉 Congratulations! You guessed the secret word: '{secret_word}'!")
                score["wins"] += 1
                return
            
        else:
            print(f"❌ Sorry, '{guess}' is not in the word\n")
            incorrect_guesses += 1

    else:
        # Loss condition (lives hit 0)
        print(HANGMAN_STAGES[incorrect_guesses])
        print(f"\n💀 Game Over! You ran out of lives")
        print(f"The correct word was: '{secret_word}'")
        score["losses"] += 1


if __name__ == "__main__":
    # Initialize session scoreboard
    score = {"wins": 0, "losses": 0}
    
    while True:
        play_hangman(score)
        
        # Display session scoreboard
        print(f"\n📊 Session Scoreboard -> Wins: {score['wins']} | Losses: {score['losses']}")
        
        # Ask player if they want to play again
        while True:
            choice = input("\nWould you like to play again? (y/n): ").lower().strip()
            
            if choice == 'y' or choice == 'n':
                break
            else:
                print("❌ Invalid choice! Please enter 'y' or 'n'\n")
        
        if choice == 'n':
            print("\nThanks for playing CodeAlpha Hangman Game! Goodbye!")
            break
            
        print("\n" + "="*40 + "\nStarting a new game...\n")