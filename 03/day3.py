lines = map(str.strip, [*open("day3.txt")])
part2 = 0
idx=0
'''for i in lines:
    i = i.strip()
    tot_idx = 0
    hi, _, idx0 = max([(a,-idx, idx) for idx,a in enumerate(i[:len(i)-11])])
    tot_idx += idx0 +1
    lo1, _, idx1 = max([(a,-idx, idx) for idx,a in enumerate(i[tot_idx:len(i)-10])])
    tot_idx += idx1 +1
    lo2, _, idx2 = max([(a,-idx, idx) for idx,a in enumerate(i[tot_idx:len(i)-9])])
    tot_idx += idx2 +1
    lo3, _, idx3 = max([(a,-idx, idx) for idx,a in enumerate(i[tot_idx:len(i)-8])])
    tot_idx += idx3 +1
    lo4, _, idx4 = max([(a,-idx, idx) for idx,a in enumerate(i[tot_idx:len(i)-7])])
    tot_idx += idx4 +1
    lo5, _, idx5 = max([(a,-idx, idx) for idx,a in enumerate(i[tot_idx:len(i)-6])])
    tot_idx += idx5 +1
    lo6, _, idx6 = max([(a,-idx, idx) for idx,a in enumerate(i[tot_idx:len(i)-5])])
    tot_idx += idx6 +1
    lo7, _, idx7 = max([(a,-idx, idx) for idx,a in enumerate(i[tot_idx:len(i)-4])])
    tot_idx += idx7 +1
    lo8, _, idx8 = max([(a,-idx, idx) for idx,a in enumerate(i[tot_idx:len(i)-3])])
    tot_idx += idx8 +1
    lo9, _, idx9 = max([(a,-idx, idx) for idx,a in enumerate(i[tot_idx:len(i)-2])])
    tot_idx += idx9 +1
    lo10, _, idx10 = max([(a,-idx, idx) for idx,a in enumerate(i[tot_idx:len(i)-1])])
    tot_idx += idx10 +1
    lo11, _, idx11 = max([(a,-idx, idx) for idx,a in enumerate(i[tot_idx:len(i)])])
    tot_idx += idx11 

    part2 += int(hi+lo1+lo2+lo3+lo4+lo5+lo6+lo7+lo8+lo9+lo10+lo11)'''


for i in lines:

    tot_idx = 0
    sum_vals = ""
    for offset in range(12):
        hi, _, idx0 = max([(a,-idx, idx) for idx,a in enumerate(i[tot_idx:len(i)-(11 - offset)])])
        sum_vals += str(hi)
        tot_idx += idx0 +1
    part2 += int(sum_vals)
        
print(part2)
