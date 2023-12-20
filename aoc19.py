import json
import copy

workflows = {}
parts = []

with open ("input_19.txt", "r") as myfile:
    datasets=myfile.read().split("\n\n")

    for wf in datasets[0].splitlines():
        #read wf until {
        key = wf.split("{")[0].strip()
        #read content between { and }
        value = wf.split("{")[1].split("}")[0].strip()
        workflows[key] = value

    for stringpart in datasets[1].splitlines():
        stringpart = stringpart.replace("=", '":').replace('{', '{"').replace(',', ',"').replace('}', '}') 
        parts.append(json.loads(stringpart))


def do_operation(operation, part):
    if len(operation.split(":")) != 2:
        return operation
    (op, res) = operation.split(":")
    if len(op.split("<")) == 2:
        if int(part[op.split("<")[0]]) < int(op.split("<")[1]):
            return res 
    if len(op.split(">")) == 2:
        if int(part[op.split(">")[0]]) > int(op.split(">")[1]):
            return res 
    return None


def do_workflow(part, workflowID):
    #print("> {}".format(workflowID), end=" ")
    wf = workflows[workflowID] 
    for op in wf.split(","):
        res = do_operation(op, part)
        if res == None:
            continue
        elif res == "R":
            return False
        elif res == "A":
            return True
        return do_workflow(part, res)
    assert("No result found")
        

def evaluate_part(part):
    sum = 0
    for k, v in part.items():
        sum += v
    return sum


sums = 0
for i, part in enumerate(parts):
    #print("\nPart {}: ".format(i), end="")
    if do_workflow(part, "in"):
        sums += evaluate_part(part)

print("\nPART1: {}".format(sums))

# part 2 

initranges = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000], "ops": []}


def apply_range(op, ranges):
    if len(op.split("<")) == 2:
        key = op.split("<")[0]
        ranges[key][1] = min(int(op.split("<")[1])-1, ranges[key][1])
        return ranges
         
    if len(op.split(">")) == 2:
        key = op.split(">")[0]
        ranges[key][0] = max(int(op.split(">")[1])+1, ranges[key][0])
        return ranges
    assert("No result found")

def apply_contra_range(op, ranges):
    if len(op.split("<")) == 2:
        key = op.split("<")[0]
        ranges[key][0] = max(int(op.split("<")[1]), ranges[key][0])
        return ranges
         
    if len(op.split(">")) == 2:
        key = op.split(">")[0]
        ranges[key][1] = min(int(op.split(">")[1]), ranges[key][1])
        return ranges
    assert("No result found")

def evalcombi(comb):
    sum = 1
    for k, v in comb.items():
        if k == "ops":
            continue
        sum *= v[1] - v[0] +1
    return sum  

def check_range(ranges):
    for k, v in ranges.items():
        if k == "ops":
            continue
        if v[0] >= v[1]:
            return False
    #print("Valid range: {}".format(ranges))
    return True


states = [("in", initranges)]

sum = 0

while len(states) != 0:

    new_states = []
    for (wf, state) in states:
        if check_range(state) == False:
            #print("Invalid range: {}".format(state))
            continue

        if wf == "R":
            #print("R {}".format(state))
            continue

        if wf == "A":
            #print("A {}".format(state))
            sum += evalcombi(state)
            continue

        workflow = workflows[wf]
        for i, wfstep in enumerate(workflow.split(",")):
            bufferstate = copy.deepcopy(state)
            bufferstate["ops"].append(wfstep) 
            if ":" not in wfstep:
                new_states.append((wfstep, bufferstate))
                continue
            (op, nextwf) = wfstep.split(":")
            new_state = apply_range(op, bufferstate)

            new_states.append((nextwf, new_state))

            state = apply_contra_range(op, state)
    states = new_states

print("PART2 {}".format(sum))



    

