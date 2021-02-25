import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n, m = inpl()
score = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = inpl()
    score[a-1][b-1] = 1

for i in range(m):
    print(*score[i])