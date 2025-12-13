lines = list(map(str.strip, [*open("day7.txt")]))

day1 = 0
rays = {}

rays[lines[0].index('S')]=1

for i in lines[1:]:
    split_idx = [j for j in range(len(i)) if i[j] == '^']
    if split_idx:
        for j in split_idx:
            if rays.get(j,0) != 0 :day1+=1
            if j in rays.keys():
                rays[j-1] = rays.get(j-1,0) + rays[j]
                rays[j+1] = rays.get(j+1,0) + rays[j]
                rays[j] = 0
        
print(day1)
print(sum(rays.values()))