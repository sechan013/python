"""
#28278
import sys #시간초과 대비 (input이 너무 많음)
N = int(sys.stdin.readline())
stack1 = []
for _ in range(N):
    X = sys.stdin.readline().split()
    if X[0] == "1":
        stack1.append(int(X[1]))

    elif X[0] == "2":
        if stack1: #스택이 비었으면 False
            print(stack1.pop()) #가장 top의 원소 제거, 가져오기
        else:
            print(-1)

    elif X[0] == "3":
        print(len(stack1))

    elif X[0] == "4":
        if stack1:
            print(0)
        else:
            print(1)

    elif X[0] == "5":
        if stack1:
            print(stack1[-1]) #스택에서 top의 원소는 stack[-1]
        else:
            print(-1)
"""
from collections import deque

"""
#10773
K = int(input())
stack1 = []
for _ in range(K):
    X = int(input())
    if X != 0:
        stack1.append(X)
    else:
        stack1.pop()

print(sum(stack1))
"""


"""
#9012
T = int(input())
for _ in range(T):
    stack1 = []
    for ch in input():
        if ch == "(":
            stack1.append(ch)
        elif ch == ")":
            if stack1:
                stack1.pop()
            else:
                print("NO")
                break

    else:
        if stack1:
            print("NO")
        else:
            print("YES")
"""


"""
#4949
flag = True
while flag:
    stack1 = []
    S = input()
    if S.rstrip() == ".": #rstrip() 오른쪽 공백 제거 (실수보정)
        break             #_. 은 의도된 것이지만 ._은 실수

    for ch in S:
        if ch == "(":
            stack1.append(ch)
        elif ch == ")":
            if stack1:
                if stack1[-1] == "(":
                    stack1.pop()
                else:
                    print("no")
                    break
            else:
                print("no")
                break
        elif ch == "[":
            stack1.append(ch)
        elif ch == "]":
            if stack1:
                if stack1[-1] == "[":
                    stack1.pop()
                else:
                    print("no")
                    break
            else:
                print("no")
                break

    else: #break가 안나왔을때 -> 스택이 비어있는데 빼는건 없음
        if stack1: #스택이 차있을 때 -> 닫는 괄호 X
            print("no")
        else: #스택이 비어있을 때
            print("yes")
"""


"""
#18258
from collections import deque #덱, 큐 -> deque이용!!
#q.append(1)      # 오른쪽에 넣기
#q.appendleft(2)  # 왼쪽에 넣기
#q.append(1)      # 오른쪽에 넣기
#q.appendleft(2)  # 왼쪽에 넣기
import sys
N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
    X = sys.stdin.readline().split()
    if X[0] == "push":
        q.append(X[1])

    elif X[0] == "pop":
        if q:
            print(q.popleft()) #왼쪽 -> 가장 처음 들어간 수 [0]
        else:
            print(-1)

    elif X[0] == "size":
        print(len(q))

    elif X[0] == "empty":
        if q:
            print(0)
        else:
            print(1)

    elif X[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)

    elif X[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
"""


"""
#2164
from collections import deque
N = int(input())
q = deque()
for i in range(N):
    q.append(i+1)

while len(q) > 1:
    q.popleft()
    q.append(q[0])
    q.popleft()

print(*q)
"""


"""
#28279
import sys
N = int(sys.stdin.readline())
from collections import deque
q = deque()
for _ in range(N):
    X = sys.stdin.readline().split()
    if X[0] == "1":
        q.appendleft(X[1]) #앞에 넣기
    elif X[0] == "2":
        q.append(X[1]) #뒤에 넣기
    elif X[0] == "3":
        print(q.popleft() if q else -1) #맨앞 pop
    elif X[0] == "4":
        print(q.pop() if q else -1) #맨뒤 pop
    elif X[0] == "5":
        print(len(q))
    elif X[0] == "6":
        print(0 if q else 1)
    elif X[0] == "7":
        print(q[0] if q else -1)
    elif X[0] == "8":
        print(q[-1] if q else -1)
"""
