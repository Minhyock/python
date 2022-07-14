# 파이썬에서 파일 읽고 쓰기

# 파일 열기
# 파일 객체 = open(파일명, 파일 열기 모드)

# 파일 열기 모드
# r(읽기 모드) : 파일을 읽기 전용으로 open 할 때 사용, 모드를 생략하면 기본 r 모드로 설정
# w(쓰기 모드) : 파일에 내용을 쓸 때 사용. 파일을 쓰기 모드로 열면 해당 파일이 존재할 경우 원래 있던 내용이 사라지고
#                해당 파일이 존재하지 않을 경우 새로운 파일을 생성
# a(추가 모드) : 파일의 마지막에 새로운 내용을 추가 시킬 때 사용
# t(문자열) : 파일에 저장하는 데이터가 문자열임을 나타냄. 기본으로 문자열 모드로 설정
# b(바이너리) : 바이너리 데이터를 쓸 때 사용

file = open("sample.txt", mode="w", encoding="utf-8")
file.write("Hello Python\n")
file.write("안녕 파이썬\n")
file.close()

file = open("sample.txt", mode="r", encoding = "utf-8")
print(file.read())
file.close()

# with : with 라인이 끝나면 자원을 반환
with open("sample.txt", mode="r", encoding="utf-8") as file:
    print(file.read())

# 연습문제 for문을 이용해서 score.txt라는 파일을 생성하고 
# 학생수 : 00명
# 점수합계 : 000점
# 평균 : 00점
# 최고점수 : 00점
# 최하점수 : 00점

score = {"길동": 89, "영희":78, "철수":88, "순희":90, "민수":95, "개똥":79, "민지":99}

f = open("score.txt", mode="w",encoding="utf-8")

for name, s in score.items():
    f.write(name + ' : ' + str(s) + "점\n")
f.write("학생수 : " + str(len(score)) + "명\n")
f.write("점수 합계 : " + str(sum(score.values())) + "점\n")
f.write("평균 : " + str(sum(score.values())/len(score)) + "점\n")
f.write("최고점수 : " + str(max(score.values())) + "점\n")
f.write("최하점수 : " + str(min(score.values())) + "점\n")
f.close()
print("작업 완료")

p = 3.141592111111111
print(p)
print("%f" %p)
print("%.2f" %p)    # 자릿수 지정
print("%10.5f" %p)  # 자릿수 지정 후 모자란 경우 공백 채움