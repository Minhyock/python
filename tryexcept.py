# 예외처리
# 방법 1 모든 종류의 오류 처리
# try: 
#   오류 발생 가능 코드
# except:
#   오류처리 코드

# 방법 2 특정 종류의 오류만 처리
# try: 
#   오류 발생 가능 코드
# except 발생 오류: 
#   오류처리 코드

# 방법 3
# try: 
#   오류 발생 가능 코드
# except 발생 오류 as 오류 메시지 변수: 
#   오류처리 코드

# 방법 4
# try: 
#   오류 발생 가능 코드
# except 발생 오류 as 오류 메시지 변수: 
#   오류처리 코드
# else:
#   오류가 발생하지 않았을 때 코드

# 방법 5
# try: 
#   오류 발생 가능 코드
# except 발생 오류: 
#   오류처리 코드
# finally:
#   오류 유무에 관계없이 반드시 처리해야할 코드

# 오류 타입
# NameError : 초기화 하지 않은 변수 사용할 때 발생
# ValueError : 타입은 맞지만 값의 형식이 잘못 되었을 때 발생
# ZeroDivisionError : 0으로 나누었을 때 발생
# IndexError : index의 범위를 넘었을 때 발생
# TypeError : 타입이 맞지 않을 때 발생

a = [1,2,3,4,5]
# a[5] : indexError 발생
b =  "123#"
# c = int(b) : ValueError 발생 #로 인해 int로 변경 불가
# f = open("index.txt") : FileNotFoundError
try:
    f = open("index.txt")
except FileNotFoundError as e:
    print("파일을 찾을 수 없습니다.")
    print(e)
# 오류가 없을 경우 실행
else:
    data = f.read()
    print(data)
    f.close()

# finally
try:
    f = open("index.txt", mode="w", encoding="utf-8")
    f.write("Hello Python")
finally:
    f.close

# 하나의 try가 여러개의 Error를 발생시키는 경우 01(오류의 순서에 따라 출력문 달라짐, 먼저 걸리는 오류)
try:
    a = [1,2,3]
    print(10/0)
    print(a[3])
except IndexError:
    print("리스트의 index를 잘못 사용했습니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

# 02
try:
    a = [1,2,3]
    print(a[3])
    print(10/0)
except (IndexError, ZeroDivisionError) as e:
    print(e)

# 오류의 회피
try:
    f = open("index2.txt")
except FileNotFoundError:
    pass
print("완료")
