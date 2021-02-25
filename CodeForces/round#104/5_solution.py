import sys

mod = 10 ** 9 + 7
INF = float('inf')


def inp(): return int(sys.stdin.readline())


def inpl(): return list(map(int, sys.stdin.readline().split()))


def inpl_1(): return list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))


def inps(): return sys.stdin.readline()


def inpsl(x): tmp = sys.stdin.readline(); return tmp[:x]


def err(x): print(x); exit()


n0, n1, n2, n3 = inpl()
A = inpl()
B = inpl()
C = inpl()
D = inpl()

m1 = inp()
xy1 = [inpl_1() for _ in range(m1)]
m2 = inp()
xy2 = [inpl_1() for _ in range(m2)]
m2 = inp()
xy3 = [inpl_1() for _ in range(m2)]
dis = [[] for _ in range(n1)]
for x, y in xy1: dis[y].append(A[x])
A.sort()
BB = [INF] * n1
for i, nums in enumerate(dis):
    nums.sort()
    ind = 0
    for x in nums:
        if A[ind] != x:
            break
        ind += 1
    if ind < n0:
        BB[i] = A[ind] + B[i]
# print(BB)

dis = [[] for _ in range(n2)]
for x, y in xy2: dis[y].append(BB[x])
BB.sort()
CC = [INF] * n2
for i, nums in enumerate(dis):
    nums.sort()
    ind = 0
    for x in nums:
        if BB[ind] != x:
            break
        ind += 1
    if ind < n1 and BB[ind] != INF:
        CC[i] = BB[ind] + C[i]
# print(CC)
dis = [[] for _ in range(n3)]
for x, y in xy3: dis[y].append(CC[x])
CC.sort()
DD = [INF] * n3
res = INF
for i, nums in enumerate(dis):
    nums.sort()
    ind = 0
    for x in nums:
        if CC[ind] != x:
            break
        ind += 1
    if ind < n2 and CC[ind] != INF:
        if res > CC[ind] + D[i]:
            res = CC[ind] + D[i]
if res == INF: res = -1
print(res)