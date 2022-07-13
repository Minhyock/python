# 문자열 슬라이싱
from importlib.resources import path


str = "abcd 가나다라"
print(str)
print(str[0])

# [x:y] : x부터 y-1까지 출력
# [x:y::z] : x부터 y-1까지 z씩 건너뛰면서 출력
print(str[:])       # 문자열 처음부터 끝까지
print(str[4:10])    # index 4부터 9까지
print(str[::2])

# index(x) : x가 몇 번째 문자인지 찾음
print(str.index('가'))

# find(x) : x가 몇 번째 문자인지 찾음
print(str.find('가'))

# 차이점 : index는 없는 문자 검색 시 에러, find는 -1 리턴
# print(str.index('하'))
# print(str.find('하'))

# 경로를 제외하고 파일명 찾기
path = "c:\\test\\abcd\\1234.jpg"
print(path)
print(path.rfind('\\'))
print(path[path.rfind('\\')+1:])

# split : 특정 문자열 기준으로 나머지를 list로 묶음
print(path.split("\\"))

# replace : 특정 문자열을 다른 문자열로 변경
str = "Hello World"
print(str.replace("Hello","Hi"))

# strip : 공백을 제거
str = "            Hello World       "
print(str.strip())  # 양쪽의 공백을 제거

# 대문자 변환 upper()
a = "abcd"
print(a.upper())

# 소문자 변환 lower()
a = "ABCD"
print(a.lower())


a = "aaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbcccccccccccccccccdddddddddd"
# count() : 특정 문자열의 갯수를 리턴
print(a.count('a'))

# len() : 문자열의 길이
print(len(a))

# isalpha() : 알파벳이면 True, 다른 문자(숫자 등)가 섞이면 False
print(a.isalpha())

a = '1234'
# isdecimal() : 10진수인지 판단
print(a.isdecimal())
# isdigit() : 아라비아숫자인지 판단
print(a.isdigit())
# isnumeric() : 숫자(아라비아, 로마 등)인지 판단
print(a.isnumeric())


a = 'abcd'
print(type(a))
# str 클래스의 모든 메소드 출력
# print(dir(str))
# print(dir(float))