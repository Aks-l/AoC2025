
import numpy as np
from collections import deque
from shapely import Polygon, Point, LineString

idx = []
with open("day9.txt") as f:
    for line in f:
        x, y = map(int, line.strip().split(","))
        idx.append((x, y))
maximum = 0

green_map = Polygon(idx)


for i in range(len(idx)):
    for j in range(i+1, len(idx)):
        x1,y1,x2,y2 = idx[i][0], idx[i][1], idx[j][0], idx[j][1]
        box = Polygon([(x1,y1), (x1,y2), (x2,y2), (x2,y1)])
        if not green_map.contains(box):
            continue

        dx, dy = max(x1, x2) - min(x1, x2), max(y1, y2) - min(y1, y2)
        area = (dx+1) * (dy+1)
        maximum = max(maximum, area)
    print(i)



print(maximum)