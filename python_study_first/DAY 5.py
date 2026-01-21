# 📚 Python 공부 기록
from logging import exception

## 📅 날짜: 2025-10-19


## 💡 오늘 학습 내용


# while 반복문 (조건이 참이면 계속 반복)
#selected = None
#while selected not in ['가위', '바위', '보']: # 이 요소들이 입력되지않으면 계속해서 반복
    #selected = input('가위, 바위, 보 중에 하나를 입력해주세요: ')

#print(selected)
# 반복횟수가 정해져 있다면 -> for, 조건이 만족할때까지 무한정 반복 -> while


# break - 반복문을 종료시킨다
list = [1, 3, 5, 6, 9]
for i in list:
    if i % 3 == 0:
        print(i)
        break # 3만 출력 하고 break를 만나 반복문 종료

print()
# 짝수만 출력하는 코드
for i in range(5):
    if i % 2 == 0:
        print(i)
print()

for i in range(5):
    if i % 2 != 0:
        continue # 홀수가 나오면 continue 값을 만나 반복문의 나머지 부분을 보지않고 처음으로
    print(i)

# 예외 처리
i = 5
try: # 오류가 발생할 수 있는 코드
    print(list.pop(i))
except IndexError: # 오류가 발생했을 때 처리 할 코드
    print('{} 인덱스는 없습니다'.format(i))
# 에러코드를 모를때는 그냥 except만
# 에러를 알고싶을 때
try:
    text = 'abc'
    number = int(text)
except Exception as ex: # ex에 에러를 받아와 출력
    print(ex)


# raise - 예외를 의도적으로 발생시킴
allowed = ['가위', '바위', '보']
def rsp (mine, yours):
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError
try:
    rsp('가위', '바보')
except ValueError:
    print('허용되지 않는 값입니다.')
# raise를 이용하여 중첩된 반복문 종료 가능


# 논리연산
if False and True: # 앞 조건만 보고 판단 가능할 때는 뒤 조건을 보지않음
    print(True)    # -> 단락평가
else:
    print(False)
# +) or, bool값 등등 but 기본적인거라 넘어가겠음.
# 구분	False	        True
# 숫자	숫자 0	        숫자 0을 제외한 모든 수
# 문자열	빈 문자열('')	빈 문자열을 제외한 모든 문자열
# 리스트	빈 리스트([])	빈 리스트를 제외한 모든 리스트
# 딕셔너리 빈 딕셔너리({})	빈 딕셔너리를 제외한 모든 딕셔너리
# 기타	None 오브젝트



## ✍️ 주요 코드 예제