
"""
#2745
N, B = input().split()
B = int(B)
result1 = 0
for ch in N:
    if ch.isdigit(): #숫자인지 확인 숫자면 TRUE
        value = int(ch)
    else:
        value = ord(ch) - ord('A') + 10
    result1 = result1 * B + value # 진법계산 이해 좀 더 필요

print(result1)
"""


"""
#11005
keytable = {
    10 : 'A', 11 : 'B', 12 : 'C',
    13 : 'D', 14 : 'E', 15 : 'F',
    16 : 'G', 17 : 'H', 18 : 'I',
    19 : 'J', 20 : 'K', 21 : 'L',
    22 : 'M', 23 : 'N', 24 : 'O',
    25 : 'P', 26 : 'Q', 27 : 'R',
    28 : 'S', 29 : 'T', 30 : 'U',
    31 : 'V', 32 : 'W', 33 : 'X',
    34 : 'Y', 35 : 'Z'
}

N, B = map(int, input().split())
remind = 0
remind_list = []

while N > 0: #B진법 수 로 계속 나눠주면서
    remind_list.append(N % B) #나머지를 리스트에 넣고
    N = N // B

remind_list.reverse()

result1 = []
for ch in remind_list: #딕셔너리 이용하여 10이상의 수 변환
    if ch in keytable:
        result1.append(keytable[ch])
    else:
        result1.append(str(ch)) #str 붙여줘서 문자열 리스트로 만들기

print(''.join(result1)) #join은 문자열만 가능
"""


"""
#2720
T = int(input())
C = [int(input()) for _ in range(T)]
Q, D, N, P = 0, 0, 0, 0
for ch in C:
    Q = ch // 25
    ch = ch % 25
    D = ch // 10
    ch = ch % 10
    N = ch // 5
    ch = ch % 5
    P = ch // 1
    ch = ch % 1

    print(Q, D, N, P)
"""


"""
#2903
N = int(input())
print(( (2 ** N) + 1 ) ** 2)
"""


"""
#2292
N = int(input())
k = 1
while True:
    if N <= ( 1 + ( 3 * (k-1) * k )):
        break
    k = k + 1

print(k)
"""