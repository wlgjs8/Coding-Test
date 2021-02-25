def solution(conference):
    answer = 1
    arranged_conference = conference[0]

    # for i, conf in enumerate(conference):
    #     if i == 0:
    #         continue
    #
    #     if arranged_conference[1] <= conf[0]:
    #         arranged_conference[1] = conf[1]
    #         answer += 1

    for i in range(1, len(conference)):
        if arranged_conference[1] <= conference[i][0]:
            arranged_conference[1] = conference[i][1]
            answer += 1

    return answer

size = int(input())

conference = list()
for _ in range(size):
    data = list(map(int, input().split()))
    conference.append(data)

conference.sort(key=lambda x : [x[1], x[0]])

print(solution(conference))