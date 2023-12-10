# A very ugly solution sorry xD 


input_arr = []
startpos = (0,0)

breadCrumbs = [] 

with open("input_10.txt") as f:
    lines = f.readlines()
    for y, line in enumerate(lines):
        linearr = []
        for x, c in enumerate(line.strip()):
            linearr.append(c)
            if c == "S":
                startpos = (x,y)
        input_arr.append(linearr)

breadCrumbs = [["." for x in range(len(lines[0]))] for y in range(len(lines))]

pipes = {
    "|": [(0,1), (0,-1)],
    "-": [(1,0), (-1,0)],
    "L": [(0,-1), (1,0)],
    "J": [(0,-1), (-1,0)],
    "7": [(0,1), (-1,0)],
    "F": [(0,1), (1,0)],
    "S": [(0,1), (0,-1), (1,0), (-1,0)],
    ".": []
}

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this 

def gp(pos):
    return input_arr[pos[1]][pos[0]]


longest = 0

for d in pipes[gp(startpos)]:
    distance = 0
    pos = startpos
    dir = d
    while True:
        #print("### {} ### next move".format(gp(pos), dir))
        pos = (pos[0] + dir[0], pos[1] + dir[1])
        distance += 1
        #check bounds
        if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(input_arr[0]) or pos[1] >= len(input_arr):
            print("out of bounds pos:{} form dir {}".format(gp(pos), dir))
            break

        breadCrumbs[pos[1]][pos[0]] = "#"
        
        if gp(pos) == "S":
            print("S{}".format(distance))
            if distance > longest:
                longest = distance
            break

        if not any([d for d in pipes[gp(pos)] if d == (-dir[0], -dir[1])]):
            print("dead end pos:{} form dir {}".format(gp(pos), dir))
            break

        newdir = [d for d in pipes[gp(pos)] if d != (-dir[0], -dir[1])][0]

        #inside marker
        im = (pos[0] + dir[1], pos[1] - dir[0])
        if im[0] >= 0 and im[1] >= 0 and im[0] < len(input_arr[0]) and im[1] < len(input_arr):
            if breadCrumbs[im[1]][im[0]] == ".":
                breadCrumbs[im[1]][im[0]] = "I"

        im = (pos[0] + newdir[1], pos[1] - newdir[0])
        if im[0] >= 0 and im[1] >= 0 and im[0] < len(input_arr[0]) and im[1] < len(input_arr):
            if breadCrumbs[im[1]][im[0]] == ".":
                breadCrumbs[im[1]][im[0]] = "I"

        dir = newdir

        # print("pos {} to dir {}".format(gp(pos), dir))
    if longest > 0:
        break


print("--- Result ---")
print(longest//2)

def recursivefill(prepos):
    pattern = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for div in pattern:
        pos = (prepos[0]+div[0], prepos[1]+div[1])
        if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(breadCrumbs[0]) or pos[1] >= len(breadCrumbs):
            continue
        if breadCrumbs[pos[1]][pos[0]] != ".":
            continue
        breadCrumbs[pos[1]][pos[0]] = "I"


for y, brow in enumerate(breadCrumbs):
    for x, b in enumerate(brow):
        if b == "I":
            recursivefill((x, y))


i_count = 0

for line in breadCrumbs:
    for c in line:
        if c == "I":
            i_count += 1
    print("".join(line))

print("Result 2: {}".format(i_count))



