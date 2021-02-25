import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

t = inp()
for _ in range(t):
    n = inp()
    arr = inpl()

    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        arr[i] = arr[i] % 3
        if arr[i] == 0:
            cnt0 += 1
        elif arr[i] == 1:
            cnt1 += 1
        else:
            cnt2 += 1

    n = int(n/3)
    answer = 0

    if cnt0 > n:
        answer += cnt0 - n
        cnt1 += cnt0 - n
        cnt0 = n
    if cnt1 > n:
        answer += cnt1 - n
        cnt2 += cnt1 - n
        cnt1 = n
    if cnt2 > n:
        answer += cnt2 - n
        cnt0 += cnt2 - n
        cnt2 = n
    if cnt0 > n:
        answer += cnt0 - n
        cnt1 += cnt0 - n
        cnt0 = n
    if cnt1 > n:
        answer += cnt1 - n
        cnt2 += cnt1 - n
        cnt1 = n
    if cnt2 > n:
        answer += cnt2 - n
        cnt0 += cnt2 - n
        cnt2 = n

    print(answer)