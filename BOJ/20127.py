import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def check(A: list, B: list):
    A.extend(B)
    if A == incA or A == decA:
        return True
    else:
        return False
n = inp()
a = inpl()

ans = 1000001
incA, decA = sorted(a), sorted(a, reverse=True)
minA, maxA = min(a), max(a)
minA_index, maxA_index = a.index(minA), a.index(maxA)

if check(a[minA_index:],a[:minA_index]):
    ans = minA_index
if check(a[maxA_index:],a[:maxA_index]):
    if ans > maxA_index:
        ans = maxA_index
if ans == 1000001:
    ans = -1
print(ans)