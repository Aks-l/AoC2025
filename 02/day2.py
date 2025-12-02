total = 0

ranges = [*open("day2.txt")][0].split(",")

for r in ranges:
    a, b = map(int, r.split("-"))

    for i in range(a, b + 1):
        s = str(i)
        l = len(s)

        for d in range(1, l//2+1):
            if l % d != 0:continue

            sub = s[:d]
            if sub*(l//d) == s:
                total += i
                break

print(total)
