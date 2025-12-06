"""
#2738
N, M = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(N)]
matrix2 = [list(map(int, input().split())) for _ in range(N)]
matrix3 = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

for row in matrix3:
    print(*row)
"""


"""
#2556
matrix = [list(map(int, input().split())) for _ in range(9)]

max_value = 0
R, O = 0, 0

for i in range(9):
    for j in range(9):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            R, O = i, j
            continue

R = R+1
O = O+1

print(max_value)
print("{} {}".format(R,O))
"""


"""
#10798
matrix = [input() for _ in range(5)]
list1 = []

max_len = 0
for row in matrix:
    if len(row) > max_len:
        max_len = len(row)

for i in range(max_len):
    for j in range(5):
        if i < len(matrix[j]):
            list1.append(matrix[j][i])

print(''.join(list1))
"""


"""
#2563
matrix_p = [[False]*100 for _ in range(100)] # 도화지
N = int(input()) # 검은 색종이 수
for _ in range(N):
    X, Y = map(int, input().split())
    for i in range(10): #세로 이동
        for j in range(10): #가로 이동
            if matrix_p[Y+i][X+j] == False:
                matrix_p[Y+i][X+j] = True
            else:
                continue

count = 0

for i in range(100):
    for j in range(100):
        if matrix_p[i][j] == True:
            count = count + 1

print(count)
"""


"""
#2563 -> SET 활용
# 좌표 자체를 넣는 형태로 구현
colored = set()
N = int(input())
for _ in range(N):
    X, Y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            colored.add((X+i, Y+j))

print(len(colored))
"""