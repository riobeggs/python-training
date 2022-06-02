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
    def __init__(self, question_prefix, number, converted_number, operator):
        self.question_prefix = question_prefix
        self.number = number
        self.converted_number = converted_number
        self.operator = operator


    def get_number(self):
        while True:
            self.number = input(f"{self.question_prefix} number: ")
            self.converted_number = Equation._convert_to_float(self.number)

            if self.converted_number == None:
                continue

            return self.converted_number

            
    def _convert_to_float(number):
        """As this class is never called externally, we prefix it with an "_". 
        
        Attempts to convert a number to a float.
        """
        converted = None
        try:
            converted = float(number)
        except:
            print("Could not convert", number, "to a float")

        return converted


    def get_operator(self):
        while True:
            self.operator = input("Operator: ")
            if self.operator not in OPERATIONS:
                continue
            return self.operator



Calculator.instructions()
num1 = Equation(question_prefix="First", number=None, converted_number=None, operator=None).get_number()
operator = Equation(question_prefix=None, number=None, converted_number=None, operator=None).get_operator()
num2 = Equation(question_prefix="Second", number=None, converted_number=None, operator=None).get_number()
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
