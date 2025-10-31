# 📚 Python 공부 기록


## 📅 날짜: 2025-10-31


## 💡 오늘 학습 내용

# datetime
import datetime # 모듈 불러오기

start_time = datetime.datetime.now() # 데이트타임 모듈의 데이트타임 클래스에 접근
print(start_time)

christmas_time = datetime.datetime(2025, 12, 25)
remaing_time = christmas_time - start_time # 남은 시간 계산
print(remaing_time)

print("크리스마스 까지는 {}시간 {}초 남았습니다.".format(remaing_time.days, remaing_time.seconds/3600))
# .days -> 날짜, .seconds -> 초 계산


# timedelta 시간의 연산을 가능하게 해주는 클래스

hundred = datetime.timedelta(days = 100) # 날짜, 시간등 연산 가능
now = datetime.datetime.now() + hundred
print(now)
now = datetime.datetime.now() - hundred
print(now)

hudred_after = datetime.datetime.now().replace(hour = 9, minute = 0, second = 0) + hundred
print(hudred_after) # 100일 뒤에 오전 9시로 바꾸기




## ✍️ 주요 코드 예제