# AND = &
# OR = |
# NOT = ~
# LSHIFT = <<
# RSHIFT = >>
import os


def input_list() -> list:
    input_ = open("/Users/riobeggs/Downloads/day7.txt", "r")
    input_ = input_.read().split("\n")
    input_ = input_[:-1]
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
            
            continue    

        if "OR" in line:
            variable = extract_variable(line)

            if variable[0] not in variable_list:
                variable_list.append(variable[0])
            
            if variable[1] not in variable_list:
                variable_list.append(variable[1])      

            if variable[2] not in variable_list:
                variable_list.append(variable[2]) 
            
            continue

        if "NOT" in line:
            variable = extract_variable(line)   

            if variable[0] not in variable_list:
                variable_list.append(variable[0])
            
            if variable[1] not in variable_list:
                variable_list.append(variable[1])
            
            continue 

        if "LSHIFT" in line:
            variable = extract_variable(line)

            if variable[0] not in variable_list:
                variable_list.append(variable[0])
            
            if variable[2] not in variable_list:
                variable_list.append(variable[2])
            
            continue

        if "RSHIFT" in line:
            variable = extract_variable(line)

            if variable[0] not in variable_list:
                variable_list.append(variable[0])
            
            if variable[2] not in variable_list:
                variable_list.append(variable[2]) 
            
            continue

        else:
            variable = line.replace("->", ",").replace(" ", "")  
            variable = variable.split(",") 

            try:
                int(variable[0])
            except:
                if variable[0] not in variable_list:
                    variable_list.append(variable[0])

            try:
                int(variable[1])
            except:            
                if variable[1] not in variable_list:
                    variable_list.append(variable[1])
            
            continue

    return variable_list


def make_value_list(variable_list : list) -> list:
    value_list = []

    for variable in variable_list:
        value_list.append(None)

    return value_list


def recursion_loop(input_ : list, variable_list : list, value_list : list) -> None:
    for line in input_:
        pass


class Bitwise_operators:
    def __init__(self, line, value_list, variable_list) -> None:
        self.line = line
        self.value_list = value_list
        self.variable_list = variable_list


    def AND(self) -> None:
        variable_0 = self.line[0]
        variable_0 = self.value_list[self.variable_list.index(variable_0)]

        variable_1 = self.line[1]
        variable_1 = self.value_list[self.variable_list.index(variable_1)]

        variable_2 = self.line[2]
        variable_2 = self.value_list[self.variable_list.index(variable_2)]

        variable_2 += variable_0 & variable_1


    def OR(self) -> None:
        variable_0 = self.line[0]
        variable_0 = self.value_list[self.variable_list.index(variable_0)]

        variable_1 = self.line[1]
        variable_1 = self.value_list[self.variable_list.index(variable_1)]

        variable_2 = self.line[2]
        variable_2 = self.value_list[self.variable_list.index(variable_2)]

        variable_2 += variable_0 | variable_1


    def NOT(self) -> None:
        variable_0 = self.line[0]
        variable_0 = self.value_list[self.variable_list.index(variable_0)]

        variable_1 = self.line[1]
        variable_1 = self.value_list[self.variable_list.index(variable_1)]

        variable_1 += ~variable_0


    def LSHIFT(self) -> None:
        variable_0 = self.line[0]
        variable_0 = self.value_list[self.variable_list.index(variable_0)]

        variable_1 = int(self.line[1])

        variable_2 = self.line[2]
        variable_2 = self.value_list[self.variable_list.index(variable_2)]

        variable_2 = variable_0 << variable_1    


    def RSHIFT(self) -> None:
        variable_0 = self.line[0]
        variable_0 = self.value_list[self.variable_list.index(variable_0)]

        variable_1 = int(self.line[1])

        variable_2 = self.line[2]
        variable_2 = self.value_list[self.variable_list.index(variable_2)]

        variable_2 = variable_0 >> variable_1 


def wire_a(variable_list : list, value_list : list) -> int:
    a_index = variable_list.index("a")

    return value_list[a_index]


def main() -> None:
    input_ = input_list()
    input_ = ['x AND y -> z']
    variable_list = make_variable_list(input_)
    value_list = make_value_list(variable_list)
    # recursion_loop(input_, variable_list, value_list)

    for line in input_:
        operators = Bitwise_operators(line=line, value_list=value_list, variable_list=value_list)

        if "AND" in line:
            variable = line.replace("AND", ",").replace("->", ",").replace(" ", "")
            variable = variable.split(",")
            operators.AND()

        
        



    print(wire_a(variable_list, value_list))


if __name__ == "__main__":
    main()