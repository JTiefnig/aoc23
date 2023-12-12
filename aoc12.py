parsed_input = []

with open('input_12.txt') as f:
    for line in f:
        lsplit = line.split(" ")
        if len(lsplit) != 2:
           continue
        engineer = [int(x) for x in lsplit[1].split(',')]
        parsed_input.append([lsplit[0], engineer])
 
patterns = {}

def combi_try(line_sub, eng_notes):
    combinations = 0

    patternid = line_sub+str(eng_notes)

    if patternid in patterns:
        return patterns[patternid]
 
    if len(eng_notes) == 0:
        if any([x == "#" for x in line_sub ]):
            return 0
        return 1
 
    for i in range(len(line_sub)-sum(eng_notes)+1):
        if all([x != '.' for x in line_sub[i:i + eng_notes[0]]]):
            if len(line_sub) == (i + eng_notes[0]) or line_sub[i + eng_notes[0]] != "#":
                combinations += combi_try(line_sub[i + eng_notes[0] + 1:], eng_notes[1:])
       
        if line_sub[i] == '#':
            break

    patterns[patternid] = combinations
    return combinations


combinations_sum = 0
for line in parsed_input:
    combinations = combi_try(line[0], line[1])
    combinations_sum += combinations
    #print("{} comb: {}".format(line , combinations))
    

print("result 1: {}".format(combinations_sum))


#PART 2
combinations_sum = 0

for i, line in enumerate(parsed_input):
    multiMap= ""
    multiEng= []

    for x in range(5):
        if x != 0:
            multiMap += "?"
        multiMap += line[0]
        multiEng.extend(line[1])

    combinations = combi_try(multiMap, multiEng)
    print("{}: {}".format(i, combinations))
    combinations_sum += combinations

print("result 2: {}".format(combinations_sum))


