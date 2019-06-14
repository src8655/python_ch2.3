import sys

x = object()
print(type(x))
print(sys.getrefcount(x))

y = x
print(sys.getrefcount(y))

# 레퍼런스 값 줄이기
del x
print(sys.getrefcount(y))
print(globals())
