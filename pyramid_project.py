#converts an input to an integer and returns it
def convert_to_int(input):
    converted = None
    try:
        converted = int(input)
    except: 
        pass

    return converted
#gets the users input for the height of the pyramid and returns it
#loops until input is an integer bigger than 0
def pyramid_height():
  while True:
    height = input("\nPyramid height: ") 
    chosen_height = convert_to_int(height)
    if chosen_height == None:
      print("Please enter a number")
      continue
    elif chosen_height <=0:
      print("Please enter a positive number")
      continue
    else:
      return chosen_height

#prints the structure of the pyramid for the given height
def pyramid_structure(chosen_height):
  print("\n")
  for i in range(chosen_height):
    x = i+1  
    for y in range(chosen_height-x):
      print(" ", end="")
    for z in range((2*i)+1):
      print("*", end="")
    print("")
  print("\n")

#calls functions
def main():
  chosen_height = pyramid_height()
  pyramid_structure(chosen_height)

#excecutes main()
if __name__ == "__main__":
  main()

