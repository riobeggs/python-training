import operator
import sys


class Calculator:
    def __init__(self, num1, operator, num2):
        self.num1 = num1
        self.operator = operator
        self.num2 = num2


    def add(self):
        if self.operator == "+":
            return self.num1 + self.num2
        else:
            pass


    def subtract(self):
        if self.operator == "-":
            return self.num1 - self.num2
        else:
            pass


    def multiply(self):
        if self.operator == "x":
            return self.num1 * self.num2
        else:
            pass

        if self.operator == "*":
            return self.num1 * self.num2
        else:
            pass


    def divide(self):
        if self.operator == "/":
            return self.num1 / self.num2
        else:
            pass


def instructions():
        """Print an introduction teaching users how to use the calculator."""
        print("\n\nYou may use this calculator as many times as you like.")
        # shows how to exit program
        print("To exit the calculator, type 'quit', then press enter.")
        print()
        # gives the user the operators available to use
        print("Add using the '+' key.")
        print("Subtract using the '-' key.")
        print("Multiply using the 'x' key.")
        print("Divide using the '/' key.")
        print()


def convert_to_float(number: str):
    converted = None
    # if the input cant be converted to a float then it returns as None
    try:
        converted = float(number)
        # retuns as float if it can be converted to a float
    except:
        print(f"Could not convert '{number}' to a float")

    return converted


def get_number(question_prefix: str):
    while True:
        num = input(f"{question_prefix} number: ")

        converted_num = convert_to_float(num)

        # if the users input is not a float start loop again (ask for input)
        if converted_num == None:
            continue

        return converted_num


available_operators = ["+", "-", "x", "*", "/"]

def get_operator():
    while True:
        operator = input("Operator: ")
        if operator not in available_operators:
            continue
        # if operator is not in available operators ask for input again
        return operator


instructions()
num1 = get_number("First")
operator = get_operator()
num2 = get_number("Second")
equation = Calculator(num1=num1, operator=operator, num2=num2) #excecute the correlating function
# to the operator chosen by the user
if operator == "+":
    print("Answer:", equation.add())
if operator == "-":
    print("Answer: ", equation.subtract())
if operator == "x":
    print("Answer:", equation.multiply())
if operator == "*":
    print("\nAnswer:", equation.multiply())
if operator == "/":
    print("Answer:", equation.divide())
print("\n\n")

    # Define a function which gives instruction how to use the calculator

    # Create multiply func
    # Create devide func
    # Create add func
    # Create subtract func



# Once you have created a calculator class capable of performing calculations
# Create project 4 again, but this time use the calculator. 
# You must use my_calculator.Add(5, 6) for adding for instance

# I really dont expect you to be able to do this.
# Super added you dont need me points, Construct a quizzer, which asks questions.
# It should use the Calculator.
