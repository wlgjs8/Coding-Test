import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

x = inp()
if x % 100 == 0:
    print(100)
else:
    print(100 -x%100)