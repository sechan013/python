# 📚 Python 공부 기록


## 📅 날짜: 2025-10-29


## 💡 오늘 학습 내용

# 상속

class Animal():
    def eat(self):
        print("밥을 먹었습니다.")

    def walk(self):
        print("걸어갑니다.")

class Human(Animal): # 클래스 생성시 괄호안에 상속하고 싶은 부모클래스 넣기
    def wave(self):
        print("손을 흔듭니다.")

class Dog(Animal):
    def wag(self):
        print("꼬리를 흔듭니다.")

man = Human()
man.eat() # 자식 클래스의 인스턴스는 부모 클래스의 메소드 사용 가능
man.wave()

dog = Dog()
dog.walk()
dog.wag()


class Cow(Animal):
    def eat(self): # 단순 오버라이드
        print("소가 밥을 먹소")

cow = Cow()
cow.eat() # 상속을 해도 따로 자정을 해주면 부모 클래스를 덮어 쓰게된다.
print()
print()

# super()

class study():
    def __init__(self, name):
        self.name = name

    def work(self):
        print("{}가 공부를 한다".format(self.name))

class hands(study):
    def __init__(self, name, hand):
       super().__init__(name)               # super()을 이용하여 초기화 함수에서  반복을 피한다
       self.hand = hand

    def talk(self):
        super().work() # super() 이용 불러오기
        print("{}으로 글을 쓰면서".format(self.hand))

dada = hands("다다", "오른손")
dada.talk()
print()
print()

# list Comprehension
list1 = []
for i in range(10):
    list1 = list1 + [i*i]
print(list1)

list2 = [ i*i for i in range(10) ] # [계산식 for문] list comprehension 사용 -> 코드 간편화
print(list2)

list3 = [ i*i for i in range(10) if i % 2 == 0 ] # [ 계산식 for문 조건문 ]
print(list3)

tuple1 = [ ( x, y ) for x in range(15) for y in range(15) ] # [ 계산식 for문 for문 ]
print(tuple1)
print()
print()

# Dictionary Comprehension

students = ['세찬', '다현', '방민']
students_dict = { "{}번".format(num + 1): name for num, name in enumerate(students) }
print(students_dict) # enumerate [ 형식 for문 ]

scores = [100, 78, 45]
scores_dict = {name: score for name, score in zip(students, scores)}
print(scores_dict) # zip 두개이상의 리스트를 하나로 묶음


## ✍️ 주요 코드 예제