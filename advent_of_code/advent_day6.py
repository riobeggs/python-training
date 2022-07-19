import os


# part 1
def grid_base() -> list:
    grid = []

    for x in range(1000):
        row = []
        for y in range(1000):
            row.append(0)
        grid.extend([row])

    return grid


def input_list() -> list:
    input_ = open("/Users/riobeggs/Downloads/day6.txt", "r")
    input_ = input_.read().split("\n")
    return input_


def find_coordinates(instructions : list) -> list:
    x1, y1, x2, y2 = instructions[0], instructions[1], instructions[2], instructions[3]
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    coordinates = [x1, y1, x2, y2]
    return coordinates


def lights_on(input_ : list) -> int:
    lights_on = 0
    grid = grid_base()

    for instructions in input_:
        if "turn on" in instructions:
            instructions = instructions.replace("turn on ", "").replace(" through ", ",")
            instructions = instructions.split(",")
            coordinates = find_coordinates(instructions)
            x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[x][y] = 1
            continue
            
        if "turn off" in instructions:
            instructions = instructions.replace("turn off ", "").replace(" through ", ",")
            instructions = instructions.split(",")
            coordinates = find_coordinates(instructions)
            x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[x][y] = 0
            continue

        if "toggle" in instructions:
            instructions = instructions.replace("toggle ", "").replace(" through ", ",")
            instructions = instructions.split(",")
            coordinates = find_coordinates(instructions)
            x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]            
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if grid[x][y] == 0:
                        grid[x][y] = 1
                    else:
                        grid[x][y] = 0

    for row in grid:
        lights_on += sum(row)                    

    return lights_on


# part 2
def brightness(input_ : list) -> int:
    brightness = 0
    grid = grid_base()

    for instructions in input_:
        if "turn on" in instructions:
            instructions = instructions.replace("turn on ", "").replace(" through ", ",")
            instructions = instructions.split(",")
            coordinates = find_coordinates(instructions)
            x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[x][y] +=1
            continue
            
        if "turn off" in instructions:
            instructions = instructions.replace("turn off ", "").replace(" through ", ",")
            instructions = instructions.split(",")
            coordinates = find_coordinates(instructions)
            x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if grid[x][y] == 0:
                        continue
                    grid[x][y] -= 1
            continue

        if "toggle" in instructions:
            instructions = instructions.replace("toggle ", "").replace(" through ", ",")
            instructions = instructions.split(",")
            coordinates = find_coordinates(instructions)
            x1, y1, x2, y2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]            
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    grid[x][y] += 2

    for row in grid:
        brightness += sum(row)                    

    return brightness


def main() -> None:
    input_ = input_list()
    print("lights on:",lights_on(input_))
    print("brightness:", brightness(input_))


if __name__ == "__main__":
    main()