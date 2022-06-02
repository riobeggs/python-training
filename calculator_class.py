import operator


#constants
available_operators = ["+", "-", "x", "*", "/"]
OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "x": operator.mul,
    "*": operator.mul,
    "/": operator.truediv,
}


class Calculator:
    def __init__(self, num1, operator, num2):
        self.num1 = num1
        self.operator = operator
        self.num2 = num2


    def instructions():
        print("\n\nYou may use this calculator as many times as you like.")
        print("To exit the calculator, type 'quit', then press enter.")
        print()
        print("Add using the '+' key.")
        print("Subtract using the '-' key.")
        print("Multiply using the 'x' key.")
        print("Divide using the '/' key.")
        print()


    def calculate_answer(self):
        print()
        print(self.num1, self.operator, self.num2, "=", OPERATIONS[self.operator](self.num1, self.num2))
        print()
   

class Equation:
    def __init__(self, question_prefix):
        self.question_prefix = question_prefix

    def get_number(self):
        while True:
            number = input(f"{self.question_prefix} number: ")
            converted_number = Equation.convert_to_float(number)

            if converted_number == None:
                continue

            return converted_number

            
    def convert_to_float(number):
        converted = None
        try:
            converted = float(number)
        except:
            print("Could not convert", number, "to a float")

        return converted


    def get_operator():
        while True:
            operator = input("Operator: ")
            if operator not in OPERATIONS:
                continue
            return operator



Calculator.instructions()
num1 = Equation(question_prefix="First").get_number()
operator = Equation.get_operator()
num2 = Equation(question_prefix="Second").get_number()
calculator = Calculator(num1=num1, operator=operator, num2=num2) 
calculator.calculate_answer()


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
