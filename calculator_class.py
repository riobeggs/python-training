import operator
import sys


available_operators = ["+", "-", "x", "*", "/"]


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
        print("\n\nYou may use this calculator as many times as you like.")
        print("To exit the calculator, type 'quit', then press enter.")
        print()
        print("Add using the '+' key.")
        print("Subtract using the '-' key.")
        print("Multiply using the 'x' key.")
        print("Divide using the '/' key.")
        print()

    
    def answer(self):
        if operator == "+":
            print()
            print(num1, "+", num2, "=", equation.add())
            print()

        if operator == "-":
            print()
            print(num1, "-", num2, "=", equation.subtract())
            print()

        if operator == "x":
            print()
            print(num1, "x", num2, "=", equation.multiply())
            print()

        if operator == "*":
            print()
            print(num1, "*", num2, "=", equation.multiply())
            print()

        if operator == "/":
            print()
            print(num1, "/", num2, "=", equation.divide())
            print()
            



def convert_to_float(number: str):
    converted = None
    try:
        converted = float(number)
    except:
        print(f"Could not convert '{number}' to a float")

    return converted


def get_number(question_prefix: str):
    while True:
        num = input(f"{question_prefix} number: ")

        converted_num = convert_to_float(num)

        if converted_num == None:
            continue

        return converted_num


def get_operator():
    while True:
        operator = input("Operator: ")
        if operator not in available_operators:
            continue
        return operator



Calculator.instructions()
num1 = get_number("First")
operator = get_operator()
num2 = get_number("Second")
equation = Calculator(num1=num1, operator=operator, num2=num2) 
equation.answer()


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
