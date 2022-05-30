import sys
import operator


QUIT = "quit"
OPERATIONS = {"+" : operator.add,
        "-" : operator.sub,
        "x" : operator.mul,
        "*" : operator.mul,
        "/" : operator.truediv}


# gives the user instructions on how to use the calculator
def instructions():
    print("\n\nYou may use this calculator as many times as you like.")
    # shows how to exit program
    print("To exit the calculator, type 'quit', then press enter.")
    # gives the user the operators available to use
    print("\nAdd using the '+' key.")
    print("Subtract using the '-' key.")
    print("Multiply using the 'x' key.")
    print("Divide using the '/' key.\n")


# trys to convert the users input to a float
def convert_to_float(number: str):
    converted = None
    # if the input cant be converted to a float then it returns as None
    try:
        converted = float(number)
        # retuns as float if it can be converted to a float
    except: 
        print(f"Could not convert '{number}' to a float")

    return converted


def exit():
    print("Quitting...")
    sys.exit(0)


def is_quit(user_input: str) -> bool:
    formatted = user_input.lower().strip()
    return formatted == QUIT


# gets the users input for a number in the equation
def get_number(question_prefix: str):
    while True:
        num = input(f"{question_prefix} number: ")

        # quits program if they enter 'quit'
        if is_quit(num):
            exit()

        converted_num = convert_to_float(num)

        # if the users input is not a float start loop again (ask for input)
        if converted_num == None:
            continue

        return converted_num


# gets the users input for the operator that want to use
def get_operator():
    while True:
        operator = input("Operator: ")

        # quits program if they enter 'quit'
        if is_quit(operator):
            exit()
        
        # if the chosen operator is not a real operator
        # and is not in the available operators created in the operator dictionary
        # then ask for the users input again
        if operator not in OPERATIONS:
            continue

        return operator


# prints and calculates the answer to the users equation
def calculate_answer(num1, operator, num2):
    print(num1, operator, num2, "=", OPERATIONS[operator](num1,num2), "\n\n")      


# calls functions that compile the program
def run_calculator():
    # excecutes instructions function
    instructions()
    while True:
        # forever repeats the calculator until the user enters 'exit'
        num1 = get_number("First")
        operator = get_operator()
        num2 = get_number("Second")
        calculate_answer(num1, operator, num2)


# excecutes the program
run_calculator()