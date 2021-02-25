import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
m = inp()
INF = int(1e9)
bus_arr = [[INF for _ in range(n+1)] for _ in range(n+1)]
edges = list()

for _ in range(m):
    edges.append(inpl())

edges.sort(key=lambda x : x[2])

for edge in edges:
    node = bus_arr[edge[0]][edge[1]]
    if node > edge[2]:
        bus_arr[edge[0]][edge[1]] = edge[2]

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            bus_arr[a][b] = min(bus_arr[a][b], bus_arr[a][k] + bus_arr[k][b])

for i in range(1, n+1):
    bus_arr[i][i] = 0
    for j in range(1, n+1):
        if bus_arr[i][j] == INF:
            bus_arr[i][j] = 0
        print(bus_arr[i][j], end =' ')
    print()