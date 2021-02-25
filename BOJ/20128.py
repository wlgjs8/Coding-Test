import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def make_set(n):
    for i in range(1, n+1):
        parent.append(i)
        rank.append(0)

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(n1, n2):
    root1 = find(n1)
    root2 = find(n2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2

            if rank[root1] == rank[root2]:
                rank[root2] += 1

parent = [0]
rank = [0]
n, m = inpl()
edges = []
for _ in range(m):
    edges.append(inpl())
edges.sort(key=lambda x:x[2])
make_set(n)

mst = []
for e in edges:
    if find(e[0]) != find(e[1]):
        union(e[0], e[1])
        mst.append(e[2])
# print(parent)
# print(rank)
print(mst)