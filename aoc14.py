
cgrid = None
with open('input_14.txt') as f:
    lines = f.readlines()
    cgrid = [[c for c in line.strip('\n')] for line in lines]


def printGrid(gird):
    for line in gird:
        print("".join(line))


def movenorth(grid):
    for i, cline in enumerate(grid):
        for j, c in enumerate(cline):
            if c == 'O':
                for d in range(i+1):
                    if i-d-1 < 0 or grid[i-d-1][j] != '.':
                        grid[i][j] = '.'
                        grid[i-d][j] = 'O'
                        break
    return grid


def calcLoad(grid):
    load = 0
    for i, l in enumerate(grid):
        # print("rowf {}".format(llen-i))
        for c in l:
            if c == 'O':
                load += (len(grid)-i)
    return load


print("--- PART 1 ---")
cgrid = movenorth(cgrid)
print(calcLoad(cgrid))

print("--- PART 2 ---")

def rotate90(grid):
    return [[grid[i][j] for i in range(len(grid) - 1, -1, -1)] for j in range(len(grid[0]))] # rotate right
    # return [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]) - 1, -1, -1)] # rotate left

def doCycle(grid):
    for i in range(4):
        grid = movenorth(grid)
        grid = rotate90(grid)
    return grid

cycles= 1000000000

buffer = {}
loopclose = 0
looplength = 0

for i in range(cycles):
    cgrid = doCycle(cgrid)
    id = str(cgrid)
    if id in buffer:
        loopclose = buffer[id][0] # offset of the loop
        looplength = i - buffer[id][0] #length of the loop
        break # break after first loop found
    buffer[id] = (i, calcLoad(cgrid))


resultid = (cycles-loopclose)%looplength+loopclose -1 
#print(resultid)

result = [b[1] for b in buffer.values()][resultid]
print(result)

# old solution: manually look for the cycle
# for v in [b for b in buffer.values()][(resultid-10):]:
#     if v[0] == loopclose:
#         print("x", end="")
#     print("{}".format(v))
# 
# print("resultid: {}".format(resultid))
# print((cycles-102)%9) - then count in the output starting with 1 where the cycle starts

