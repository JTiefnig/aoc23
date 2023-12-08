import re

directions =""

mapHash = {}

#load input
with open('input_8.txt') as f:
    # convert to 2d array
    lines = f.readlines()
    # get frist line
    directions = lines.pop(0)
    lines.pop(0)

    for line in lines:
        pattern = re.compile(r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)')
        match = pattern.match(line)
        mapHash[match.group(1)] = {"L":match.group(2), "R":match.group(3)}

current_pos = mapHash["AAA"]


count = 0
while True:
    for d in directions:
        if(d != "L" and d != "R"):
            # end of direction set
            break
        count+=1

        next_pos = current_pos[d]
        current_pos = mapHash[next_pos]

        if(next_pos == "ZZZ"):
            print("found ZZZ at step: {}".format(count))
            exit()



