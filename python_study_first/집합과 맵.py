"""
#10815
N = int(input())
list1 = list(map(int, input().split()))
M = int(input())
list2 = list(map(int, input().split()))

d = {}
for i in range(N):
    d[list1[i]] = 1

for i in range(M):
    if list2[i] in d:
        list2[i] = 1
    else:
        list2[i] = 0

print(*list2)


#딕셔너리의 value가 중요하지 않으므로 key를 이용하여 간결하게
N = int(input())
cards = set(map(int, input().split()))

M = int(input())
queries = map(int, input().split())

print(*[1 if x in cards else 0 for x in queries])
"""


"""
#14425
N, M = map(int, input().split())
list_S = [ input() for _ in range(N) ]
list_C = [ input() for _ in range(M) ]

set_S = set(list_S)
count = 0
for x in list_C:
    if x in set_S:
        count += 1
print(count)
"""


"""
#7785
N = int(input())
d = {}
for i in range(N):
    a, b = input().split()
    d[a] = b

#for문 in 뒤에 디렉터리는 기본적으로 key가 들어옴
#특정하기위해선 d.keys(), d.values(), d.items() (둘다)
for key in sorted(d.keys(), reverse=True):
    if d[key] == "enter":
        print(key)
"""


"""
#1620
N, M = map(int, input().split())
d1 = {}
d2 = {}
for i in range(N):
    name = input()
    d1[i+1] = name
    d2[name] = i+1

#reverse_d = {v: k for k, v in d1.items()}
#딕셔너리 뒤집기 1:1관계일때만 가능

matter = []
for i in range(M):
    matter.append(input())

result = []
for x in matter:
    if x.isdigit(): #숫자로 이루어진 문자열
        result.append(d1[int(x)])
    else: #문자열로 이루어짐
        result.append(d2[x])

for y in result:
    print(y)
"""


"""
#10816
N = int(input())
d = {}
list1 = list(map(int, input().split()))
for i in list1:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

M = int(input())
list2 = list(map(int, input().split()))
result = []
for x in list2:
    if x in d:
        result.append(d[x])
    else:
        result.append(0)
print(*result)

#딕셔너리 개수카운팅 dict.get(key,default) 이용
#key가 있으면 -> value / 없으면 default 반환
#d = {}
#for x in numbers:
#    d[x] = d.get(x, 0) + 1
#value 값을 개수로 지정했을때 key가 있으면 가져와 그 값에서 +1
#없으면 0에서 +1 
"""