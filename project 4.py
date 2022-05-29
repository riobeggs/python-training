#calculator
#tell user how to use the calculator
# + = add , x = multiply , - = minus , / = divide.
#print the answer to their input


#ask for the equation
#if their inpout is exit then exit the program
#if their input is not an integer then ask for equation
#if their input does not take * / + - = then ask for equation



#intro
def instructions():
    print("\n\nYou may use this calculator as many times as you like.")
    print("To exit the calculator, type 'exit', then press enter.")
    print("\nAdd using the '+' key.")
    print("Minus using the '-' key.")
    print("Multiply using the 'x' key.")
    print("Divide using the '/' key.\n\n")


def convert_to_int(equation):
  converted = None
  try:
      converted = int(equation)
  except: 
      pass

  return converted

def first_number():
    while True:
        num1 = input("First number: ")
        converted_num1 = convert_to_int(num1)

        if converted_num1 == None:
            continue

        return converted_num1

#multiplication function

#enter a first number
#enter an operator
#enter a 2nd number


# gets users input/ equation
def get_equation():
    while True:
        equation = input("Equation: ")
        if equation == "exit":
            break

        converted_equation = convert_to_int(equation)
        if converted_equation == None:
            continue
        
        if converted_equation == int(converted_equation):
            return converted_equation
        
        

instructions()
converted_equation = get_equation()
print(converted_equation)
    


