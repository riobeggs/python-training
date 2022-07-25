def input_list() -> list:
    input_ = open("/Users/riobeggs/Downloads/day8.txt", "r")
    input_ = input_.read().split("\n")
    input_ = input_[:-1]
    return input_


def character_tuple() -> tuple:
    characters = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
    return characters


def character_amount() -> int:
    character_amount = 0


def code_amount() -> int:
    code_amount = 0


def main() -> None:
    # input_ = input_list()
    input_ = ['"aaa\"aaa"']
    characters = character_tuple()
    for i in input_:
        print(len(i))
        print(i)

if __name__ == "__main__":
    main()