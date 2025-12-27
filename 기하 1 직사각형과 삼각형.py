
"""
#27323
A = int(input())
B = int(input())
print(A*B)
"""


"""
#1085
x, y, w, h = map(int, input().split())
X = 1000 # 가로까지의 최소거리
Y = 1000 # 세로까지의 최소거리
if w - x > x:
    X = x
else:
    X = ( w - x )

if h - y > y:
    Y = y
else:
    Y = ( h - y )

if X > Y:
    print(Y)
elif X < Y:
    print(X)
else:
    print(X)
#min( x, y, w-x, h-y) 한줄이면 끝 (간결하게 짜려고 노력하기)
"""


"""
#3009
(a,b) = map(int, input().split())
(c,d) = map(int, input().split())
(e,f) = map(int, input().split())
(g,h) = 0,0
if a == c:
    g = e
elif c == e:
    g = a
else:
    g = c

if b == d:
    h = f
elif d == f:
    h = b
else:
    h = d

print(g, h)
"""
"""
#XOR 사용 (간결한 코드)
#XOR -> 같은수 0, 다른수 1, (* 0과 어떤 수 N -> N)
#3개의 점 중 X좌표가 같은점 하나 존재 다른 남은 X좌표가 값
x = y = 0
for _ in range(3):
    a, b = map(int, input().split())
    x ^= a
    y ^= b

print(x, y)
"""


"""
#15894
N = int(input())
print(4*N)
"""


"""
#9063
N = int(input())

X_max = -10000
Y_max = -10000
X_min = 10000
Y_min = 10000

for _ in range(N):
    a, b = map(int, input().split())
    X_max = max(X_max, a)
    Y_max = max(Y_max, b)
    X_min = min(X_min, a)
    Y_min = min(Y_min, b)

area = (X_max - X_min) * (Y_max - Y_min)
print(area)
"""


"""
#10101
a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print("Error")
elif a == b == c:
    print("Equilateral")
elif a == b or a == c or b == c:
    print("Isosceles")
else:
    print("Scalene")
"""


"""
#5073
result_list = []
while True:

    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    if a + b <= c or b + c <= a or a + c <= b:
        result_list.append("Invalid")
    elif a == b == c:
        result_list.append("Equilateral")
    elif a == b or a == c or b == c:
        result_list.append("Isosceles")
    else:
        result_list.append("Scalene")

print(*result_list, sep="\n")
"""


"""
#14215
list1 = list(map(int, input().split()))
list1.sort()

if list1[0] + list1[1] <= list1[2]:
    list1[2] = list1[0] + list1[1] - 1

print(sum(list1))

#변수사용 -> 간결
a, b, c = sorted(map(int, input().split()))
if a + b <= c:
    c = a + b - 1
print(a + b + c)
"""