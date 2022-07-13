# 문자열의 특징
# 1. 파이썬은 유니코드를 지원한다.
# 2. 문자열지정은 '문자열', "문자열", '''문자열''', """문자열"""
# 3. ''', """ -> 여러줄로 구성된 문자열을 만들 수 있다.

# 이스케이프문자
# \n : 줄바꿈
# \t : 탭
# \\ : 역슬래쉬
# \' : 따옴표
# \" : 쌍따옴표

a = 'hello World'
b = """Hello World"""
c = 'Hello\tWorld'
d = '''Hello


World'''
print(a)
print(b)
print(c)
print(d)

# Hello "World"
a = "Hello \"World\""
print(a)
a = 'Hello "World"'
print(a)

a = 'Hello'
b = 'World'
print(a+b)
# 문자열과 숫자는 + 연산이 안 됨

a = '*' * 40
print(a)

# 문자열 포매팅
# %d : 정수
# %f : 실수
# %s : 문자열
# %c : 문자 1개
# %o : 8진수
# %x : 16진수
# %% : %문자
old = 30
a = "나는 %d살 입니다."%old
print(a)

# 나는 25살이고 키는 172.5cm입니다.
old = 25
height = 172.5
s = "나는 %d살이고 키는 %fcm입니다."%(old, height)
print(s)

# format() : 문자열 내에 {} 괄호를 입력하고
# format 함수 인수로 삽입할 변수 또는 값을 입력하면
# {} 괄호 자리에 차례로 인수 값이 전달된다.

a = "나는 {}살이고 키는 {}cm입니다.".format(old, height)
print(a)

a = "숫자 {},{},{}".format(1,2,3)
print(a)

a = "숫자 {2},{1},{0}".format(1,2,3)    # 번지 지정 가능
print(a)