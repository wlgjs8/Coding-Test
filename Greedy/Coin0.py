def solution(coins, k):
    answer = 0
    coins.sort(reverse=True)

    for coin in coins:
        answer += k // coin
        k %= coin

    return answer

n, k = map(int, input().split())
coins = list()
for _ in range(n):
    coins.append(int(input()))

# k = 4790
# coins = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
print(solution(coins, k))