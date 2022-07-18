# 라이브러리
# import
# 모듈은 파이썬 코드를 작성해 놓은 스크립트 파일이다.
# 스크립트 파일 안에는 함수, 변수, 클래스 등이 정의되어 있음
# 외부의 모듈을 가져와서 사용할 때는 import 명령을 사용한다.
# 모듈에 포함된 함수를 호출할 때는 함수명 앞에 모듈명을 붙인다.

import math
print(math.sqrt(2))
# sqrt(x) : x의 제곱근 구하기
# pow(x,y) : x의 y제곱
# ceil(x) : 올림
# floor(x) : 내림
# fabs(x) : 절대값, -1 -> 1
# trunc(x) : x의 소수점 이하 버림, 3.14 -> 3

# 특정 함수만 임포트하곶자 할 때 사용하는 구문
# from 모듈명 import 함수명 or 클래스명

# 모듈의 모든 함수를 불러올 때는 함수명 자리에 * 문자를 사용
# 모듈의 이름이 길고 복잡할 때는 as 다음에 별칭(alias)을 지정할 수 있다.
import math as m
print(m.trunc(3.14))

import os
os.system("cls")    # cls : 콘솔창 초기화
print(os.listdir("c:\\"))   # listdir(x) : x 경로의 폴더 및 파일 리스트

import time
start = time.time() # time() : 현재 시간
# print(start)
# 실행되는 문장
# time.sleep(1)   # sleep(x) : x초 동안 실행 중지
end = time.time()
# print(end)
print(end - start)
t = time.time()
print(time.ctime(t))

import datetime
d = datetime.datetime.now() # 모둘명..함수명
print(d)
print(d.date()) # 날짜값
print(d.time()) # 시간값
print(d.year)   # 년도
print(d.month)  # 월
print(d.day)    # 날짜


import random
print(random.random())      # 무작위 소수 생성
print(random.randint(1,10)) # random.randint(x,y) : x ~ y 사이의 랜덤한 정수 생성

a = ["가위", "바위", "보"]
print(random.choice(a)) # list에서 랜덤하게 값을 출력
random.shuffle(a)       # list에서 순서를 랜덤하게 섞음
print(a)

os.system("cls")

# import requests
# 외부 모듈 설치 : pip install requests


# random() : 0~1 미만의 실수를 랜덤하게 생성
# randint(x, y) : x~y 사이의 무작위 정수 생성(y 포함)
# randrange(x, y) : x~y 사이의 무작위 정수 생성(y 제외)
# uniform(x, y) : x~y 사이의 실수를 랜덤하게 생성
# choice(list 객체) : list에서 임의의 요소를 하나 리턴
# shuffle(list 객체) : list에서 순서를 랜덤하게 변경
# sample(list 객체, n) : list 항목 중 n개를 무작위로 뽑아 새로운 리스트를 만든다.

# calendar 모듈
# calendar 함수는 년도를 인수로 받아 달력 객체를 반환
# month 함수는 년도와 월을 인수롤 받아 해당 월의 달력 객체를 반환
import calendar
print(calendar.calendar(2022))  # calendar(x) : x년의 달력(12개) 출력
print(calendar.month(2022, 7))  # month(x,y) : x년의 y월 달력 출력
