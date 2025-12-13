
import numpy as np
from collections import deque

idx = []
with open("day9.txt") as f:
    for line in f:
        x, y = map(int, line.strip().split(","))
        idx.append((x, y))
maximum = 0

green_map = np.zeros((100000,100000), dtype=bool)
for i in range(len(idx)):
    x1,y1,x2,y2 = idx[i][0], idx[i][1], idx[(i+1)%len(idx)][0], idx[(i+1)%len(idx)][1]
    #print(x1, y1, x2, y2)
    green_map[x1:x2+1, y1:y2+1] = True
    green_map[x2:x1+1, y2:y1+1] = True

#print(green_map.T)

h, w = green_map.shape
visited = np.zeros_like(green_map, dtype=bool)

q = deque()
q.append((8,2))
visited[8, 2] = True

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w:
            if not visited[nx, ny] and not green_map[nx, ny]:
                visited[nx, ny] = True
                q.append((nx, ny))

part2_map = np.logical_or(visited, green_map)

for i in range(len(idx)):
    for j in range(i+1, len(idx)):
        x1,y1,x2,y2 = idx[i][0], idx[i][1], idx[j][0], idx[j][1]
        if not np.all(part2_map[min(x1, x2):max(x1, x2)+1, min(y1, y2):max(y1, y2)+1]):
            continue

        dx, dy = max(x1, x2) - min(x1, x2), max(y1, y2) - min(y1, y2)
        area = (dx+1) * (dy+1)
        #print(x1, y1, x2, y2, area)
        maximum = max(maximum, area)
    print(i)


#print(np.logical_or(visited, green_map).T)

print(maximum)