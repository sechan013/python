# 📚 Python 공부 기록
# 다음주 수요일에 사랑니 뽑으러 갑니다..... :(

## 📅 날짜: 2025-10-17


## 💡 오늘 학습 내용

# 오늘 날짜 출력
import datetime
print(datetime.datetime.today())


# 딕셔너리 여러 값을 저장해두고 필요한 값을 꺼내 쓰는 기능
wintable = {  #이름표[값]
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위'
}

def rsp(mine, yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'

result = rsp('바위', '보')

print(result)

massage = {
    'draw' : '비겼네',
    'win' : '이겼다!',
    'lose' : '졌어...'
}

print(massage[result])


#            ↓ 이름표는 문자열 또는 숫자를 주로 사용하지만
dict = {     "이름표"    :    [1,2,3] }
#                           ↑ 값은 리스트를 포함해서 무엇이든 올 수 있습니다.

print( dict["이름표"] )

# 딕셔너리 수정하기
dict2 = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
}

# 수정
dict2['one'] = 4
print( dict2['one'] )

# 추가
dict2['four'] = 4
print( dict2['four'] )

# 삭제
del(dict2['two'])
print(dict2)

# 딕셔너리와 for 반복문
for key in dict2.keys():  # key -> 이름표, value-> 값
    print(key)

for value in dict2.values():
    print(value)

for key, value in dict2.items():
    print('{}의 값은 {}이다.' .format(key,value))
# 딕셔너리를 반복할때 순서는 무작위 <> 리스트


# 리스트와 딕셔너리 공통점
# 생성, 호출, 삭제, 개수확인, 값 확인, 전부 삭제

list = [1,2,3,4,5]

# 개수확인
print(len(dict)), print(len(list))

# 값 확인
print(2 in list), print(2 in dict2.keys())

# 전부 삭제
list.clear(), dict2.clear()
print(list), print(dict2)


# 차이점
# 삭제 - 리스트는 삭제시 순서가 달라짐 [인덱스], 딕셔너리 순서 무관

# 결합
list2 = [6, 7, 8, 9, 10]
list3 = list + list2
print(list3)

dict.update(dict2) # .update() 앞 딕셔너리에 뒤 딕셔너리 덮어쓰기
print(dict)


# 튜플
# 튜플은 리스트와 비슷하지만 한번 생성하면 값의 변경이나 삭제가 불가능
tuple1 = (1,2,3,4,5)
print(tuple1)

mylist = [1,2,3,4,5,6]
tuple2 = tuple(mylist)
print(tuple2)


# 패킹 언패킹
a, b =1, 2
print(a)
print(b)
# 패킹 - 하나의 변수에 여러개의 값을 넣는 것
c = (1, 2) # 튜플
print(c)
# 언패킹 패킹된 변수에서 여러개의 값을 꺼내오는 것
d, e = c
print(d)
print(e)
f = d, e
print(f)

# 두 변수의 값을 교환할때
x = 5
y = 10
x, y =  y, x
print(x) , print(y)


# 튜플을 이용한 리턴 값
age_list = [20, 21, 22]
for a in enumerate(age_list): # a라는 변수에 튜플을 넣어줌
    print('{}번째 값 {}.'.format(a[0], a[1]))

age = {
    '세찬' : 21,
    '다현' : 20
}
for b in age.items(): # 마찬가지로 하나의 변수에 2개를 받아줌 튜플이용
    print('{}의 나이는 {}살.'.format(*b)) # 튜플 앞에 *은 튜플을 쪼개라 라는 뜻



## ✍️ 주요 코드 예제