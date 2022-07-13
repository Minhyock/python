# 튜플(tuple)
# 기본적으로 list와 tuple은 동일하다.
# 차이점 : list는 [], tuple은 ()이며 값이 immutable(불변)하다
# list는 값을 생성, 수정, 삭제가 가능하지만 tuple은 값을 바꿀수 없다.
# tuple은 내부 구조가 간단하고 읽는 속도가 빠르다. 그리고 데이터가 안전하기 때문에 자주 사용된다.

# tuple의 생성1
from re import A


a = ()
print(type(a))

# tuple의 생성2
a = tuple()
print(type(a))

a = [1,2,3,4,5]
b = (1,2,3,4,5)
print(type(a),type(b), sep='|', end="마지막 문자") # sep='x' x로 두 문자열 사이를 구분, end="y" y로 마무리
a[0] = 9
# b[0] = 9 - 오류발생
print(a)
print(b)

# 변수 하나에 여러개의 값을 넣으면 튜플로 생성된다.
b = 1,2,3,4,5
print(b)
# 원소 1개인 tuple 생성
b=1,
print(b)

# 패킹 : tuple로 만드는 작업
a = 1,2,3,4
print(a)

# 언패킹 : tuple에서 값을 꺼내는 작업
a1,a2,a3,a4 = a
print(a1,a2,a3,a4)


















