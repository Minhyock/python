# 내장함수
print(int("100"))
print(int("100", 16))    # "100"을 16진수로 표현
print(int("100", 8))     # 8진수
print(int("100", 2))     # 2진수

print(float("10.01"))

a = "홍길동,홍길순,이말똥"
print(a.split(","))                    # , 기준으로 열 나누어 list로 나타냄
print(a.replace("홍길동", "김길동"))    # "홍길동"을 "김길동"으로 변경

a = -1
print(abs(a))               # 절대값

print(all([True, True]))    # and 연산, 모두 같은 값일 때 True, 다른 값이 존재하면 False
print(any([0,1]))           # or 연산, 둘 중 하나가 True일 때 True(0은 False 혹은 값 없음으로 취급)

# 유니코드 변경
print(chr(97))
print(ord('a'))


print(bin(10))  # 2진수(0b) xx
print(oct(10))  # 8진수(0o) xx
print(hex(10))  # 16진수(0x) xx

# type확인
a = 10
print(isinstance(a, int))
print(isinstance(a, str))