import os

def input_list() -> list:
    input_ = open("/Users/riobeggs/Downloads/day6.txt", "r")
    input_ = input_.read().split("\n")
    input_ = ["turn on 0,0 through 999,999", "turn off 499,499 through 500,500"]
    return input_

    
def lights_on(input_ : list) -> str:
    lights_on = 0
    for instructions in input_:
        if "turn on" in instructions:
            instructions = instructions.replace("turn on ", "").replace(" through ", ",")
            coordinates = instructions.split(",")

            x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            x_axis = len(range(x1, x2 + 1))
            y_axis = len(range(y1, y2 + 1))
            area = x_axis * y_axis

            lights_on += area
            continue
            

        if "turn off" in instructions:
            instructions = instructions.replace("turn off ", "").replace(" through ", ",")
            coordinates = instructions.split(",")

            x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            x_axis = len(range(x1, x2 + 1))
            y_axis = len(range(y1, y2 + 1))
            area = x_axis * y_axis

            lights_on -= area
            continue


        if "toggle" in instructions:
            pass

    return lights_on

def main() -> None:
    input_ = input_list()
    print(lights_on(input_))


if __name__ == "__main__":
    main()