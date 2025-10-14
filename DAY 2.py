# 📚 Python 공부 기록


## 📅 날짜: 2025-10-14


## 💡 오늘 학습 내용

#함수 정의
def function():
    print('안녕, 함수야!')

# 만드는 것 만으로는 실행 X

print('첫 줄')
function() # 이때 출력
print('마지막 줄')


def add():
    result = a + b
    print('result =', result)

a = 3
b = 5

add()

# 매개변수

def calculate(q, w, e): # 매개변수, 함수 밖의 변수와는 분리됨
    result = q + w - e
    print('result =', result)

x = 1
y = 2
z = 3

calculate(x, y, z) # 실행인자
calculate(3, 5, 2) # 넣고 싶은 숫자도 바로 가능

def print_round(number): # 반 올림
    rounded = round(number)
    print('반 올림 하면: ', rounded)

print_round(2.6)

# 함수의 값, return

def add2(o, p):
    r1 = o + p
    return r1 # 함수가 r1의 값을 내보냄 , return을 하면 함수는 종료 (뒤에 코드가 더 남아도 끝)

n = add2(1, 2) # n이란 변수에 함수의 값을 넣어줌
print(n)

def add3(o, p):
    r1 = o + p
    r2 = o - p
    return r1, r2 # 2개의 값을 내보내기

v, m = add3(1, 2) # 마찬가지로 두개의 변수로 받아주기
print(v)
print(m)


# format

sen1 = '20'
sen2 = '에 오신 것을'
sen3 = '환영합니다'

# 기존 방식
print(sen1, '번 손님 저희 가게에', sen2, sen3)
# format 이용
print('{} 번 손님 저희 가게에 {} {}' .format(sen1, sen2, sen3))
# format 앞의 . 앞의 객체에 접근, 객체의 기능을 실행? 후에 자세히
# 각각의 방식이 편할 때가 있음
