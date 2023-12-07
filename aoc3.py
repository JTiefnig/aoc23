

array = [] 
with open('input_3.txt') as f:
    # convert to 2d array
    lines = f.readlines()
    array = []
    for line in lines:
        arr_line = [c for c in line]
        array.append(arr_line)
    


def adjacentcheck(x, y, array):
    # check if adjacent
    for dy in range(-1, 2):
        if y+dy < 0 or y+dy >= len(array):
            continue
        for dx in range(-1, 2):
            if x+dx < 0 or x+dx >= len(array[y]):
                continue
            if array[y+dy][x+dx] != "." and not array[y+dy][x+dx].isdigit():
                return True
    return False



# iterate over array and find all numbers
numbers = []
for y, line in enumerate(array):
    strnr = ""
    adjacent_flag = False
    for x, c in enumerate(line):
        if c.isdigit():
            strnr += c
            adjacent_flag = adjacentcheck(x, y, array) if not adjacent_flag else True
        else:
            if strnr != "" and adjacent_flag:
                numbers.append(int(strnr))
            strnr = ""
            adjacent_flag = False


print(sum(numbers))

# part 2

def adjacentcheck(x, y, array):
    # check if adjacent
    for dy in range(-1, 2):
        if y+dy < 0 or y+dy >= len(array):
            continue
        for dx in range(-1, 2):
            if x+dx < 0 or x+dx >= len(array[y]):
                continue
            if array[y+dy][x+dx] == "*":
                return (x+dx, y+dy)
    # return null if no adjacent
    return (None, None)


gearcenters = {}
for y, line in enumerate(array):
    strnr = ""
    adjacentgearcenter = ""
    for x, c in enumerate(line):
        if c.isdigit():
            strnr += c
            (x_adj, y_adj) = adjacentcheck(x, y, array)
            if x_adj is not None and y_adj is not None:
                adjacentgearcenter = str(x_adj)+"x"+str(y_adj)
        else:
            if strnr != "" and adjacentgearcenter != "":
                # if add to dict a list
                if adjacentgearcenter not in gearcenters:
                    gearcenters[adjacentgearcenter] = []
                gearcenters[adjacentgearcenter].append(int(strnr))
            strnr = ""
            adjacentgearcenter = ""


sums = 0

for key, value in gearcenters.items():
    if len(value) == 2:
        sums += value[0] * value[1]



print(sums)