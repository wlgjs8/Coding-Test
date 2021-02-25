def solution(n, lost, reserve):
    reserve_del = set(reserve) - set(lost)
    lost_del = set(lost) - set(reserve)

    for good in reserve_del:
        if good -1 in lost_del:
            lost_del.remove(good-1)
        elif good + 1 in lost_del:
            lost_del.remove(good + 1)
    answer = n - len(lost_del)
    return answer

# print(solution(5, [2,4], [1, 3, 5]))
print(solution(5, [2,4], [3]))