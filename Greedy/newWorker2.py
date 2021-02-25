import sys

N = int(sys.stdin.readline())
appliant = list()

for i in range(N):
    n = int(sys.stdin.readline())
    appliant = list()
    y_top, answer = n+1, 0

    for j in range(n):
        appliant.append(list(map(int, sys.stdin.readline().split())))
    appliant.sort(key=lambda x : x[0])

    for app in appliant:
        if y_top > app[1]:
            y_top = app[1]
            answer += 1
    print(answer)


# for i in range(N):
#     print(solution(appliant[i]))
# appliant = [[3,6],[7,3],[4,2],[1,4],[5,7],[2,5],[6,1]]
# print(solution(appliant))