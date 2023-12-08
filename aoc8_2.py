import re
import math 
from functools import reduce


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



#getnodes that end with A in the key as a list
nodePointers = [mapHash[k] for k in mapHash.keys() if k.endswith("A")]

print("found {} nodes that end with A".format(len(nodePointers)))

# hint all the cycles loop over exactly one step after reaching the goal. 
# therefore thy all have a fixed length of reaching their goal
# this problem would be much harder if the cycles would reach multiple goals in their cycle


def get_steps_to_goal(node):
    count = 0
    while True:
        for d in directions:
            if(d != "L" and d != "R"):
                # end of direction set
                break
            count+=1

            next_pos = node[d]
            node = mapHash[next_pos]
            if(next_pos.endswith("Z")):
                return count


steps_needed = [get_steps_to_goal(node) for node in nodePointers]

print("steps needed: {}".format(steps_needed))



def lcm_of_list(numbers):
    # LCM of a list of numbers
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)

    return reduce(lcm, numbers)

print(lcm_of_list(steps_needed))


exit()

# BAD Slow solution
count = 0
while True:
    for d in directions:
        if(d != "L" and d != "R"):
            # end of direction set
            break
        count+=1

        goalflag = True

        for id, node in enumerate(nodePointers):
            next_pos = node[d]
            nodePointers[id] = mapHash[next_pos]
            if not next_pos.endswith("Z"):
                goalflag = False

        if(goalflag):
            print("found **Z for all {} at step: {}".format(len(nodePointers),count))
            exit() 

