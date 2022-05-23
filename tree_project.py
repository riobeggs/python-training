# Create code to print trees
def convert_to_int(input):
    converted = None
    try:
        converted = int(input)
        return converted
    except: 
        pass

def tree_height():
  while True:
    height = input("\nTree height: ") 
    chosen_height = convert_to_int(height)
    if chosen_height == None:
      print("Please enter a number.")
      continue
    elif chosen_height <=0:
      print("Please enter a positive number.")
      continue
    else:
      return chosen_height

def tree_structure(chosen_height):
  print("\nYou chose the height of:", chosen_height, "\n")
  for i in range(chosen_height):
    x = i+1
    if i <= x:
        print("*", end="")
    else:
      continue


def main():
  chosen_height = tree_height()
  tree_structure(chosen_height)

if __name__ == "__main__":
  main()

