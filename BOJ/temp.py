import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def a_sort(node):
    return -node[1], node[0].lower()

n = inp()
a = []
for _ in range(n):
    na, sco = list(sys.stdin.readline().split())
    a.append([na, int(sco)])

a.sort(key=a_sort)
print(a[0][0])
