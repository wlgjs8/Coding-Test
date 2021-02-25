N = int(input())

answer = 0
change = [500, 100, 50, 10, 5, 1]

N = 1000 - N

for coin in change:
    answer += N // coin
    N %= coin

print(answer)