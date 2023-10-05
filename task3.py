string=input("请输入一个字符串")
if"ol" in string:
    new_string=string.replace("ol","fzu")
    reversed_string=new_string[::-1]
    print(reversed_string)
else:
    print("字符串中不含有ol")