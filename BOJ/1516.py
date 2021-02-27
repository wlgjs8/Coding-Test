import sys
from heapq import heappop, heappush

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

N = inp()
building = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]
DP = [0 for _ in range(N+1)]

for i in range(N):
    temp = inpl()
    building[i+1] = temp[0]
    j = 1
    while temp[j] != -1:
        inDegree[i+1] += 1
        graph[temp[j]].append(i+1)
        j += 1

q = []
for i in range(1, N+1):
    if inDegree[i] == 0:
        heappush(q, i)
        DP[i] = building[i]

while q:
    a = heappop(q)
    for i in graph[a]:
        inDegree[i] -= 1
        DP[i] = max(DP[i], DP[a] + building[i])
        if inDegree[i] == 0:
            heappush(q, i)

# print(building)
# print(graph)
# print(inDegree)

for dd in range(1, N+1):
    print(DP[dd])