import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def mul(s,e):
    ans = trees[s]
    for i in range(s+1,e):
        ans *= trees[i]
    return ans

n = inp()
trees = inpl()

max = 0
for a in range(1,n):
    for b in range(a+1,n):
        for c in range(b+1,n):
            temp = mul(0,a) + mul(a,b) + mul(b,c) + mul(c,n)
            if temp > max:
                # print(temp, mul(0, a), mul(a, b), mul(b, c), mul(c, n),a,b,c)
                # print(temp, a,b,c)

                max = temp
print(max)
