import sys
import operator

# function for storing properties of operators in a dictionary 
def operator_dict():
    # also associates operators with the users input and variables
    ops = {"+" : operator.add,
        "-" : operator.sub,
        "x" : operator.mul,
        "/" : operator.truediv}
    return ops


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
def convert_to_int(equation):
    converted = None
    # if the input cant be converted to a float then it returns as None
    try:
        converted = float(equation)
        # retuns as float if it can be converted to a float
    except: 
        pass

    return converted


# gets the users input for a number in the equation
def get_number():
    while True:
        num1 = input("First number: ")

        # quits program if they enter 'quit'
        if num1 == "quit":
            sys.exit(0)

        converted_num1 = convert_to_int(num1)

        # if the users input is not a float start loop again (ask for input)
        if converted_num1 == None:
            continue

        return converted_num1


# gets the users input for the operator that want to use
def get_operator():
    while True:
        operator = input("Operator: ")

        # quits program if they enter 'quit'
        if operator == "quit":
            sys.exit(0)

        ops = operator_dict()
        
        # if the chosen operator is not a real operator
        # and is not in the available operators created in the operator dictionary
        # then ask for the users input again
        if operator not in ops:
            continue

        return operator


# prints and calculates the answer to the users equation
def calculate_answer(num1, operator, num2):
    ops = operator_dict()
    print(num1, operator, num2, "=", ops[operator](num1,num2), "\n\n")      


# calls functions that compile the program
def run_calculator():
    # excecutes instructions function
    instructions()
    while True:
        # forever repeats the calculator until the user enters 'exit'
        num1 = get_number()
        operator = get_operator()
        num2 = get_number()
        calculate_answer(num1, operator, num2)


# excecutes the program
run_calculator()