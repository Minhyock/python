class Person:
    # 생성자 정의
    def __init__(self, **kwargs):
        self.name = "홍길동"
        self.age = 20
        if "name" in kwargs:
            self.name = kwargs.get("name")
        if "age" in kwargs:
            self.age = kwargs.get("age")
    
    # print() 함수가 실행될 때 호출되는 함수
    def __str__(self):
        return "이름 : {}, 나이 : {}".format(self.name, self.age)
    
    # lt, le : 작다, 작거나 같다
    def __lt__(self, other):
        return self.age < other.age
    def __le__(self, other):
        return self.age <= other.age
    # gt, ge : 크다, 크거나 같다
    def __gt__(self, other):
        return self.age > other.age
    def __ge__(self, other):
        return self.age >= other.age
    # eq, ne : 같다, 같지 않다
    def __eq__(self, other):
        return self.age == other.age
    def __ne__(self, other):
        return self.age != other.age

    # 프로그램이 끝나면 자동으로 호출되는 함수
    # def __del__(self):
    #    print("삭제 되었습니다.")

p = Person()
print("이름 : {}, 나이 : {}".format(p.name, p.age))
# print(dir(Person))
# dir(a) : a 함수에 사용할 수 있는 함수 목록

p1 = Person(name = "김철수")
p2 = Person(name = "이영희", age = 25)
print(p1)
print(p2)

if p1.age >= p2.age:
    print("{} 는(이) {} 보다 나이가 많다.".format(p1.name, p2.name))
else:
    print("{} 는(이) {} 보다 나이가 많지않다.".format(p1.name, p2.name))

print(p1 <= p2)
print(p1 < p2)
print(p1 > p2)