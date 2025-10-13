# 📚 Python 공부 기록


## 📅 날짜: 2025-10-13


## 💡 오늘 학습 내용

# print 출력
print('Hello World')


# 변수 선언
name = '김세찬'
age = 21
num = 2025

print('저의 이름은', name, '이고', '나이는', age, '살 입니다') # 변수 이용, 문장 구분

print(num + age) # 변수를 이용한 숫자연산

print('21' + '2025') # 숫자를 문자열로 표현 가능


# if 문
""""
if 조건:
    실행문 #들여쓰기
"""

if True:
    print('조건문은 참 입니다.')

# if else 문
""""
if 조건:
    실행문
else:       #if문의 조건이 거짓일 경우 실행
    실행문  
"""
if False:
    pirnt('거짓입니다.')
else:
    print('거짓이 아닙니다.')

# if elif 문 (많은 else문을 사용하면 너무 많은 내부 블럭이 생겨 보기에 불편함) *기능은 동일
if False:
    print('거짓입니다.') # 조건이 참일때 실행
elif True:
    print('elif가 참입니다.') # 조건이 참일때 실행
else:
    print('위에 모두 아닙니다.') # 위 조건들 모두 거짓일때 실행


## ✍️ 주요 코드 예제

# if elif문을 이용한 가위바위보 게임

SCISSOR = '가위'
ROCK = '바위'
PAPER = '보'

WIN = '이겼다!'
DRAW = '비겼다.'
LOSE = '졌다...'

MINE = '보'  # 변수 값을 다르게 지정하면 다른 결과
YOURS = '바위'

if MINE == YOURS:
    print(DRAW)
else:
    if MINE == SCISSOR:
        if YOURS == PAPER:
            print(WIN)
        else:
            print(LOSE)
    elif MINE == ROCK:
        if YOURS == SCISSOR:
            print(WIN)
        else:
            print(LOSE)
    elif MINE == PAPER:
        if YOURS == ROCK:
            print(WIN)
        else:
            print(LOSE)