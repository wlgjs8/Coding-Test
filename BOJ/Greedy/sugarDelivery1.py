def solution(n):
    answer = 0

    while True:
        if n % 5 == 0:
            answer += int(n / 5)
            break
        elif n < 3:
            return -1
        else:
            n -= 3
            answer += 1

    return answer

n = int(input())
print(solution(n))