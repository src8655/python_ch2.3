# 주소를 복사한다
import copy

a = 1
b = a

a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]
y = x

print(x)
print(y)

# copy 모듈을 이용한 복사 : 주소 말고 내용을 복사

# 1. 얕은 복사 : 1단계에서 복사 끝
a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]
y = copy.copy(x)

print(x is y)           # 변수의 주소는 다르다
print(x == y)           # 변수의 값은 같다
print(x[0] is y[0])     # 하지만 변수 안의 리스트([])를 가리키는 주소는 같다 => 얕은복사임
print(x)
print(y)

# 2. 깊은 복사 : 끝까지 복사하는 것
a = [1, 2, 3]
b = [4, 5, a]
x = [a, b, 100]
y = copy.deepcopy(x)

print(x is y)               # 변수의 주소는 다르다
print(x == y)               # 변수의 값은 같다
print(x[0] is y[0])         # 변수 안의 리스트([])를 가리키는 주소도 다르다
print(x[1][2] is y[1][2])   # 변수 안의 변수 안의 리스트를 가리키는 주소도 다르다
print(x)
print(y)


# 복합객체 : 얕은복사, 깊은복사 차이가 없다
a = ['hello', 'world']
b = copy.copy(a)
print(a is b)
print(a[0] is b[0])
b = copy.deepcopy(a)
print(a is b)
print(a[0] is b[0])