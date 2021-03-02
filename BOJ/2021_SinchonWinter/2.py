import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

N = inp()
a = inpl()

a.sort()
MAX = 1
cnt = 1
for i in range(len(a) - 1):
    if a[i] != a[i + 1]:
        cnt = 1
    else:
        cnt += 1
        if MAX < cnt:
            MAX = cnt

print(MAX)