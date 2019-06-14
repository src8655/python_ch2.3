

def f() :
    l_a = 2
    l_b = '마이콜'
    print(locals())


class MyClass:
    x = 10
    y = 20


g_a = 1
g_b = '둘리'

f()
print(globals())

# 1. 정의된 함수
f.k = 'hello'
print(f.__dict__)   # 함수 확장

# 2. 클래스 객체
MyClass.z = 10
print(MyClass.__dict__)
# str.z = 10        # 내장 클래스는 확장할 수 없다
print(str.__dict__)


o = MyClass()
o.x = 100
print(o.__dict__)