
def solution(distance, rocks, n):
    answer = 0
    left = 1
    right = distance
    rocks.sort()
    print('rocks : ', rocks)
    while left <= right:
        mid = (left + right) // 2
        pre_rock = 0
        num_of_rock = 0
        m_min = 1000000001
        for rock in rocks:
            if rock - pre_rock < mid:
                num_of_rock += 1
                print(rock, pre_rock, mid)
            else:
                m_min = min(m_min, rock - pre_rock)
                pre_rock = rock
                print('m_min, pre_rock : ', m_min, pre_rock)

        print('------------')
        print()
        if num_of_rock > n:
            right = mid - 1
        else:
            answer = m_min
            left = mid + 1
    return answer

print(solution(25, 	[2, 14, 11, 21, 17], 2))