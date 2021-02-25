def solution(citations):
    citations.sort()

    num = len(citations)
    while True:
        for i, value in enumerate(citations):
            if value >= num and len(citations[i:]) >= num:
                return num
        else:
            num -= 1
            continue
        break

# print(solution([3, 0, 6, 1, 5]))
# print(solution([1,4,4,5,6]))
print(solution([1]))