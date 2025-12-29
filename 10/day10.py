from itertools import combinations

tasks = []
total = 0

def switchToBin(switches: (int), length: int):
    out = ""
    for i in range(length):
        out += "1" if str(i) in switches else "0"
    return out

def xor(a: str, b: str):
    out = ""
    assert(len(a) == len(b))
    for i in range(len(a)):
        out += "0" if a[i] == b[i] else "1"
    return out

with open("day10.txt") as f:
    for l in f: tasks.append(l)

for task in tasks:
    split = task.split(" ")
    target, switches, joltage = split[0][1:-1], split[1:-1], split[-1]
    targetLen = len(target)
    target = target.replace(".", "0").replace("#", "1")
    switches = [switchToBin(tuple(i), targetLen) for i in switches]

    found = False
    depth = 0

    while not found:
        depth += 1
        toTest = list(combinations(switches, depth))
        for test in toTest:
            start = "0"*targetLen
            for switch in test:
                start = xor(start, switch)
            if start == target:
                found = True

    total += depth

print(total)

        

    

        