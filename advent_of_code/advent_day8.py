def non_raw_string_list() -> list:
    non_raw = open("/Users/riobeggs/Downloads/day8.txt", "r")
    non_raw = non_raw.read().split("\n")
    non_raw = non_raw[:-1]
    return non_raw


def raw_string_list() -> list:
    raw = open("/Users/riobeggs/Downloads/day8.txt", "r")
    raw = raw.read().split("\n")
    raw = raw[:-1]
    raw = ["r" + string for string in raw]
    return raw


def character_counter(non_raw) -> int:
    characters = 0
    for string in non_raw:
        index_ = 0
        for character in string:
            index_ += 1
            if index_ == 1:
                continue
            if index_ == len(string):
                continue
            characters += 1
    return characters


def code_counter(raw) -> int:
    code = 0
    for string in raw:
        code += len(string)
    return code    


def total(characters, code) -> None:
    total = code - characters
    
    print("\ncharacters =", characters)
    print("code =", code)
    print("total =", total)
    print()


def main() -> None:
    # non_raw = non_raw_string_list()
    # raw = raw_string_list()

    non_raw = ['""', '"abc"', '"aaa\"aaa"', '"\x27"']
    raw = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']

    characters = character_counter(non_raw)
    code = code_counter(raw)

    total(characters, code)


if __name__ == "__main__":
    main()