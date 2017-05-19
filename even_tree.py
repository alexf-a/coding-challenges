#Even Tree Problem from HackerRank: https://www.hackerrank.com/challenges/even-tree

import fileinput
import copy

def max_edges(N, edges):
    if N == 0:
        return 0
    q = [1]
    cpy = copy.deepcopy(edges)
    while q:
        v = q.pop(0)
        children = []
        for e in edges:
            if e[1] == v:
                q.append(e[0])
                children.append(e[0])
        for child in children:
            if test_even(child, cpy):
                cpy.remove([child, v])
    return len(edges) - len(cpy)
        
    
        
def test_even(root, edges):
    q = [root]
    count = 1
    while q:
        curr = q.pop(0)
        for edge in edges:
            if edge[1] == curr:
                count += 1
                q.append(edge[0])
    if count%2 == 0:
        return True
    return False
        
    
    
edges = []
counter = 0
M, N = 0, 0
for line in fileinput.input():
    if counter > 0:
        edge = line.split(' ')
        edge = [int(str(v)) for v in edge]
        edges.append(edge)
        counter += 1
    else:
        l = line.split(' ')
        l = [int(str(val)) for val in l]
        N = l[0]
        M = l[1]
    counter = counter + 1
print(max_edges(N, edges))