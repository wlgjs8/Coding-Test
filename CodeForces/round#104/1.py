import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = sys.stdin.readline()
    heros = list(map(int, sys.stdin.readline().split()))

    heros.sort()
    if heros[0] == heros[len(heros)-1]:
        print(0)
    else:
        cnt = 0
        for hero in heros:
            if hero == heros[0]:
                cnt += 1
        print(len(heros) - cnt)
