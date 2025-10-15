# 📚 Python 공부 기록


## 📅 날짜: 2025-10-15


## 💡 오늘 학습 내용

# 문자열
# 큰따옴표 ", 작은 따옴표' 상관없이 맞춰주기만 하면 됨

string = '문자열'
print(string)

# 여러줄의 긴 문자열을 쓰고싶다면 '''(문자열)''' 따옴표를 3개씩 묶어주면 된다

long_string = '''긴 문자열은
따옴표 3개로
씁시다.'''
print(long_string)


# 정수와 실수
# 나누기 / 는 기본적으로 실수로 결과값을 냄

age = 21
height1 = 182
height2 = 182.3 #(실수)

print(age, height1, height2)

#나눴을때 정수로 나오게 하려면 //
print(5//3)

height3 = int(182.3) #정수로
age2 = float(21) #실수로

print(height3, age2)
print()

# 사용자 입력받기 input
""""
print('가위, 바위, 보, 중 하나를 입력해주시오', end = '')
mine = input()
print(mine)

yours = input('input은 프린트 기능도 가짐 ')
print(yours)
"""


# 리스트 *배열
list1 = [1, 2, 3]
print(list1)
print(list1[0]) # 첫 번째는 0번부터
print(list1[-1]) # 뒤에서 첫 번째라는 뜻

list1[0] = 4 # 바꿔주기
print(list1)

list1.append(5) # 리스트 끝에 값 넣기
print(list1)

list2 = [6, 7, 8]
list3 = list1 + list2 # 리스트끼리 붙일수도 있음
print(list3)

n = 2
m = n in list3 # in <- 리스트 안에 특정 값이 있는지 확인
print(m)

if n in list3: # 결과가 bool 값이므로 if문등 활용 가능
    print('{}은 있어!'.format(n))

del list3[0] # 리스트의 특정 수를 지우기
print(list3)

list3.remove(2) # 처음으로 나오는 특정 숫자를 지우기
print(list3)


# for 반복문

patterns = ['가위', '바위', '보']
for pattern in patterns: # pattern 이란 변수 안에 리스트의 값을 하나씩 전달
    print(pattern) #반복하여 출력, 리스트의 길이만큼 반복


for i in range(5): # 필요한 만큼 숫자를 만들어냄
    print(i)

print()
for i in range(3):
    num = patterns[i]
    print(num)

print()
names = ['세찬', '다현', '방민']
for j, name in enumerate(names): # 숫자와 리스트의 값을 전달
    print('{}번 : {}' .format(j+1, name))


# 모듈 미리 만들어진 코드를 가져와 씀 (모듈이름.모듈안에 구성요소)
import random
GBB = ['가위', '바위', '보']
s = random.choice(GBB) # random.choice() <- 랜덤으로 정해줌
print(s)



## ✍️ 주요 코드 예제