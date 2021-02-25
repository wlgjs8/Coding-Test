import sys

def solution(appliant):
    answer = 0
    congrats = list()
    appliant.sort(key=lambda x : x[0])
    y_top = len(appliant)

    for app in appliant:
        if app[1] < y_top:
            congrats.append(app)
            y_top = app[1]
            answer += 1

    return answer

# N = int(sys.stdin.readline())
# appliant = list()

# for i in range(N):
#     N2 = int(sys.stdin.readline())
#     temp = list()
#     for j in range(N2):
#         temp.append(list(map(int, sys.stdin.readline().split())))
#     print(solution(temp))

# for i in range(N):
#     print(solution(appliant[i]))
# appliant = [[3,6],[7,3],[4,2],[1,4],[5,7],[2,5],[6,1]]

appliant =[[3,2],[1,4],[4,1],[2,3],[5,5]]
print(solution(appliant))