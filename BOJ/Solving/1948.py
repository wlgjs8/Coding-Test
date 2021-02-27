import sys
from heapq import heappop, heappush

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

N = inp()
M = inp()

graph = [[] for _ in range(N+1)]
rego = [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]
DP = [0 for _ in range(N+1)]
path_DP = [[] for _ in range(N+1)]

for _ in range(1, M+1):
    start, end, cost = inpl()
    graph[start].append((end, cost))
    rego[end].append((start, cost))
    inDegree[end] += 1

startCity, endCity = inpl()

q = []
heappush(q, startCity)

while q:
    cur = heappop(q)
    for end_cost in graph[cur]:
        end, cost = end_cost
        inDegree[end] -= 1
        # temp = DP[end]
        DP[end] = max(DP[end], DP[cur] + cost)
        # if DP[end] != temp:
        #     path_DP[end] = []
        #     path_DP[end].append(cur)
        # if temp == DP[end] and DP[cur] + cost == DP[end]:
        #     path_DP[end].append(cur)
        if inDegree[end] == 0:
            heappush(q, end)

print(DP[endCity] - DP[startCity])
q = [endCity]
visited = [0] * N
roadAnswer = 0
while len(q):
    now = q.pop()
    for i in range(len(rego[now])):
        next, cost = rego[now][i]
        if DP[now] - DP[next] == cost:
            roadAnswer += 1
            if visited[next] == 0:
                q.append(next)
                visited[next] = 1
print(roadAnswer)