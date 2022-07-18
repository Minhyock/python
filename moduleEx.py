# import person
# 모듈의 이름을 생략하고 클래스명이나 함수명으로 바로 쓸 수 있다.
from person import Person, add


# person1 = person.Person(name="김개똥", age=30)
person1 = Person(name="김개똥", age = 30)
print(person1)
print(add(1,5))