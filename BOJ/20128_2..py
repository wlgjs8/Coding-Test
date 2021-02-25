import sys
import heapq

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

# N개의 노드, M개의 간선
n, m = inpl()
INF = int(10e14 + 1)
edges = [[] for _ in range(n+1)]
# 1번은 짝수, 0번은 홀수
dist = [[INF] * 2 for _ in range(n+1)]
dist[1][1] = 0

for _ in range(m):
    u, v, w = inpl()
    edges[u].append([v, w])
    edges[v].append([u, w])

q = []
heapq.heappush(q, [0, 1])
while q:
    distance, current = heapq.heappop(q)
    if distance != dist[current][1] and distance != dist[current][0]:
        continue
    for end, weight in edges[current]:
        end_distance = distance + weight
        if end_distance < dist[end][0] and end_distance % 2 == 1:
            dist[end][0] = end_distance
            heapq.heappush(q, [end_distance, end])
        elif end_distance < dist[end][1] and end_distance % 2 == 0:
            dist[end][1] = end_distance
            heapq.heappush(q, [end_distance, end])

for i in range(1, n+1):
    print(dist[i][0], end=' ') if dist[i][0] != INF else print(-1, end=' ')
    print(dist[i][1]) if dist[i][1] != INF else print(-1)
