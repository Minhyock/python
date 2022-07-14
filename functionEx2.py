# 사용자 함수

def 함수명():
    print("함수호출")
    return True

a = 함수명()
print(a)

# 위치 인자를 이용한 함수호출
def resturant(food, drink, dessert):
    return {"food : ":food,"drink : ":drink, "dessert : ":dessert}

result = resturant("스테이크","포도주","케잌")
print(result)

# 매개변수의 이름을 지정하여 호출
result = resturant(drink = "소주", dessert = "국수", food = "피자")
print(result)
print("---------------------------------------------------------------------------------")

# Default parameter : 매개변수에 초기값을 지정하는 것
def resturant2(food="초밥",drink="맥주",dessert="아이스크림"):
    return {"food : ":food,"drink : ":drink, "dessert : ":dessert}

print(resturant2())
print(resturant2("돈부리"))
print(resturant2("돈까스","사케"))
print(resturant2("돈까스","사케","과일"))

c = 10
print(c)
# def add(a, b):
#    global c    # 전역변수의 c : 바깥의 c를 불러옴
#    c = a + b   # 불러온 c를 재정의
#    return c

# print(add(1,2))
# print(c)

# *args, **kwargs : 매개변수 사용
# *args는 전달된 데이터를 tuple로 묶음

def myFunc1(*args):
    print(args)

myFunc1(1,2,3,4,5,'a','b')
myFunc1()

def myFunc2(x, y, *args):
    print(x, y, args)

myFunc2(1,2,3,4,5)  # x, y 이후 전달된 데이터를 tuple로 묶음
# myFunc2(1)    y값이 없어 오류

def myFunc3(*args):
    print(args,"갯수 => ", len(args))

myFunc3(1,2,3,4,5)
myFunc3([1,2,3,4,5])    # list 1개가 tuple이 되어 갯수 1
myFunc3((1,2,3,4,5))    # tuple 1개가 넘어가 갯수 1
myFunc3(*(1,2,3,4,5))   # 전달인자 * 사용 시 unpacking으로 갯수 5개

# **kwargs : 가변 인자를 dict(딕셔너리) 형태로 받음
def myFunc4(**kwargs):
    print(kwargs, type(kwargs))

myFunc4(food="돈까스", drink="콜라", price=9000)

print("---------------------------------------------------------------------------")

def myFunc5(*args,**kwargs):
    print(args,kwargs)

myFunc5(food="돈까스", drink="콜라", price=9000)    # 매핑 해주면 kwargs
myFunc5("돈까스","콜라", 9000)                      # 매핑 없으면 tuple
myFunc5("돈까스","콜라",price=9000)                 # 섞어서 사용(price만 매핑하여 kwargs)

# 변수에 함수 주입
def hi():
    print("hello")

hello = hi
hello()
print(type(hello))

# 함수를 변수로 주입해서 불러옴
def add(a, b):
    return a + b

def calc(func, a, b):
    print("계산결과 {}".format(func(a,b)))

calc(add, 1, 5)
print("-------------------------------------------------------")
# 함수 내부에 함수
# 클로저(함수 내부에 정의된 함수, 외부에서 호출 불가)
def outer_func(func):
    def inner_func(*args, **kwargs):
        print("함수명 : {}".format(func.__name__))
        result = func(*args,**kwargs)
        return result
    return inner_func

f = outer_func(add)
f(10, 20)

def get_input_user(msg,casting=int):
    # 툴팁 : """ """" 의 문장을 함수에 마우스를 가져갈 시 출력됨
    """
    사용자에게 msg를 출력하고 casting 형태를 확인하여 입력된 값을 처리한다.

    Args:
        msg(str) : input 시 출력할 문구
        casting(class) : 사용자에게 입력 받은 값의 자료형
    
    Return:
        user(casting-value) : 사용자에게 입력받은 값
    """
    while True:
        user = casting(input(msg))
        return user

# user = get_input_user("사용자의 이름을 입력하세요 : ", str)
# age = get_input_user("사용자의 나이를 입력하세요 : ", int)
# print(user, age)

# help() : 함수의 정보를 자세히 출력
help(get_input_user)

# __doc__ : docstring(툴팁)만 출력
print(get_input_user.__doc__)

