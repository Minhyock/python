# 클래스
# class 클래스명 : 
#   pass
# someone = 클래스명()

# 클래스의 생성자
# 두 개 이상의 생성자를 가질 수 없다.
# 생성자 함수의 이름은 __init__()
# self : 클래스 내부에서 __init__() 함수의 첫번째 매개변수로 지정, 객체명을 받는 용도이며 생략 불가

# def __init__(self) : 기본 생성자
# def __init__(self, a, b) : 전달인자 2개를 받는 생성자

# 클래스 선언 방법
#class Person:
#    # pass
#    # 기본 생성자 -> 필수 아님
#    def __init__(self):
#        pass

class Calc:
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = Calc()
a.setdata(3,4)

b = Calc()
Calc.setdata(b, 5, 6)

print(a.first, a.second)
print(b.first, b.second)

# 상속
# 문법 : class 자식클래스명(부모클래스명1, 부모클래스2)

class Car:
    def exclaim(self):
        print("I'm a Car")

class Bus(Car):
    def exclaim(self):
        super().exclaim()
        print("I'm a Bus")


car = Car()
car.exclaim()

bus = Bus()
bus.exclaim()

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
