# print("Hello")

# 줄 단위 실행 => 특정 행에서 실행 오류가 나는 경우 프로그램은 멈추게 됨
# 파이썬 자료형
# 정수형, 문자형, 불린형, 리스트형, 튜플, 딕셔너리, set

# 변수 : 프로그램 안에서 값을 담아놓기 위한 공간(이름 사용)
a = 123
# print(a)

# \n == enter
multiline = "Life is too short\nYou need python"
# print(multiline)

# 커스텀 생성한 모듈 호출하여 사용
# import mod1
# print(mod1.add(5,3))
# print(mod1.add(5,3))

# from mod1 import add
# print(add(0,6))

# * : 모두
from mod1 import *
print(add(2,6))
print(sub(2,6))


