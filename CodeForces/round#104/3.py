import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    pos_score = (n-1) / 2 * 3

    if pos_score - int(pos_score) != 0.0:
    #     짝수개의 팀
        for k in range(1, n+1):
            print('hi')

    else:
        for k in range(n-1, 0, -1):
            for i in range(k):
                if i % 2 == 0:
                    print(1, end=' ')
                else:
                    print(-1, end=' ')