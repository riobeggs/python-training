


# grid[0][1] = 1
# grid[0][2] = 1
# grid[1][0] = 1
# grid[1][1] = 1

# coordinates = [x1 = 0, y1 = 1] : [x2 = 1, y2 = 1]

# x = 0 y = 1
# x = 0 y = 2
# x = 1 y = 0
# x = 1 y = 1

# for x in range(x1 , x2 + 1):
    # for y in range(y1 + x, y2 + 1)
        # grid[x][y]
        # x += 1






grid = [[0, 0 ,0,], [0 ,0 ,0], [0, 0, 0]]

# outcome should be 
# grid = [[0, 1, 1], [1, 1, 0], [0 ,0 ,0]]

coordinates = [0,1,1,1]
x1 = coordinates[0]
y1 = coordinates[1]
x2 = coordinates[2]
y2 = coordinates[3]

for x in range(x1, x2 + 1):
    for y in range(y1 + x, y2 + 1):
        grid[x][y] = 1
        x += 1

grid[x][y] = 1

print(grid)











# x1 = 0
# y1 = 1
# x2 = 1
# y2 = 1

# for x in range(x1, x2 + 1):
#     for y in range(y1, y2 + 1):
#         grid[x][y] = 1

# print(grid)




# for x in range(x1, x2 + 1):
#     for y in range(y1, y2 + 1):
#         print(x) 
#         print(y)











# grid = []

# for row in range(3):
#     for col in range(3):
#         grid.append(0)

# input_ = "turn on 0,1 through 1,1"

# if "turn on" in input_:
#     input_ = input_.replace("turn on ", "").replace(" through ", ",")
#     input_ = input_.split(",")

# x1, y1, x2, y2 = input_[0], input_[1], input_[2], input_[3]
# x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

# for i in range(y2 + 1):
#     grid[x1 : x2 + 1] = [1] * ((x2 - x1 + 1))
#     print(len(grid[x1 : x2 + 1]))


# print(sum(grid))

# grid["000", "000", "000"]