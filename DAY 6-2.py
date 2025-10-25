# 📚 Python 공부 기록


## 📅 날짜: 2025-10-25


## 💡 오늘 학습 내용

# 클래스와 인스턴스

# 클래스 - 함수나 변수들을 모아놓은 집합체

# 인스턴스 - 클래스에서 셍성된 객체, 각자 자신의 값을 가지고 있음
"""
class Human(): # 클래스 생성

person1 = Human() # 인스턴스 생성
person2 = Human()

person1.name = '김세찬'
person2.name = '김다현'

person1.age = 21
person2.age = 20

def speak(person):
    print('{}의 나이는 {}살'.format(person.name, person.age))

Human.speak = speak # 클래스 안에 추가
person1.speak() # 추가 되어있으므로 호출만
person2.speak()

# 모델링 클래스로 현실의 게념을 표현

def create_human(name, weight):
    person = Human()
    person.name = name
    person.weight = weight
    return person

Human.create = create_human

person = Human.create("방민", 66) # Human.create를 Human 함수에 속성으로 붙인다

def walk(person):
    person.weight -= 1
    print('{}가 걸어서 {}kg이 되었습니다.'.format(person.name, person.weight))

Human.walk = walk # 인스턴스 메서드

person.walk()
"""

# 메소드 - 클래스에 묶여서 클래스의 인스턴스 관련된 일을 하는 함수
# 위에 코드에서 함수를 클래스 안으로 넣어줌 -> 따로 넣어주는 작업 X
"""
class Human( ):
    '''인간'''

    def __init__(self, name, weight):
        '''초기화 함수'''
        print("__init__실행")
        print("이름은 {}, 몸무게는 {}kg".format(name, weight))

    def create( name, weight ): # 다음 강의에서 자세히 설명
        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat(self):
        self.weight += 0.1
        print("{}이 먹어서 {}kg이 되었습니다".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{}이 걸어서 {}kg이 되었습니다".format(self.name, self.weight))

    def speak(self, massage ):
        print(massage)

person = Human.create("방민", 66)
person.eat()
# self = 메소드의 첫 번째 인자
person.speak('안녕하세요') # 인스턴스가 자동으로 self로 들어감
"""


# 특수한 메소드

class Human( ):
    """인간"""

    def __init__(self, name, weight): # 별도로 create 함수 필요 X
        '''초기화 함수'''
        print("__init__실행")
        self.name = name
        self.weight = weight

    def __str__(self):
        return "{} (이름) {}kg (몸무게)".format(self.name, self.weight)

    def eat(self):
        self.weight += 0.1
        print("{}이 먹어서 {}kg이 되었습니다".format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print("{}이 걸어서 {}kg이 되었습니다".format(self.name, self.weight))

    def speak(self, massage ):
        print(massage)

bangmin = Human("bangmin", 66)
bangmin.eat()
print(bangmin) # 인스턴스 자체를 출력하면  __str__ 에서 정의한 형식을 지정

## ✍️ 주요 코드 예제