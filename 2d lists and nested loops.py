number_grid = [
    [1,2,3],            #row 0
    [4,5,6],            #row 1
    [7,8,9],
    [0]
]

print(number_grid[0][0])            #first is row, 2nd is column
print(number_grid[2][1])

#nested for loop

for row in number_grid:
    #print(row)
    for column in row:
        print(column)