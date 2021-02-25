import sys
import heapq

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

V, E = inpl()
K = inp()
INF = V*10 + 1
distance = [[] for _ in range(V+1)]
visited = [False] * (V+1)

for _ in range(E):
    s, e, d = map(int, sys.stdin.readline().split())
    distance[s].append([e, d])

q = []
K_distance = [INF] * (V + 1)
K_distance[K] = 0
heapq.heappush(q, [0, K])

while q:
    dis, cur = heapq.heappop(q)
    visited[cur] = True
    for end in distance[cur]:
        if visited[end[0]]:
            continue
        if K_distance[end[0]] > dis + end[1]:
            K_distance[end[0]] = dis + end[1]
            heapq.heappush(q, [K_distance[end[0]], end[0]])

for i in range(1, V+1):
    print('INF') if K_distance[i] == INF else print(K_distance[i])