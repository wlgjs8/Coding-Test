def solution(name):
    answer = 0

    make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    charMove = 0
    cursorMove = 0
    idx, answer = 0, 0

    while True:
        charMove += make_name[idx]
        make_name[idx] = 0

        if sum(make_name) == 0:
            break
        right, left = 1, 1

        while make_name[idx + right] == 0:
            right += 1
        while make_name[idx - left] == 0:
            left += 1

        if left < right:
            cursorMove += left
            idx -= left
        else:
            cursorMove += right
            idx += right


    # print(charMove, cursorMove)
    answer = charMove + cursorMove
    return answer

# print(solution('JEROEN'))
# print(solution('AABCAAAAA'))
print(solution('BACAD'))
# print(solution('BCADE'))
# print(solution('BCBAAADE'))
# 11 /6
# print(solution('AAABAAAAAAAAAAAAAAAAABAA'))
# 2 / 9
# print(solution('BAAAAAAAAAAAAAAAAABAA'))
# B D C
