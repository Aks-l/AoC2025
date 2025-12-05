goods = set()
day1 = 0

with open ("day5.txt") as f:
    lines = f.readlines()

    ranges, items = list(map(str.strip, lines[:lines.index("\n")])),list(map(str.strip, lines[lines.index("\n")+1:]))
    # Not-enough-memory-solution for part 1
    '''
    for i in ranges:
        a, b = map(int, i.split("-"))
        goods.update(range(a, b + 1))

    
    for i in items:
        if int(i) in goods: day1 += 1
    '''

    # Working solution to part 1
    '''
    for i in items:
        i = int(i)

        for j in ranges:
            a,b = map(int, j.split("-"))
            if i >= a and i <= b:
                day1 += 1
                break
                '''
    day2 = 0
    sorted_ranges = sorted([[a,b] for a,b in (map(int, i.split("-")) for i in ranges)]) 
    for i in range(len(sorted_ranges)-1):
        a,b,c,d = *sorted_ranges[i], *sorted_ranges[i+1]
        if b >=c: day2 -= 1 # Remove overlapping ranges
        sorted_ranges[i+1] = [max(b,c), max(b, d)]
        day2 += b-a +1
   
    day2+= sorted_ranges[-1][1] - sorted_ranges[-1][0] + 1 # one more since loop ends early

    
#print(day1)
print(day2)
