# 리스트(list)
# 배열과 같은 자료(순서가 있음), 수정이 가능하고, 길이가 가변적이다.
# 리스트의 요소는 일반적으로 같은 타입이지만 다른 타입을 섞어서 저장하는 것도 가능

# 리스트의 생성1
from re import T


a = []
print(type(a))
# 리스트의 생성2
a = list()
print(type(a))

a = [1,2,3,4,5]
print(a)

# 리스트의 데이터 타입은 같을 필요가 없다.
a = ['Hello', 100, 10.5, True]
print(a)

# 리스트의 인덱싱, 슬라이싱
a = [1,2,3,4,5,6]
print(a[0])   # 인덱싱 - int타입
print(a[0:1]) # 슬라이싱 - list 타입
print(a[:])
print(a[-1])

# 리스트의 추가 : append()
a = [1,2,3]
print(a)
a.append(4)
print(a)

# 리스트의 삽입 : insert()
# a.insert(x, y) : x번지에 y값 추가
a.insert(0, 0)
print(a)

# 삭제 : del 인덱스
del a[0]
print(a)

del a[:2]
print(a)

# 삭제 : remove(요소)
a.remove(4)
print(a)

# 삭제 : pop(인덱스) -> 삭제된 값을 리턴
print(a.pop(0))
print(a)

# 리스트의 확장 : extend()
a = [1,2,3]
b = [4,5,6]
print(a + b)    # 기존 리스트 변경 X
a.extend(b)     # 기존 리스트 변경
print(a)

# 정렬
a = [5,6,3,1,2,7]
a.sort() # 오름차순 정렬
print(a)

a.reverse() # 내림차순 정렬
print(a)

a = ['1','2','10','100']
a.sort()
print(a)

# 특정요소 포함 여부
a = [1,2,3,4,5]
print(1 in a)   # a 안에 1 포함되서 True
print(8 in a)   # a 안에 8 미포함으로 False