def solution(N, stages):
    answer = []

    stage_cur = [[0, 0] for i in range(N)]

    totalPeople = len(stages)
    for stage in range(0, N):
        stage_cur[stage][0] = stages.count(stage+1)
        stage_cur[stage][1] = totalPeople
        totalPeople -= stage_cur[stage][0]

    stage_failure = [[i+1, 0] for i in range(len(stage_cur))]
    cnt = 0
    for cur in stage_cur:
        if cur[1] == 0:
            stage_failure[cnt][1] = 0
        else:
            stage_failure[cnt][1] = cur[0]/cur[1]
        cnt += 1

    stage_failure.sort(key=lambda x:x[1], reverse=True)

    for stage in stage_failure:
        answer.append(stage[0])

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4, [4,4,4,4,4]))