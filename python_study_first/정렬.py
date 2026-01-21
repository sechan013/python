"""
#2750
N = int(input())
list1 = [ int(input()) for _ in range(N)]
list1.sort()
for i in list1:
    print(i)
"""


"""
#2587
list1 = [ int(input()) for _ in range(5) ]
average = int(sum(list1) / len(list1))
list1.sort()
median = list1[2]
print(average)
print(median)
"""


"""
#25305
N, k = map(int, input().split())
list1 = list(map(int, input().split()))
#list1 = [ int(input()) for _ in range(N) ]
list1.sort(reverse = True) #역순으로 정렬
print(list1[k-1])
"""


"""
#2751
import sys #입출력 빠르게 대용량 문제
N = int(sys.stdin.readline())
list1 = [ int(sys.stdin.readline()) for _ in range(N) ]
list1.sort()
result = []
for x in list1:
    result.append(str(x))

sys.stdout.write('\n'.join(result))
"""


"""
#1427
N = int(input())
list1 = []
for i in str(N):
    list1.append(i)

list1.sort(reverse = True)
print(''.join(list1))
"""


"""
#11650
N = int(input())
list1 = [ list( map(int, input().split())) for _ in range(N) ]
list1.sort(key = lambda x: (x[0], x[1])) #lamda -> 함수라고보면됨
#가장처음 x좌표 비교(x[0]) -> 같으면 y좌표(x[1])
for x in list1:
    print(*x)
"""


"""
#11651
N = int(input())
list1 = [ list(map(int, input().split())) for _ in range(N) ]
list1.sort(key = lambda x: (x[1], x[0]))
for x in list1:
    print(*x)
"""



"""
#1181
N = int(input())
list1 = [ input() for _ in range(N) ]
list1 = list(set(list1)) #set은 sort 불가 -> 다시 list로
list1.sort(key = lambda x: (len(x), x))
for x in list1:
    print(x)
"""


"""
#10814
N = int(input())
list1 = [ input().split() for _ in range(N) ]
list1.sort(key = lambda x: int(x[0]))
for x in list1:
    print(*x)
"""


"""
#18870
N = int(input())
list1 = [ int(x) for x in input().split() ]

list2 = sorted( list( set(list1) ) ) #복사본 (정렬) #set으로 중복 제거
d = {}
for i in range(len(list2)):
    if list2[i] not in d: #중복된 수 들어가는 것 방지
        d[list2[i]] = i #정렬된 순서대로 작은 것 부터 죄표압축

for i in range(N):
    list1[i] = d[list1[i]] #압축된 수 꺼내 갱신

print(*list1)
"""