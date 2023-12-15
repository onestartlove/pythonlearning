
a = int(input('a的值：'))
b = int(input('b的值：'))
c = int(input('c的值：'))
if a < b:
    a, b = b, a
if b > c:
    print("排列后：", a, b, c)
elif a > c:
    print("排列后：", a, c, b)
else:
    print("排列后：", c, a, b)

