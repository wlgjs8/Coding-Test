for _ in range(int(input())):
    n = int(input()) - 1
    if n%2:
        s = [1]*(n//2) +[0] + [-1]*(n//2)
    else:
        s = [1]*(n//2) + [-1]*(n//2)
    for i in range(n):
        for j in s:
            print(j, end = " ")
        s = s[:-1]
    print()

# for _ in range(int(input())):
# 	n = int(input())
# 	if n%2==1:
# 		arr = [0]*((n*(n-1))//2)
# 		arr[0] = 1
# 		for i in range(1,len(arr)):
# 			if arr[i-1]==1:
# 				arr[i] = -1
# 			else:
# 				arr[i] = 1
# 		print(*arr)
# 	else:
# 		a = [1]*((n-1)//2) + [0]*(1) + [-1]*(n-1 - (n-1)//2 - 1)
# 		arr = a[:]
# 		for i in range(n-1):
# 			a.pop()
# 			arr += a
# 		print(*arr)