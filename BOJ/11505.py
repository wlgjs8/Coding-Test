import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n, m, k = inpl()
A = [0]
M = [1]
mul = 1
for _ in range(n):
    temp = inp()
    A.append(temp)
    mul *= temp
    M.append(mul)

for _ in range(m+k):
    a, b, c = inpl()
    if a == 1:
        if A[b] == 0:
            A[b] = c
            mul = M[b-1]
            for i in range(b, n+1):
                mul *= A[i]
                M[i] = mul
        else:
            for i in range(b, n+1):
                M[i] = int(M[i]/A[b]) * c
        A[b] = c
    else:
        print(int(M[c] / M[b-1]) % 1000000007)