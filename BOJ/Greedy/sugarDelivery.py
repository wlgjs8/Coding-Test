def solution(n):
    five_kilos = n // 5

    # three_kilo = 0
    # five_kilo = 0

    for five_kilo in range(five_kilos, -1, -1):
        three_kilo = 0

        while True:
            if (5*five_kilo + 3*three_kilo) >= n:
                break
            three_kilo += 1

        if 5*five_kilo + 3*three_kilo == n:
            answer = three_kilo + five_kilo
            break
        if five_kilo == 0 and (5*five_kilo + 3*three_kilo) != n:
            answer = -1

    return answer

n = int(input())
print(solution(n))