import sys

waterMelon = int(sys.stdin.readline())

if waterMelon % 2 == 0 and waterMelon > 2:
    print('YES')
else:
    print('NO')