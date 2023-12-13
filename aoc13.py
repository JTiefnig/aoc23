inputs = []

with open("input_13.txt") as f:
    #split file by empty lines
    inputs = f.read().split("\n\n")


def debugOutput(lines, i, scope):
    print("reflection:")
    refs = []
    for j in range(scope):
        refs.append("{} {}".format(i-j-1,lines[i-j-1]))
    refs.reverse()
    for j in range(scope):
        refs.append("{} {}".format(i+j,lines[i+j]))
    for rl in refs:
        print(rl)


def getreflections(inp, tolerance=0):
    reflections = []
    lines = inp.splitlines()
    for i, l in enumerate(lines):
        if i == 0:
            continue
        else:
            scope = min(i, len(lines)-i)
            errorCount = 0 
            for j in range(scope):
                errorCount += len([1 for c1, c2 in zip(lines[i-j-1], lines[i+j]) if c1 != c2])
                if errorCount > tolerance:
                    break
            if errorCount == tolerance:
                 # debugOutput(lines, i, scope)
                 reflections.append(i)

    return reflections


result2 = 0
result1 = 0
for n,input in enumerate(inputs):

    hrefs = getreflections(input)
    #print(hrefs)
    hrefs2 = getreflections(input, 1)
    #print(hrefs2)

    flippedinp = "\n".join(["".join([line[i] for line in input.splitlines()]) for i in range(len(input.splitlines()[0]))])

    vrefs = getreflections(flippedinp)
    #print(vrefs)
    vrefs2 = getreflections(flippedinp, 1)
    #print(vrefs2)

    result1 += sum(hrefs)*100 + sum(vrefs)
    result2 += sum(hrefs2)*100 + sum(vrefs2)


print("result 1: {}".format(result1))
print("result 2: {}".format(result2))