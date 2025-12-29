from itertools import combinations, permutations, product, combinations_with_replacement

import pulp

tasks = []
total = 0


def switchToBin(switches: (int), length: int):
    out = ""
    for i in range(length):
        out += "1" if str(i) in switches else "0"
    return out

with open("day10.txt") as f:
    for l in f: tasks.append(l.strip())

for task in tasks:
    split = task.split(" ")
    target, switches, joltage = split[0][1:-1], split[1:-1], split[-1].strip()
    targetLen = len(target)
    target = [int(i) for i in joltage[1:-1].split(",")]

    switches = [switchToBin(s, targetLen) for s in switches]

    # pulp init 
    prob = pulp.LpProblem("", pulp.LpMinimize)
    #pulp variable setup
    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat=pulp.LpInteger) for i in range(len(switches))]
    # total rule
    prob += pulp.lpSum(x)
    # individual rules per button
    for j in range(targetLen):
        prob += pulp.lpSum(x[i] for i in range(len(switches)) if switches[i][j] == "1") == target[j]
    # magic
    sol = prob.solve(pulp.PULP_CBC_CMD(msg=False))

    counts = {j: int(pulp.value(xj)) for j, xj in enumerate(x) if int(pulp.value(xj)) != 0}
    depth = sum(counts.values())

    total += depth
    print(depth, counts)

print(total)
