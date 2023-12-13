

inputs = []

with open("input_13.txt") as f:
    #split file by empty lines
    inputs = f.read().split("\n\n")


def getreflections(inp):
    reflections = []
    lines = inp.splitlines()
    for i, l in enumerate(lines):
        if i == 0:
            continue
        else:
            scope = min(i, len(lines)-i)
            if all([lines[i-j-1] == lines[i+j] for j in range(scope)]):
                print("reflection:")
                refs = []
                for j in range(scope):
                    refs.append("{} {}".format(i-j-1,lines[i-j-1]))
                refs.reverse()
                for j in range(scope):
                    refs.append("{} {}".format(i+j,lines[i+j]))

                for rl in refs:
                    print(rl)


                reflections.append(i)

    return reflections

result1 =0

for n,input in enumerate(inputs):

    print("N{}".format(n))

    hrefs = getreflections(input)
    print(hrefs)

    flippedinp = "\n".join(["".join([line[i] for line in input.splitlines()]) for i in range(len(input.splitlines()[0]))])

    vrefs = getreflections(flippedinp)
    print(vrefs)

    result1 += sum(hrefs)*100

    result1 += sum(vrefs)


print("result 1: {}".format(result1))
    