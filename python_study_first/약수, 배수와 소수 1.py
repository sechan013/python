
"""
#5086
A, B = -1, -1
list1 = []
while A != 0 and B != 0:
    A, B = map(int, input().split())

    if A == 0 or B == 0:
        break

    if B % A == 0:
        list1.append('factor')

    if A % B == 0:
        list1.append('multiple')

    if A % B != 0 and B % A != 0:
        list1.append('neither')

for i in list1:
    print(i)
"""


"""
#2051
N, K = map(int, input().split())
i = 1
list1 = []
while i <= N:
    if N % i == 0:
        list1.append(i)

    i = i + 1

if len(list1) < K:
    print(0)
else:
    print(list1[K-1])
"""


"""
#9506
S = 0
i = 1
result_list = [] #출력문을 저장 할 리스트
while S != -1:

    list1 = [] #약수를 저장 할 리스트

    S = int(input())
    if S == -1: #-1을 입력하면 종료
        break

    i = 1
    while i < S:
        if S % i == 0:
            list1.append(i)
        i = i + 1

    add = 0
    procedure = (str(S) + " = ")
    for j in list1:
        add = add + j #-> add = sum(list1) 간단하게
    if add == S:    #완전수인지 확인 (자신을 제외한 모든 약수들의 함과 같음)
        list1 = list(map(str, list1)) #join은 문자열만
        # +) map은 이터레이터 -> 한번만 사용가능 (list로 또 묶어주면 좋음)
        procedure += ' + '.join(list1) #join을 사용하여 풀이

        result_list.append(procedure)
        #하나의 리스트, 문자열을 while문을 돌면 초기화 해줌으로써
        #잠시 문자열을 담아두는 그릇으로 활용
        #문자열은 통째로 출력리스트에 저장

        
        #내가 처음 했던 방식
        procedure = (str(S) + " = ") 
        for j in list1:
            add = add + j
        if add == S: #문자열을 이어주면서 풀이
            for k in range(len(list1)-1):
                procedure += (str(list1[k]) + ' + ')
            procedure += (str(list1[-1]))
            result_list.append(procedure)
        
        
    else:
        result_list.append(str(S) + " is Not perfect.")

for m in result_list: #출력리스트에서 문자열 꺼내오기
    print(m)
"""


"""
#1978
N = int(input())
list1 = [int(x) for x in input().split()]

result_list = []

for ch in list1:

    a = 0

    if ch == 1:
        continue

    m = 2
    while m < ch:
        if ch % m == 0:
            a = a + 1
            break
        m = m + 1

    if a == 0:
        result_list.append(ch)

print(len(result_list))
"""

"""
#1978 (간결한 버전)
N = int(input())
list1 = [int(x) for x in input().split()]

count = 0

for n in list1:
    if n < 2:       #1은 소수가 아니기에 예외
        continue
    
    for i in range(2, n):
        if n % 1 == 0:
            break
    else:           #break 없이 끝났을 때만 실행
        count += 1
        
print(count)
"""


"""
#2581
M = int(input())
N = int(input())
is_prime = []
for i in range(M,N+1):

    if i < 2:
        continue

    j = 2
    while j < i:
        if i % j == 0:
            break
        j += 1
    else:
        is_prime.append(i)

if is_prime == []:
    print(-1)
else:
    print(sum(is_prime))
    print(is_prime[0])
"""



#11653 #소인수 분해는 작은수부터 나누고 안나누어지면 더 큰수로 나눔
#합성수로 나누어질걱정 -> 어차피 작은수로 나누어져야하기 때문에 X
N = int(input())
prime_divide = []

i = 2
while N > 1:
    if N % i == 0:
        prime_divide.append(i)
        N = N // i
    else:
        i = i + 1

for int in prime_divide:
    print(int)

