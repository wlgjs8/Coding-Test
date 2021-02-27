import sys
from collections import deque

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

t = inp()
for _ in range(t):
    N, K = inpl()
    building = [0] + inpl()
    inDegree = [0 for _ in range(N + 1)]
    DP = [0 for _ in range(N + 1)]

    tree = [[] for _ in range(N+1)]
    for _ in range(K):
        a, b = inpl()
        tree[a].append(b)
        inDegree[b] += 1

    q = deque()
    for i in range(1, N+1):
        if inDegree[i] == 0:
            q.append(i)
            DP[i] = building[i]

    while q:
        a = q.popleft()
        for i in tree[a]:
            DP[i] = max(building[i] + DP[a], DP[i])
            inDegree[i] -= 1
            if inDegree[i] == 0:
                q.append(i)

    print(tree)
    # print(DP)
    print(inDegree)

    ans = inp()
    print(DP[ans])