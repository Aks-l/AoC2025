
n = 50
part2 = 0
part1 = 0
with open("day1.txt") as f:
    for l in f:
        d,c=l[0], int(l[1:])

        rounds = c // 100
        part2 += rounds
        c %= 100

        if d == 'L' :
            if n == 0 and c > 0: part2 -=1 # edge case took 15 minutes to spot :(
            if n - c <= 0:
                part2 += 1
            n = (n-c + 100) % 100

        else:
            if n + c >= 100:
                part2 += 1
            n = (n + c + 100) % 100
        
        if n % 100 == 0: part1 += 1

print(part1)
print(part2)