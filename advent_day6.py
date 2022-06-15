import os

def input_list() -> list:
    instructions = open("/Users/riobeggs/Downloads/day6.txt", "r")
    instructions = instructions.read()
    instructions = instructions.split("\n")
    return instructions


def lights_on(instructions : list) -> str:
    pass


def main() -> None:
    instructions = input_list()
    lights_on(instructions)


if __name__ == "__main__":
    main()