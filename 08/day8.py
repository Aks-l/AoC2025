import numpy as np
from functools import reduce
boxes = np.array(list(map(lambda x: x.strip().split(","), [*open("day8.txt")])), dtype= float)
clusters: list[set] = [{i} for i in range(len(boxes))]

diff = boxes[:, None, :] - boxes[None, :, :]
dist_matrix = np.linalg.norm(diff, axis=-1)
dist_matrix[np.tril_indices_from(dist_matrix)] = np.inf

def find_and_remove():
    global dist_matrix, clusters
    i,j = np.unravel_index(np.argmin(dist_matrix), dist_matrix.shape)
    dist_matrix[i,j] = np.inf

    newly_merged = boxes[[i,j]]
    # Print running answer to part 2
    print(newly_merged[0][0] * newly_merged[1][0])

    for cluster in clusters:
        if i in cluster or j in cluster:
            cluster.add(i)
            cluster.add(j)
            merge_overlap(clusters)
            return
    clusters.append(set([i,j]))
    merge_overlap(clusters)
    

def merge_overlap(clusters: list[set]):
    merged = True
    while merged:
        merged = False
        new_clusters = []
        while clusters:
            current = clusters.pop()
            for other in clusters:
                if not current.isdisjoint(other):
                    current.update(other)
                    clusters.remove(other)
                    merged = True
            new_clusters.append(current)
        clusters.extend(new_clusters)

# Part 1 does this 1000 times instead of while 
while len(clusters[0]) != len(boxes):
    find_and_remove()

merge_overlap(clusters)

print(reduce(lambda a,b: a*b, sorted([len(c) for c in clusters], reverse=True)[:3]))



