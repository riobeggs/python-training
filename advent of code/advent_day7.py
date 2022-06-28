import os


# part 1
def input_list() -> list:
    input_ = open("/Users/riobeggs/Downloads/day7.txt", "r")
    input_ = input_.read().split("\n")
    input_ = input_[:-1]
    return input_


def is_integer(variable) -> bool:
    try:
        variable = int(variable)
        return True
    except:
        return False


def AND(line : str, variable_list : list, value_list : list) -> None:
    variable = line.replace("AND", ",").replace("->", ",").replace(" ", "")
    variable = variable.split(",")

    if variable[0] not in variable_list:
        if is_integer(variable[0]) == False:
            variable_list.append(variable[0])
            value_list.append(None)
            variable_0 = variable[0]
            variable_0 = value_list[variable_list.index(variable_0)]            
        else:
            variable_0 = int(variable[0])
    else:
        variable_0 = variable[0]
        variable_0 = value_list[variable_list.index(variable_0)]    
            
    if variable[1] not in variable_list:
        if is_integer(variable[1]) == False:        
            variable_list.append(variable[1])
            value_list.append(None)    
            variable_1 = variable[1]
            variable_1 = value_list[variable_list.index(variable_1)]
        else:
            variable_1 = int(variable[1]) 
    else:
        variable_1 = variable[1]
        variable_1 = value_list[variable_list.index(variable_1)]

    if variable[2] not in variable_list:
        if is_integer(variable[2]) == False:  
            variable_list.append(variable[2]) 
            value_list.append(None) 
            variable_2 = variable[2]
            variable_2 = value_list[variable_list.index(variable_2)]
        else:
            variable_2 = int(variable[2])   

    try:
        value_list[variable_list.index(variable[2])] = variable_0 & variable_1
    except:
        pass


def OR(line : str, variable_list : list, value_list : list) -> None:
    variable = line.replace("OR", ",").replace("->", ",").replace(" ", "")
    variable = variable.split(",")\

    if variable[0] not in variable_list:
        if is_integer(variable[0]) == False:
            variable_list.append(variable[0])
            value_list.append(None)
            variable_0 = variable[0]
            variable_0 = value_list[variable_list.index(variable_0)]            
        else:
            variable_0 = int(variable[0])
    else:
        variable_0 = variable[0]
        variable_0 = value_list[variable_list.index(variable_0)]    
            
    if variable[1] not in variable_list:
        if is_integer(variable[1]) == False:        
            variable_list.append(variable[1])
            value_list.append(None)    
            variable_1 = variable[1]
            variable_1 = value_list[variable_list.index(variable_1)]
        else:
            variable_1 = int(variable[1]) 
    else:
        variable_1 = variable[1]
        variable_1 = value_list[variable_list.index(variable_1)]

    if variable[2] not in variable_list:
        if is_integer(variable[2]) == False:  
            variable_list.append(variable[2]) 
            value_list.append(None) 
            variable_2 = variable[2]
            variable_2 = value_list[variable_list.index(variable_2)]
        else:
            variable_2 = int(variable[2])   

    try:
        value_list[variable_list.index(variable[2])] = variable_0 | variable_1
    except:
        pass 


def NOT(line : str, variable_list : list, value_list : list) -> None:
    variable = line.replace("NOT", "").replace("->", ",").replace(" ", "")
    variable = variable.split(",") 

    if variable[0] not in variable_list:
        if is_integer(variable[0]) == False:
            variable_list.append(variable[0])
            value_list.append(None)
            variable_0 = variable[0]
            variable_0 = value_list[variable_list.index(variable_0)]            
        else:
            variable_0 = int(variable[0])
    else:
        variable_0 = variable[0]
        variable_0 = value_list[variable_list.index(variable_0)]


    if variable[1] not in variable_list:
        if is_integer(variable[1]) == False:        
            variable_list.append(variable[1])
            value_list.append(None)    
            variable_1 = variable[1]
            variable_1 = value_list[variable_list.index(variable_1)]
        else:
            variable_1 = int(variable[1]) 
    else:
        variable_1 = variable[1]
        variable_1 = value_list[variable_list.index(variable_1)]

    try:
        value_list[variable_list.index(variable[1])] = ~variable_0
    except:
        pass


def LSHIFT(line : str, variable_list : list, value_list : list) -> None:
    variable = line.replace("LSHIFT", ",").replace("->", ",").replace(" ", "")
    variable = variable.split(",")

    if variable[0] not in variable_list:
        if is_integer(variable[0]) == False:
            variable_list.append(variable[0])
            value_list.append(None)
            variable_0 = variable[0]
            variable_0 = value_list[variable_list.index(variable_0)]            
        else:
            variable_0 = int(variable[0])
    else:
        variable_0 = variable[0]
        variable_0 = value_list[variable_list.index(variable_0)] 

    if variable[2] not in variable_list:
        if is_integer(variable[2]) == False:
            variable_list.append(variable[2])
            value_list.append(None)
            variable_2 = variable[2]
            variable_2 = value_list[variable_list.index(variable_2)]            
        else:
            variable_2 = int(variable[2])
    else:
        variable_2 = variable[2]
        variable_2 = value_list[variable_list.index(variable_2)]    
    
    variable_1 = int(variable[1])

    try:
        value_list[variable_list.index(variable[2])] = variable_0 << variable_1   
    except:
        pass


def RSHIFT(line : str, variable_list : list, value_list : list) -> None:
    variable = line.replace("RSHIFT", ",").replace("->", ",").replace(" ", "")
    variable = variable.split(",")

    if variable[0] not in variable_list:
        if is_integer(variable[0]) == False:
            variable_list.append(variable[0])
            value_list.append(None)
            variable_0 = variable[0]
            variable_0 = value_list[variable_list.index(variable_0)]            
        else:
            variable_0 = int(variable[0])
    else:
        variable_0 = variable[0]
        variable_0 = value_list[variable_list.index(variable_0)] 

    if variable[2] not in variable_list:
        if is_integer(variable[2]) == False:
            variable_list.append(variable[2])
            value_list.append(None)
            variable_2 = variable[2]
            variable_2 = value_list[variable_list.index(variable_2)]            
        else:
            variable_2 = int(variable[2])
    else:
        variable_2 = variable[2]
        variable_2 = value_list[variable_list.index(variable_2)]    
    
    variable_1 = int(variable[1])

    try:
        value_list[variable_list.index(variable[2])] = variable_0 >> variable_1   
    except:
        pass


def PROVIDED(line : str, variable_list : list, value_list : list) -> None:
    variable = line.replace("->", ",").replace(" ", "")  
    variable = variable.split(",") 

    try:
        variable_0 = int(variable[0])
        variable_1 = variable[1]
        if variable_1 not in variable_list:
            variable_list.append(variable_1)
            value_list.append(None)
        value_list[variable_list.index(variable_1)] = variable_0
    except:
        if variable[0] not in variable_list:
            variable_list.append(variable[0])
            value_list.append(None)
        else:
            value_list[variable_list.index(variable[1])] = value_list[variable_list.index(variable[0])]    


    try:
        variable_1 = int(variable[1])
        variable_0 = variable[0]
        if variable_0 not in variable_list:
            variable_list.append(variable_0)
            value_list.append(None)
        value_list[variable_list.index(variable_0)] = variable_1
    except:            
        if variable[1] not in variable_list:
            variable_list.append(variable[1])
            value_list.append(None)   


def run1(input_ : list, variable_list : list, value_list :list) -> list:
    while None in value_list:
        if len(value_list) == 1:
            value_list = value_list[1:]

        for line in input_:
            if "AND" in line:
                AND(line, variable_list, value_list)
                continue    

            if "OR" in line:
                OR(line, variable_list, value_list)        
                continue    

            if "NOT" in line:
                NOT(line, variable_list, value_list)
                continue    

            if "LSHIFT" in line:        
                LSHIFT(line, variable_list, value_list)
                continue 

            if "RSHIFT" in line:        
                RSHIFT(line, variable_list, value_list)
                continue

            PROVIDED(line, variable_list, value_list)
            continue

    return value_list


def wire_a1(variable_list : list, value_list : list) -> int:
    a_index = variable_list.index("a")

    return value_list[a_index]


#part 2
def run2(input_ : list, variable_list : list, value_list :list) -> list:
    while None in value_list:
        if len(value_list) == 2:
            value_list = value_list[1:]

        for line in input_:
            if line == "44430 -> b":
                continue

            if "AND" in line:
                AND(line, variable_list, value_list)
                continue    

            if "OR" in line:
                OR(line, variable_list, value_list)        
                continue    

            if "NOT" in line:
                NOT(line, variable_list, value_list)
                continue    

            if "LSHIFT" in line:        
                LSHIFT(line, variable_list, value_list)
                continue 

            if "RSHIFT" in line:        
                RSHIFT(line, variable_list, value_list)
                continue

            PROVIDED(line, variable_list, value_list)
            continue

    return value_list


def wire_a2(variable_list : list, value_list : list) -> int:
    a_index = variable_list.index("a")

    return value_list[a_index]


def main() -> None:
    input_ = input_list()

    variable_list1 = []
    value_list1 = [None]
    value_list1 = run1(input_, variable_list1, value_list1)
    wire_a = wire_a1(variable_list1, value_list1)
    print(wire_a)

    variable_list2 = ["b"]
    value_list2 = [None, wire_a]
    value_list2 = run2(input_, variable_list2, value_list2)
    wire_a = wire_a2(variable_list2, value_list2)
    print(wire_a)


if __name__ == "__main__":
    main()