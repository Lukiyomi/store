
while True:
    name=input("请输入变量名：")
    if name.isalpha():#.isalpha 判断输入的字符串是否都是字母
        print("变量名合法")
    else:
        print("变量名不合法")