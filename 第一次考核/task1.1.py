a=int(input("请输入a"))
b=int(input("请输入b"))
c=int(input("请输入c"))
d=0
if a < b:
    d = a
    a = b
    b = d
if a < c:
    d = a
    a = c
    c = d
if b < c:
    d = b
    b = c
    c = d
    print(a,b,c)
