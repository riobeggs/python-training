# Create some code to randomly select a number under 10
# The user must try to guess this number in 3 or less guesses
# If the users guess is too low, tell them
# If the users guess is too high, tell them
# There is a strategy to this game which will allow you to always win. Figure out that strategy
import random
""" Example
computer chooses 3
3 guesses remaining
user guesses 1
"too low"
2 guesses remaining
user guesses 9
"too high"
1 guess remaining
user guesses 3
"Correct"
"""

def intro():
    print("\n\nI am thinking of a number between 1 and 9.")
    print("You have 3 attempts to guess my number.")


def convert_to_int(input):
  converted = None
  try:
      converted = int(input)
  except: 
      pass

  return converted


def random_number():
    answer = random.randint(1,9)
    return answer


def get_users_guess():
    guess = input("guess: ")
    return convert_to_int(guess)


def hinter(guess, answer):
    if guess < answer:
        print("Your guess is too low")
        
    if guess > answer:
        print("Your guess is too high")

    if guess == answer:
        return guess
        # #TODO find a way to break 


def valid_guess(i):
    is_valid = False
    while is_valid == False:
        guesses_left(i)
        guess = get_users_guess()
        if guess != None:
            is_valid = True
    return guess


def guesses_left(i): 
    if 3 - i != 1:
        print("\n")
        print(3 - i, "guesses remaining")
    
    if 3 - i == 1:
        print("\n")
        print("1 guess remaining")


def run_game():
    answer = random_number()

    for i in range(3):
        guess = valid_guess(i)
        hinter(guess, answer)

    results(guess, answer)



def results(guess, answer):
    if guess == answer:
        print("\nYou win!")
        print("The number was:", answer, "\n\n")
    else:
        print("\nYou lose!")
        print("The number was:", answer, "\n\n")


def main():
    intro()
    run_game()


if __name__ == "__main__":
    main()