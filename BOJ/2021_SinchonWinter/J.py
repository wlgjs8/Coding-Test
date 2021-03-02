import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

N, K = inpl()
a = inpl()

hasN = [0] * (N + 1)
hasN[0] = 1

for aa in a:
    hasN[aa] = 1

cnt = 0
if hasN[1] == 1:
    index1 = a.index(1)
else:
    a.append(1)
    index1 = a.index(1)

size = N
if 0 in hasN:
    check = True
    hasN_index = hasN.index(0)
else:
    check = False
    print(0)

while check:
    a = a[:index1] + a[index1:]
    print(a)
    for i in range(0, index1):
        if 1 > a[i] or a[i] > index1 + 1:
            while hasN[hasN_index] == 1:
                print('hasNNN')
                hasN_index += 1
            a.append(hasN_index)
            hasN_index += 1
            break
        else:
            check = False
            print(cnt)
            break
    index1 += 1
    cnt += 1
    size += 1