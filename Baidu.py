

f = open(file="baidu_x_system.log",mode="r+",encoding="utf-8")
data = f.readlines()
# print(data[0][12])
num1 = 0#IP地址为：10.155.24.132的登录次数
num2 = 0#IP地址为：16.155.34.132的登录次数
num3 = 0#IP地址为：56.78.35.131的登录次数
num4 = 0#IP地址为：46.76.185.36的登录次数

for i in data:
    if "10.155.24.132" in i:
        num1 += 1
    elif "16.155.34.132" in i:
        num2 += 1
    elif "56.78.35.131 " in i:
        num3 += 1
    elif "46.76.185.36 " in i:
        num4 += 1
print("IP地址为：10.155.24.132的登录次数",num1,"次!")
print("IP地址为：16.155.34.132的登录次数",num2,"次!")
print("IP地址为：56.78.35.131的登录次数",num3,"次!")
print("IP地址为：46.76.185.36的登录次数",num4,"次!")
