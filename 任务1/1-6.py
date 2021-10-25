import time

for i in range(3):
    ID=input("请输入用户名：")
    password=input("请输入密码：")
    if ID=="root" and password=="admin":
        print("登录成功")
        break
    else:
        print("登录失败")
        if i==2:
            print("锁定10秒")
            time.sleep(10)