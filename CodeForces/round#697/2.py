import sys
def inp(): return int(sys.stdin.readline())

t = inp()
for _ in range(t):
    sum = inp()

    if sum < 2020 or sum > 1000000:
        print('NO')
    else:
        cnt = 0
        check = False
        while sum >= 2020:
            sum = sum - 2020
            if (sum % 2020) == cnt or (sum % 2020) == cnt + 1:
                print('YES')
                check = True
                break
            cnt += 1
        if not check:
            print('NO')