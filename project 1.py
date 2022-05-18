"""
hi sam, ive created functions for all of the different parts of the code.
my problem is that the variables i have created arent defined within other functions for example 
in my users_name function i have defined the variable name but in the greet_user function it is not defined.
the same problem occurs in other variables i have made too. Is there a way around this?
I havent started working on the bug for the quiz loop yet and i'm not sure if ive structured or
done this correctly since i havent really worked with functions before.
"""


import random
import time
# Capture the users name
def users_name():
    print("\n")
    name = input("Name: ")

# greets user and asks for the amount of equations they wish to answer
def greet_user():
    print("\n")
    print("Hello, "+str(name.capitalize())+"! \n\nThis is a multiplication test.")
    print("How many equations would you like to answer?")
    global equations
    equations = input("Equations: ")
    equations = int(equations)
    # Find a way to prevent this from crashing if I dont enter a number
    print("\nComplete the equations as fast as you can.")
    print("Your time will be displayed at the completion of this test.\n")

# starts the timer
def timer_start():
    input("Press Enter to start")
    print("\n")
    global start_time
    start_time = time.time()
    start_time = int(start_time)

def convert_to_int(input):
    converted = None
    try:
        converted = int(input)
        return converted
    except:
        pass
        

def printer(x: str) -> None:
    x = x.upper()
    print(x)
    return x

# Quizzing loop
def quiz():
    for i in range(equations):
        if i % 1 == 0:
            num1 = random.randint(0,9)
            num2 = random.randint(0,9)
        while True:
            print(num1, "x", num2, "=")
            answer = input("")
            # Find a way to prevent this from crashing if I dont enter a number
            if int(answer) == num1 * num2:
                print("Correct\n")
                break
            elif int(answer) != num1 * num2:
                print
            elif type(answer) != int:
                print("Incorrect\n") 
            

# stops the timer
def timer_end():
    input("Press Enter to stop\n")
    global end_time
    end_time = time.time()
    end_time = int(end_time)

#displays and calculates the time taken to finish the quiz
def result_display():
    timer = end_time - start_time
    print("Well done " +str(name.capitalize())+"!")
    print("Your time was:")
    print(int(timer), "seconds\n")

# Displays the time taken to answer the chosen amount of equations

def main():
    name = users_name()
    greet_user()
    timer_start()
    quiz()
    timer_end()
    result_display()


if __name__ == "__main__":
    main()