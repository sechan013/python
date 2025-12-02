# 백준 심화1 예제 풀이

"""
#3003
k, q, l, b, n, p = map(int, input().split())
list1 = []
if k != 1:
    if 1-k > 0:
        list1.append(1-k)
    elif 1-k < 0:
        list1.append(-(k-1))
else:
    list1.append(0)

if q != 1:
    if 1-q > 0:
        list1.append(1-q)
    elif 1-q < 0:
        list1.append(-(q-1))
else:
    list1.append(0)

if l != 2:
    if 2-l > 0:
        list1.append(2-l)
    elif 2-l < 0:
        list1.append(-(l-2))
else:
    list1.append(0)

if b != 2:
    if 2-b > 0:
        list1.append(2-b)
    elif 2-b < 0:
        list1.append(-(b-2))
else:
    list1.append(0)

if n != 2:
    if 2-n > 0:
        list1.append(2-n)
    elif 2-n < 0:
        list1.append(-(n-2))
else:
    list1.append(0)

if p != 8:
    if 8-p > 0:
        list1.append(8-p)
    elif 8-p < 0:
        list1.append(-(p-8))
else:
    list1.append(0)

print(*list1)
"""

"""
#2444
N = int(input())
for i in range(1, N+1):
    print(" " * (N-i) + "*" * ((2*i) -1))

for i in range((N-1), 0, -1):
    print(" " * (N-i) + "*" * ((2*i) -1))
"""

"""
#10988
S = input()
count = 1 # 미리 1로 두고 하는게 깔끔
for i in range(len(S)//2):
    if S[i] != S[-i-1]:
        count = 0
        break

print(count)
"""


"""
#1157
#딕셔너리 이용
S = input()
A = S.upper()
dict = {
    'A' : 0, 'B' : 0, 'C' : 0,
    'D' : 0, 'E' : 0, 'F' : 0,
    'G' : 0, 'H' : 0, 'I' : 0,
    'J' : 0, 'K' : 0, 'L' : 0,
    'M' : 0, 'N' : 0, 'O' : 0,
    'P' : 0, 'Q' : 0, 'R' : 0,
    'S' : 0, 'T' : 0, 'U' : 0,
    'V' : 0, 'W' : 0, 'X' : 0,
    'Y' : 0, 'Z' : 0
}

for i in range(len(A)):
    dict[A[i]] = dict[A[i]] + 1

max = 0

for value in dict.values():
    if value > max:
        max = value #가장 많이나온 횟수

count = 0

for key in dict.keys():
    if dict[key] == max:
        count = count + 1 #가장 많이 나온
                          #횟수의 갯수

if count > 1:
    print('?')
else:
    for key in dict.keys():
        if dict[key] == max:
            print(key)
"""


"""
#리스트로 구현
S = input()
S = S.upper()  # 모두 대문자로 통일

count = [0] * 26  # A~Z 등장 횟수 저장

# 각 문자 등장 횟수 세기
for ch in S:
    index = ord(ch) - ord('A')  # A→0, B→1, ... Z→25
    count[index] += 1

# 최댓값 찾기
max_value = max(count)

# 최댓값 가진 글자 확인
if count.count(max_value) > 1:
    print('?')
else:
    index = count.index(max_value)
    print(chr(index + ord('A')))  # 인덱스를 다시 문자로 변환
"""


"""
#2941
#1 for 문으로 하면 크로아티아 알파벳을 만났을 때 다음글자를 이미 검사했음에도 중복으로 넣게됨
# -> while문으로 변경, 끝에 i값 더해줌
#2 마지막 글자에 조건에 맞는 알파벳이 들어왔는데 다음 인덱스가 없을때 S[i+1] 이 존재하지않음
# -> S[i+1], S[i+2]를 검사하기전 i+1 < len(S) 조건 추가
S = input()
listC = []
list1 = []
i = 0
while i < len(S):
    if S[i] == 'c':
        if i+1 < len(S) and S[i+1] == '=':
            listC.append(S[i]+S[i+1])
            i = i + 2

        elif i+1 < len(S) and S[i+1] == '-':
            listC.append(S[i]+S[i+1])
            i = i + 2

        else:
            list1.append(S[i])
            i = i + 1

    elif S[i] == 'd':
        if i+1 < len(S) and S[i+1] == 'z':
            if i+2 < len(S) and S[i+2] == '=':
                listC.append(S[i]+S[i+1]+S[i+2])
                i = i + 3
            else:
                list1.append(S[i])
                i = i + 1

        elif i+1 < len(S) and S[i+1] == '-':
            listC.append(S[i]+S[i+1])
            i = i + 2
        else:
            list1.append(S[i])
            i = i + 1

    elif S[i] == 'l':
        if i+1 < len(S) and S[i+1] == 'j':
            listC.append(S[i]+S[i+1])
            i = i + 2
        else:
            list1.append(S[i])
            i = i + 1

    elif S[i] == 'n':
        if i+1 < len(S) and S[i+1] == 'j':
            listC.append(S[i]+S[i+1])
            i = i + 2
        else:
            list1.append(S[i])
            i = i + 1

    elif S[i] == 's':
        if i+1 < len(S) and S[i+1] == '=':
            listC.append(S[i]+S[i+1])
            i = i + 2
        else:
            list1.append(S[i])
            i = i + 1

    elif S[i] == 'z':
        if i+1 < len(S) and S[i+1] == '=':
            listC.append(S[i]+S[i+1])
            i = i + 2
        else:
            list1.append(S[i])
            i = i + 1

    else:
        list1.append(S[i])
        i = i + 1

total = len(list1) + len(listC)
print(total)
"""

"""
#2941
#replace 이용
S = input()
patterns = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for p in patterns:
    S = S.replace(p, "*")

print(len(S))
"""


"""
#1316
N = int(input())
S = [input() for _ in range(N)]
count = N
for word in S: #단어를 넘기기
    list1 = []
    for i in range(len(word)): #단어의 길이만큼
        if word[i] not in list1:
            list1.append(word[i])
        elif word[i] == word[i-1]:
            continue
        else:
            count = count - 1
            break

print(count)
"""


"""
#25206
list1 = []
list2 = []
for _ in range(20):
    S, P, G = input().split()
    
    if G == 'P':
        continue
    
    if G == 'A+':
        list1.append(float(P)*4.5)
    elif G == 'A0':
        list1.append(float(P)*4)
    elif G == 'B+':
        list1.append(float(P)*3.5)
    elif G == 'B0':
        list1.append(float(P)*3)
    elif G == 'C+':
        list1.append(float(P)*2.5)
    elif G == 'C0':
        list1.append(float(P)*2)
    elif G == 'D+':
        list1.append(float(P)*1.5)

    elif G == 'D0':
        list1.append(float(P)*1)
    elif G == 'F':
        list1.append(float(0))
        
    list2.append(float(P))

print(sum(list1)/sum(list2))
"""


