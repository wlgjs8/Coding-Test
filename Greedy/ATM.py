def solution(peopleLine):
    answer = 0
    peopleLine.sort(reverse=True)

    for i in range(1, len(peopleLine) + 1):
        answer += i * peopleLine[i-1]

    return answer

n = int(input())
lists = input().split()
peopleLine = list()

for i in range(n):
    peopleLine.append(int(lists[i]))

# peopleLine = [3, 1, 4, 3, 2]
print(solution(peopleLine))