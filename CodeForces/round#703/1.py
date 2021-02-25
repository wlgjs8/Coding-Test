import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

t = inp()
for _ in range(t):
    n = inp()
    stacks = inpl()

    for i in range(n-1):
        if stacks[i] >= stacks[i+1]:
            if i > 0:
                sum = stacks[i]
                stacks[i] = stacks[i-1] + 1
                stacks[i+1] += sum - stacks[i]
            else:
                sum = stacks[i]
                stacks[i+1] += sum
                stacks[i] = 0
        print(stacks)
        for j in range(n - i - 1):
            if stacks[j] > stacks[j+1]:
                stacks[j], stacks[j+1] = stacks[j+1], stacks[j]

    print(stacks)
    if stacks == sorted(stacks) and len(stacks) == len(set(stacks)):
        print('YES')
    else:
        print('NO')