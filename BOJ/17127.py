import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
trees = inpl()

max = max(trees)
mul = 1
re = list()
maxi = trees.index(max)
if maxi == 0:
    for i in range(n-3):
        mul *= trees[i]
    re.extend([n-3,n-2,n-1])
elif maxi == n-1:
    for i in range(3):
        mul *= trees[i]
    re.extend([0,1,2])
else:
    if trees[1] > trees[n-2]:
        for i in range(1,n-2):
            mul *= trees[i]
        re.extend([0,n-2,n-1])
    else:
        for i in range(2,n-1):
            mul *= trees[i]
        re.extend([0,1,n-1])

for r in re:
    mul += trees[r]
print(mul)