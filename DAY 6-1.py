# 📚 Python 공부 기록
# 사랑니 뽑고 아파서 간만에 공부 ;)

## 📅 날짜: 2025-10-25


## 💡 오늘 학습 내용

# list의 다양한 기능

list1 = [1, 2, 3]

list1 = [1, 2, 3] + [4, 5, 6]
print(list1)

list1.extend([7, 8, 9])
print(list1)

print(list1.index(2)) # 2라는 값으로 위치 찾기

list1.insert(9, 10)
print(list1)

list1.reverse() # 역순으로 정리
print(list1)

list1.sort()
print(list1) # 순서대로 정리

# 리스트와 문자열

str = "안녕하세요"
print(str.index('안'))
print(str[1])
print("하" in str)

# 리스트와 문자열은 유사, 서로 변환 가능

# list = str.split() 문자열에서 리스트
words = list("abcdefg")
print(words)

word = "안녕 이건 공백으로 리스트를 구분"
word_list = word.split() # 괄호 안에 넣는 문자 기준으로 쪼개기
print(word_list)

# " ".join(list) 리스트에서 문자열
print(" ".join(word_list))

# slice 리스트나 문자열의 요소를 여러개 가져옴
list2 = list(range(20))
print(list2[0:2]) # 0번 인덱스부터 2번 전까지 0 <= x < 2
print(list2[2:]) # 2번부터 끝까지
print(list2[:2]) #처음부터 2번까지
print(list2[ : ]) #똑같은 리스트 but 기존 것과는 다름
# 기존 것을 변경하는 것이 아닌 새 문자열, 리스트를 만드는 것이므로 기존 것을 복사해놓는 등으로 사용가능

print(list2[5:15:3]) # 5번째부터 3개씩 띄어서
print(list2[14:4:-3]) #반대로

del list2[0:2] #리스트 수정
print(list2)

del list2[6:]
print(list2)

list2[0:3] = [0,1,2] # 0부터 2전까지 바꿔줌
print(list2)

list2[3:6] = [4] #기존 요소보다 더 많거나 적게 바꿀 수 있음
print(list2)

print()

# 자료형
i = 42
print(type(i))
f = 3.14
print(type(f))

print(isinstance(42, int))
print(isinstance(42, float)) # 자료형 확인
## ✍️ 주요 코드 예제