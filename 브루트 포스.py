
#브루트 포스란 가능한 모든 경우의 수 해보기

"""
#2798
N, M = map(int, input().split())
list1 = list(map(int, input().split()))

result1 = 0
for i in range(N):
    for j in range(i+1,N): #+1을 해줌으로 써 중복 방지
        for k in range(j+1,N):
            tmp = list1[i] + list1[j] + list1[k]
            if tmp <= M and tmp > result1:
                result1 = tmp

print(result1)
"""


"""
#2231
N = int(input())
i = 1
while i < N:
    list1 = [] #list와 result를 밖에서 선언하면
    result1 = 0 #계속해서 쌓이게 됨

    length = len(str(i))
    str_i = str(i)

    for k in range(length):
        list1 += str_i[k]
    for j in list1:
        result1 += int(j)

    result1 += i

    if result1 == N:
        print(i)
        break

    i += 1
else:
    print(0)
"""


"""
#19532
a, b, c, d, e, f = map(int, input().split())
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            found = True
            break
    if found: #x 반복문도 빠져나오기 위함
        break
"""


"""
#1018
M, N = map(int, input().split())

matrix1 = [list(input()) for _ in range(M)]
#띄어쓰기 구분없이 한글자씩

#(map(str, input().split())) for _ in range(M)]
#띄어쓰기 기준으로 하나의 행

answer = 64
for si in range(M-7): #가능한 시작점 돌기
    for sj in range(N-7):
        result1 = 0 #첫 색깔이 W
        result2 = 0 #첫 색깔이 B

        for i in range(si, si+8): #각 시작점에 따른
            for j in range(sj, sj+8): #변경 최소값 구하기

                if (i + j) % 2 == 0: #짝수 칸 -> W
                    if matrix1[i][j] != "W":
                        result1 += 1
                    if matrix1[i][j] != "B":
                        result2 += 1
                else:
                    if matrix1[i][j] != "B":
                        result1 += 1
                    if matrix1[i][j] != "W":
                        result2 += 1

        answer = min(answer, result1, result2)

print(answer)
"""


"""
#1436
N = int(input())
devil_num = []
i = 1
while len(devil_num) != N:
    if "666" in str(i):
        devil_num.append(i)
    i += 1

print(devil_num[N-1])
"""


"""
#2839
N = int(input())
least = 5000 #최소값은 항상 반복문 밖 (계속 초기화 방지)
for i in range(0, N//3):
    for j in range(0, N//5):
        total = i + j
        if (3*i) + (5*j) == N:
            least = min(total, least)

if least != 5000:
    print(least)
else:
    print(-1)
"""