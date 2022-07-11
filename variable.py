from operator import truediv


print("HelloWorld")
num1 = 3
print(num1)
print(type(num1))
num2 = "5"
print(num2)
print(type(num2))

# print(num1 + num2) : int와 str은 계산 불가

# 변수의 선성
# 1. 변수의 이름은 영문자로 시작
# 2. 대소문자 구분함
# 3. 띄어쓰기는 안됨
# 4. 내장 키워드는 안됨

# 논리형
a = True
b = False
print(a)
print(type(a))

a = bool(True)
print(a)
a = bool(1)
a = bool(0)
print(a)

# 정수형
a = 10
print(a)
print(type(a))

# 실수형
a = 10.1
print(a)
print(type(a))

# 연산자
a = 10
b = 3
# 더하기
print(a+b)
# 빼기
print(a-b)
# 곱하기
print(a*b)
# 나누기(결과값 float으로 바뀜)
print(a/b)
# //(몫 구하기)
print(a//b)
# 나머지 구하기
print(a%b)
# 제곱
print(a**b)

# not
x = True
print(not x)

# and
x = 5 > 2
y = 5 < 4
print(x)
print(y)
print(x and y)

id = "abcd"
print(len(id))
print(len(id) > 3 and len(id) < 13)
print(3 < len(id) < 13)

# or
print(x or y)