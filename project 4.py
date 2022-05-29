import operator

ops = {"+" : operator.add,
       "-" : operator.sub,
       "x" : operator.mul,
       "/" : operator.truediv}


def instructions():
    print("\n\nYou may use this calculator as many times as you like.")
    print("To exit the calculator, type 'exit', then press enter.")
    print("\nAdd using the '+' key.")
    print("Subtract using the '-' key.")
    print("Multiply using the 'x' key.")
    print("Divide using the '/' key.\n")


def convert_to_float(equation):
  converted = None
  try:
      converted = float(equation)
  except: 
      pass

  return converted


def get_first_number():
    while True:
        num1 = input("First number: ")
        converted_num1 = convert_to_float(num1)

        if converted_num1 == None:
            continue

        return converted_num1


def get_operator():
    while True:
        operator = input("Operator: ")

        if operator not in ops:
            continue

        return operator


def get_second_number():
    while True:
        num2 = input("Second number: ")
        print("\n")
        converted_num2 = convert_to_float(num2)

        if converted_num2 == None:
            continue

        return converted_num2


def calculate_answer(num1, operator, num2):
    if operator == "+":
        print(num1, "+", num2, "=", num1 + num2, "\n\n")

    if operator == "-":
        print(num1, "-", num2, "=", num1 - num2, "\n\n")

    if operator == "x":
        print(num1, "x", num2, "=", num1 * num2, "\n\n")

    if operator == "/":
        print(num1, "/", num2, "=", num1 / num2, "\n\n")       

def run_calculator():
    instructions()
    num1 = get_first_number()
    operator = get_operator()
    num2 = get_second_number()
    calculate_answer(num1, operator, num2)


run_calculator()