# AND = &
# OR = |
# NOT = ~
# LSHIFT = <<
# RSHIFT = >>
import os


def input_list() -> list:
    input_ = open("/Users/riobeggs/Downloads/day7.txt", "r")
    input_ = input_.read().split("\n")
    return input_


def extract_variable(line : str) -> list:
    if "AND" in line:
        variable = line.replace("AND", ",").replace("->", ",").replace(" ", "")
        variable = variable.split(",")

        return variable


    if "OR" in line:
        variable = line.replace("OR", ",").replace("->", ",").replace(" ", "")
        variable = variable.split(",")

        return variable


    if "NOT" in line:
        variable = line.replace("NOT", "").replace("->", ",").replace(" ", "")
        variable = variable.split(",")

        return variable


    if "LSHIFT" in line:        
        variable = line.replace("LSHIFT", ",").replace("->", ",").replace(" ", "")
        variable = variable.split(",")

        return variable


    if "RSHIFT" in line:        
        variable = line.replace("RSHIFT", ",").replace("->", ",").replace(" ", "")
        variable = variable.split(",")

        return variable

    
    variable = variable.replace("->", ",").replace(" ", "")

    return variable


def make_variable_list(input_ : list) -> list:
    variable_list = []
    for line in input_:

        if "AND" in line:
            variable = extract_variable(line)

            if variable[0] not in variable_list:
                variable_list.append(variable[0])
            
            if variable[1] not in variable_list:
                variable_list.append(variable[1])      

            if variable[2] not in variable_list:
                variable_list.append(variable[2]) 
    

        if "OR" in line:
            variable = extract_variable(line)

            if variable[0] not in variable_list:
                variable_list.append(variable[0])
            
            if variable[1] not in variable_list:
                variable_list.append(variable[1])      

            if variable[2] not in variable_list:
                variable_list.append(variable[2]) 


        if "NOT" in line:
            variable = extract_variable(line)   

            if variable[0] not in variable_list:
                variable_list.append(variable[0])
            
            if variable[1] not in variable_list:
                variable_list.append(variable[1])  


        if "LSHIFT" in line:
            variable = extract_variable(line)

            if variable[0] not in variable_list:
                variable_list.append(variable[0])
            
            if variable[2] not in variable_list:
                variable_list.append(variable[2])
            pass


        if "RSHIFT" in line:
            variable = extract_variable(line)

            if variable[0] not in variable_list:
                variable_list.append(variable[0])
            
            if variable[2] not in variable_list:
                variable_list.append(variable[2]) 


    return variable_list


def make_value_list(variable_list : list) -> list:
    value_list = []

    for variable in variable_list:
        value_list.append(0)

    return value_list


class Bitwise_operators:
    def __init__(self) -> None:
        pass

    def AND(input_) -> None:
        pass

    def OR(input_) -> None:
        pass

    def NOT(input_) -> None:
        pass

    def LSHIFT(input_) -> None:
        pass

    def RSHIFT(input_) -> None:
        pass


def wire_a() -> int:
    pass


def main() -> None:
    input_ = input_list()
    variable_list = make_variable_list(input_)
    value_list = make_value_list(variable_list)
    for instruction in input_:
        Bitwise_operators()

    print(wire_a())


if __name__ == "__main__":
    main()