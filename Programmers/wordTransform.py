from collections import deque

def OK(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    return False if cnt > 1 else True

def solution(begin, target, words):
    answer = 0
    # que => word, cnt

    que = deque()
    que.append([begin, 0])
    while que:
        word, cnt = que.popleft()
        if cnt > len(words):
            break

        print(word, cnt)
        if word == target:
            answer = cnt
            break

        for w in words:
            if OK(word, w):
                que.append([w, cnt+1])
    return answer

print(solution('hit', 'cog', ['hot', 'dot', 'dog','lot','log','cog']))
# print(solution('hit', 'cog', ['hot', 'dot', 'dog','lot','log']))
