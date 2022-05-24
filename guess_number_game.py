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

def convert_to_int(input):
  converted = None
  try:
      converted = int(input)
  except: 
      pass

  return converted


def random_number():
    answer = random.randint(1,11)
    return answer


def get_users_guess():
    guess = input("guess: ")
    return convert_to_int(guess)

def run():
    answer = random_number()
    for i in range(3):
        # capture guess
        is_valid = False
        while is_valid == False:
            guess = get_users_guess()
            if guess != None:
                is_valid = True

        # process guess
        if guess < answer:
            print("Your guess is too low")
        
        if guess > answer:
            print("Your guess is too high")

        if guess == answer:
            print("You win")
            break


run()


