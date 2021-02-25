import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

N, Q = inpl()
n = inpl()
q = inpl()

d = list()
for i in range(N):
    sum += (n[i % N] * n[(i + 1) % N] * n[(i + 2) % N] * n[(i + 3) % N])
    # print(n[i % N], n[(i + 1) % N], n[(i + 2) % N], n[(i + 3) % N])
    d.append(sum)

# for q in range(Q):
#     n[[q]-1] = n[Q[q]-1] * -1
#     sum = 0
#     for i in range(N):
#         sum += (n[i%N] * n[(i+1)%N] * n[(i+2)%N] * n[(i+3)%N])
#         print(n[i%N] ,n[(i+1)%N],n[(i+2)%N],n[(i+3)%N])
#     print(sum)
#     print('---')