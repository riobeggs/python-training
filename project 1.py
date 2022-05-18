# import random
# import time

# # Capture the users name
# def users_name():
#     print("\n")
#     name = str(input("Name: "))
#     return name

# # captures the amount of equations the user wishes to answer
# # Find a way to prevent this from crashing if I dont enter a number
# def user_equations():
#     equations = int(input("Equations: "))
#     return equations

# # greets user and asks for the amount of equations they wish to answer
# def greet_user(name):
#     print("\n")
#     print("Hello, "+str(name.capitalize())+"! \n\nThis is a multiplication test.")
#     print("How many equations would you like to answer?\n")

# # lets the user know how many questions they will be answering and how the score is recorded
# def amount_of_equations(equations):
#     print("\nComplete the" , equations , "equations as fast as you can.")
#     print("Your time will be displayed at the completion of this test.\n")

# # starts the timer
# def timer_start():
#     input("Press Enter to start")
#     print("\n")
#     global start_time
#     start_time = time.time()
#     start_time = int(start_time)

def convert_to_int(input):
    converted = None
    try:
        converted = int(input)
        return converted
    except:
        print()
        
# def printer(x: str) -> None:
#     x = x.upper()
#     print(x)
#     return x

# Quizzing loop
def quiz(equations):
    for i in range(equations):
        if i % 1 == 0:
            num1 = random.randint(0,9)
            num2 = random.randint(0,9)
        while True:
            print(num1, "x", num2, "=")
            answer = input("")
            if convert_to_int(answer) and (answer) == num1 * num2:
                print("Correct\n")
                break
            else:
                print("Incorrect\n")
            
            
# # stops the timer
# def timer_end():
#     input("Press Enter to stop\n")
#     global end_time
#     end_time = time.time()
#     end_time = int(end_time)

# #displays and calculates the time taken to finish the quiz
# def result_display(name):
#     timer = end_time - start_time
#     print("Well done " +str(name.capitalize())+"!")
#     print("Your time was:\n")
#     print(int(timer), "seconds\n")

# def main():

    
#     name = users_name()
#     greet_user(name)
#     equations = user_equations()
#     amount_of_equations(equations)
#     timer_start()
#     quiz(equations)
#     timer_end()
#     result_display(name)


# if __name__ == "__main__":
#     main()