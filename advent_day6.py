import os


def grid_base(grid : list) -> int:
    for x in range(1000):
        for y in range(1000):
            return grid.append(0)


def input_list() -> list:
    input_ = open("/Users/riobeggs/Downloads/day6.txt", "r")
    input_ = input_.read().split("\n")
    input_ = ["turn on 0,0 through 999,999", "turn off 499,499 through 500,500"]
    return input_


def int_coordinate_list(instructions : list, grid : list) -> None:
    x1, y1, x2, y2 = instructions[0], instructions[1], instructions[2], instructions[3]
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    for row in grid[x1 : x2]:
        grid[row] = 1

    # coordinates = [x1, y1, x2, y2]
    # return coordinates


def lights_on(input_ : list) -> str:
    lights_on = 0
    grid = []

    grid_base(grid)

    for instructions in input_:
        if "turn on" in instructions:
            instructions = instructions.replace("turn on ", "").replace(" through ", ",")
            instructions = instructions.split(",")
            coordinates = int_coordinate_list(instructions, grid)
            continue
            
        # if "turn off" in instructions:
        #     instructions = instructions.replace("turn off ", "").replace(" through ", ",")
        #     instructions = instructions.split(",")
        #     coordinates = int_coordinate_list(instructions, grid)
        #     continue

        # if "toggle" in instructions:
        #     instructions = instructions.replace("toggle ", "").replace(" through ", ",")
        #     coordinates = instructions.split(",")
        

    return lights_on


def main() -> None:
    input_ = input_list()
    print(lights_on(input_))


if __name__ == "__main__":
    main()