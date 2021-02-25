import math
import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
# N = 270288240945436569515614693625975275496152008446548287007392875106625428705522193898612483924502370165362606085021546104802209750050679917549894219699518475423665484263751733356162464079737887344364574161119497604571044985756287880514600994219426752366915856603136862602484428109296905863799821216320
# C = 270288240945436551019305908463402626133344424635003137400602091930237777421360473851797325724922730460543802875678603168471867361078540080081808473288115110060581000433119131429793939577717447508918397345219433071259594386723113371250852722071254367796680880783950950640887679135140232038177361100800

def com(n, k):
    k = min(n - k, k)
    f = math.factorial
    return (f(n) // ( f(k) * f(n - k)) ) % 1000000007

t = inp()
# t = 1
for _ in range(t):
    # n, k = 1000, 500
    # blogs = [1 for _ in range(1000)]

    n, k = inpl()
    blogs = inpl()
    blogs.sort(reverse=True)

    answer = 0
    k -= 1

    if n - 1 == k:
        answer = 1

    else:
        if k > 0 and blogs[k] == blogs[k-1]:
            for blog in blogs:
                if blog == blogs[k]: answer += 1
            answer = (com(answer, (k+1)-blogs.index(blogs[k])))

        elif blogs[k] == blogs[k+1]:
            for i in range(k, len(blogs)):
                if blogs[k] == blogs[i]: answer += 1
            answer = (com(answer, (k+1)-blogs.index(blogs[k])))
        else:
            answer = 1

    print('answer : ', answer)
# print(com(10, 5))