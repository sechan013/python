
"""
#24262
n = int(input())
print(1)
print(0)
"""


"""
#24263
n = int(input())
count = n #수행횟수
degree = 1 #최고차항 <- O(n)

print(count)
print(degree)
"""


"""
#24264
n = int(input())
count = n ** 2 #수행횟수
degree = 2 #최고차항 <- O(n^2)

print(count)
print(degree)
"""


"""
#24265
#안쪽 반복문이 줄어드는 경우
n = int(input())
count = ( n * (n-1) // 2 )
degree = 2 #최고차항 <- O(n^2)

print(count)
print(degree)
"""


"""
#24266
n = int(input())
count = n ** 3
degree = 3 #최고차항 <- O(n^3)

print(count)
print(degree)
"""


"""
#24267
#반복문 3중
#중첩 반복문 수식은 “가장 안쪽 반복 횟수부터 하나씩 Σ로 감싸면 된다”
n = int(input())
count = n * (n-1) * (n-2) // 6 #등차수열의 합 공식 이용..
degree = 3 #최고차항 <- O(n^3)

print(count)
print(degree)
"""


"""
#24313
#n -> 무한대로 커지면 a0는 사실상 의미없기에
#a1 <= c여야 성립
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1 * n0 + a0 <= c*n0 and a1 <= c:
    if a1 <= c:
        print(1)
else:
    print(0)
"""