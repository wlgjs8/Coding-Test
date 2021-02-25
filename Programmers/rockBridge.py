from itertools import combinations

def solution(distance, rocks, n):
    remain_rocks = list(combinations(rocks, len(rocks) - n))

    max_distance = 0
    for remain_rock in remain_rocks:
        distance_list = []

        for rock in range(len(remain_rock) + 1):
            if rock == 0:
                distance_list.append(remain_rock[rock])
            elif rock == len(remain_rock):
                distance_list.append(abs(distance - remain_rock[rock-1]))
            else:
                distance_list.append(abs(remain_rock[rock] - remain_rock[rock-1]))

        min_distance = distance
        for distance_stuff in distance_list:
            if min_distance > distance_stuff:
                min_distance = distance_stuff

        if max_distance < min_distance:
            max_distance = min_distance
    answer = max_distance
    return answer

print(solution(25, 	[2, 14, 11, 21, 17], 2))