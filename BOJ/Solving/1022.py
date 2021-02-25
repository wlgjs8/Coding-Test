import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

r1, c1, r2, c2 = inpl()
rotate = []

x = max(abs(r1), abs(r2))
y = max(abs(c1), abs(c2))

cnt = 0
for i in range(x + 1):
    for j in range(y + 1):

