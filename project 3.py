import random

def chosen_word():
    wordchoice = ["Bake" , "Word" , "List" , "Four"	, "Five" , "Nine" , "Good" , "Best"	, "Cute" , "Zero" , "Huge" , "Cool" , "Tree" , "Race" , "Rice" , "Keep"	, "Lace" , "Beam" , "Game" , "Mars" , "Tide" , "Ride" , "Hide" , "Exit" , "Hope" , "Cold" , "From" , "Need" , "Stay" , "Come"]
    word = (random.choice(wordchoice).lower())
    return word
    
def intro():
    print("\nGuess the 4 letter word in 10 attempts to win!\n")
    input("Press Enter to start.")
    print("\n")

#if the users guess is not a real word then print incorrect
def users_guess(word):
    for i in range(10):
        guess = input("Guess: ").lower()
        if len(guess)>4 or len(guess)<4:
            print("Incorrect\nYou must guess 4 letter words only.\n")
        #if the users guess contains characters in the chosen word then let them know what letters they got correct.
        elif len(guess)==4 and guess[0] in word and guess != word:
            print("Incorrect")
            print("You guessed these letters correctly:")
            print(guess[0])
        elif len(guess)==4 and guess != word:
            print("Incorrect\n")
        elif guess == word:
            print("Correct\n")
            break

def answer(word):
    print("The word was:", word)

def main():
    intro()
    word = chosen_word()
    print(word)
    users_guess(word)
    answer(word)

if __name__ == "__main__":
    main()

# Computer chooses a word to guess

# Capture guess from user

# process guess to find matches

# Reveal matches to user

# Check number of guesses from user

    # if they guess correctly display you win
    # if they have guesses, let them guess again, (repeat loop)
    # if the number guesses is exceeded, print you lose
