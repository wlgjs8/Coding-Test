import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n, k = inpl()

for _ in range(k):
    n = str(n)
    num = list()

    for i in range(len(n)):
        num.append(int(n[i]))

    ascend_num_arr = sorted(num, reverse=False)
    descend_num_arr = sorted(num, reverse=True)

    ascend_num, descend_num = '', ''
    for i in range(len(n)):
        ascend_num += str(ascend_num_arr[i])
        descend_num += str(descend_num_arr[i])

    n = int(descend_num) - int(ascend_num)

print(n)
