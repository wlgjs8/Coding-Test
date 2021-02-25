import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def build(start, end, curD):
    if end < -1 or start - end > 0:
        return
    if start == end:
        per_depth[start] = curD
        return
    m = start
    for i in range(start, end+1):
        if per_a[m] < per_a[i]:
            m = i
    per_depth[m] = curD

    build(start, m-1, curD+1)
    build(m+1, end, curD+1)

t = inp()
for _ in range(t):
    n = inp()
    per_a = inpl()
    per_depth = [0 for _ in range(n)]

    build(0, n-1, 0)
    print(' '.join(repr(e) for e in per_depth))
