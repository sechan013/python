# 📚 Python 공부 기록
# 백준 풀면서 알아야 하거나 도움되는 개념들 정리

## 📅 날짜: 2025-11-15


## 💡 오늘 학습 내용
"""
a = int(input())    # 정수 1개 입력, input()은 기본적으로 문자열 입력
d, c = map(int, input().split())  # 공백으로 구분된 2개 입력

b = "385" #인덱싱
print(b[0])  # '3'
print(b[1])  # '8'
print(b[2])  # '5'

# (a,b) 튜플 만들기 -> 만들어진 튜플 받아서 곱셈 -> sum() 으로 다 합산
total = sum(a * b for a, b in (map(int, input().split()) for _ in range(N)))


# "구분자".join(리스트)
# 구본자를 사이에 넣어서 리스트를 합침
N = int(input())
list1 = ['long']
list1 = list1 * (N//4)

list1.append('int')

print(" ".join(list1))

# end=" " → print 다음 줄로 넘어가지 않고 공백으로 이어줌
N = int(input())
for i in range(N//4):
    print("long", end = " ")
print("int")


# int사용 하는게 편함
# 하지만 수가 수만 개 이상이면 속도가 느려서 시간 초과
# 이때 사용하는 게 sys.stdin.readline()
import sys
a, b = map(int, sys.stdin.readline().split())



N = int(input())
for i in range(1, N+1): # i값에 1부터 들어가도록 보기쉽게
    print(" " * (N-i) + "*" * i)



# 계속해서 값을 받고싶을때, 조건을 True로 사용
# BUT 끝나지 않기 때문에 예외처리를 해줌
# 로컬 콘솔에서는 ctrl + D 로 종료
while True:
        try:
            a, b = map(int, input().split())
            print(a+b)
        except EOFError:
            break




# 리스트안에 정수를 입력받으면 list()로 정수형 리스트로 변환
# list.count() 로 갯수 세기
N = int(input())
list1 = list(map(int, input().split()))
if len(list1) == N:
    v = int(input())
    print(list1.count(v))
else:
    print("너무 많거나 적은 수를 입력했습니다.")


# 줄 바꿈 없이 쭉 출력 ' ' <- 공백으로 이어서
print(A[i], end=' ')






# enumerate 사용으로 더 간단하게
for x in A[1:]:
    if x > max_value:
        max_value = x

for i in range(9):
    if A[i] == max_value:
        print(max_value)
        print(i+1)
        break

for idx, val in enumerate(A[1:]):
    if val > max_value:
        max_value = val
        max_index = idx+1




# 슬라이싱에서 i:j라면 i부터 j-1 까지
# 리스트를 슬라이싱에 대입할땐 길이를 맞춘 리스트 넣기
# ex) [k] * 4 (그냥 [k]만 입력하면 길이 1짜리로 들어감
#10810
N, M = map(int, input().split())
baskets = [0] * N


for _ in range(M):
    i, j, k = map(int, input().split())
    baskets[i-1:j] = [k] * (j-i+1)

print(*baskets) # * <- 각 요소를 출력



#10813
# 리스트 컴프레힌션으로 간결하게 리스트 생성
# 간단하게 두개 바꾸기
N, M = map(int, input().split())
A = [p for p in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    A[i-1], A[j-1] = A[j-1], A[i-1]

print(*A)




#3052
# set 중복이 자동으로 제거됨, 순서가 없음
# 추가, 삭제 가능, 교집합, 합집합, 차집합 가능
# -> 중복제거에서 자주 쓰임
A = [int(input()) for _ in range(10)]

remain = []

for i in range(10):
    if A[i]%42 in remain:
        remain.append(A[i]%42)

s = set(remain) #중복제거 set*****
print(len(s))



#10811
# 슬라이싱 [::-1] -> 리스트 뒤집기
# 구간만 뒤집기 가능 -> lst[1:4] = lst[1:4][::-1]



#리스트에 정수를 받는 방법들
#1. 한 줄로 받기 공백가쥰
#(1) 리스트 컴프리헨션 A = [int(x) for x in input().split()]
#(2) map A = list(map(int, input().split()))

#2 여러 줄로 받기
#(1) 리스트 컴프리헨션 + 반복
#N = int(input) -> A = [int(input()) for _ in range(N)]

#(2) 반복문 + append
#N = int(input())
#A = [] -> for _ in range(N):
#               A.append(int(input)))

#(3) 가장 간단
#N = int(input())
#M = int(input()) #단 변수가 통제되어있어야함

#11654
#아스키코드 변환 함수 ord()
input(A)
print(ord(A))


#11720
N = int(input())
list1 = [int(x) for x in input()]
#문자열로 받은걸 정수형으로 변경해서 넣기

print(sum(list1))


#10809
idx = ord(S[i]) - ord('a')
#알파벳이 몇번째로 나오는지 'a' -> 0, 'b -> 1...



#2941
# 문자열.replace('기존문자', '치환할 문자')
# return 값으로 주어짐


#5073
print(*result_list, sep="\n")
#separator -> 구본자 -> 줄바꿈하면서 요소들을 하나씩 꺼내라

#줄바꿈 출력 방법
#for x in result_list:
#    print(x)

#print(*result_list, sep="\n")

#print('\n'.join(result_list))
#문자열일때만 가능
#join은 문자열을 만드는 것 vs sep은 출력하는 것

#+) end 줄 바꿈 없이 쭉 출력 ' ' <- 공백으로 이어서
#print(A[i], end=' ')

"""
## ✍️ 주요 코드 예제