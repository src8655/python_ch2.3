import sys

i1 = 10
i2 = 10
print(hex(id(i1)), hex(id(i2)))

i1 = 1234567890
i2 = 1234567890
print(hex(id(i1)), hex(id(i2)))

i1 = 11
i2 = 10 + 1
print(hex(id(i1)), hex(id(i2)))

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(hex(id(l1)), hex(id(l2)))

s1 = 'hello'
s2 = 'hello'
print(hex(id(s1)), hex(id(s2)))

# is (동일 레퍼런스 비교)
print(i1 is i2)
print(i1 == i2)

print(l1 is l2)
print(l1 == l2)

# ?
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(sys.getrefcount(t1), sys.getrefcount(t2))
print(t1 is t2)

t3 = tuple(range(1, 4))
print(sys.getrefcount(t3))
print(t1 is t3)
