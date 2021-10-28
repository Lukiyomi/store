
import random
print("*********************************")
print("*           中国工商银行           *")
print("*           账户管理系统           *")
print("*              v1.0             *")
print("*********************************")
print("")
print("*1.开户                          *")
print("*2.存钱                          *")
print("*3.取钱                          *")
print("*4.转账                          *")
print("*5.查询                          *")
print("*6.Bye!                         *")
print("*********************************")

#c初始化银行
bank = {
    'Frank': {'account': 24275182, 'password': '123456', 'country': '中国', 'province': '山东', 'steert': '曹县', 'door': '001', 'money': 9000, 'bank_name': '人民银行'},
    'Frank1': {'account': 24275181, 'password': '123455', 'country': '中国', 'province': '山东', 'steert': '曹县', 'door': '001', 'money': 0, 'bank_name': '保熟人民银行'}
}
#'Frank': {'account': 24275182, 'password': '123456', 'country': '中国', 'province': '山东', 'steert': '曹县', 'door': '001', 'money': 0, 'bank_name': '人民银行'}

#定义一个开户银行
bank_name = "人民银行"

#定义添加到银行
def bankadd(account,name,password,country,province,steert,door):
    if len(bank)>=100:
        return 3
    elif name in bank:
        return 2
    else:
        bank[name]={
            "account":account,
            "password":password,
            "country":country,
            "province":province,
            "steert":steert,
            "door":door,
            "money":0,
            "bank_name":bank_name
        }
        return 1

#定义用户入参
def useradd():
    account = random.randint(10000000,99999999)
    name = input("请输入您的名称：")
    password = input("请输入您的密码：")
    print("请输入您的详细地址")
    country = input("\t\t请输入您的国籍")#\t==Tab  \n==换行
    province = input("\t\t请输入您的省份")
    steert = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    num=bankadd(account,name,password,country,province,steert,door)
    if num ==3:
        print("本银行已满，请到其他银行开户")
    elif num==2:
        print("该用户已存在")
    elif num==1:
        print("恭喜你开户成功，以下是您的详细信息：")
        info = '''
                  ----------个人信息-----------
                  用户名:%s
                  账号:%s
                  密码:******
                  国籍:%s
                  省份:%s
                  街道:%s
                  门牌号:%s
                  余额:%s
                  开户行名称:%s
               '''
        #每个元素都可以传入%
        print(info % (name,account,country,province,steert,door,bank[name]["money"],bank_name))

#存钱
def access():
    name = input("请输入用户名：")
    for i in bank:
        if i == name:
            while True:
                password = input("请输入密码：")
                if bank[i]["password"] == password:
                    print("您的余额为：",bank[i]["money"])
                    money = int(input("请输入您存款的金额："))
                    if money > 0:
                        bank[i]["money"] += money
                        print("您的余额为",money)
                        break
                else:
                    print("密码错误，请重新输入")
        else:
            return False

def withdraw():
    name = input("请输入用户名：")
    for i in bank:
        if i == name:
            password = input("请输入密码：")
            if bank[i]["password"] == password:
                print("您的余额为：",bank[i]['money'])
                money = int(input("请输入您取款的金额："))
                if bank[i]['money'] >= money:
                    bank[i]['money'] -= money
                    print('您的余额为：',bank[i]['money'])
                elif bank[i]['money'] < money:
                    print("您的余额不足")
                    return 3


            else:
                return 2
        else:
            return 1

def card():
    name = input("请输入转出用户名：")
    name1 = input("请输入转入用户名：")
    for i in bank:
        if i == name:
            for j in bank:
                if j == name1:
                    num = int(input("请输入转出账号："))
                    num1 = int(input("请输入转入账号："))
                    if bank[i]['account'] == num and bank[j]['account'] == num1:
                        password = input("请输入转出账号密码：")
                        if bank[i]['password'] == password:
                            money = int(input("请输入转出金额："))
                            if bank[i]['money'] >= money:
                                bank[i]['money'] -= money
                                bank[j]['money'] += money
                            else:
                                return 3
                        else:
                            return 2
                    else:
                        return 1
            else:
                return 1

def inquire():
    name = input("请输入用户名：")
    for i in bank:
        if i == name:
            password = input("请输入用户密码：")
            if bank[i]['password'] == password:
                print("ok")
                info = '''
                          当前账号:%s
                          密码:******
                          余额:%s元
                          用户居住地址%s%s%s%s
                          当前账户的开户行:%s
                        '''
                print(info % (bank[name]['account'],bank[name]["money"],bank[name]['country'],bank[name]['province'],bank[name]['steert'],bank[name]['door'],bank_name))
                break
            else:
                print("密码错误")
        else:
            print("该用户不存在！")


while False==0:
    index=int(input("请输入您需要的业务："))
    if index==1:
        print("开户")
        useradd()
        print(bank)
    elif index==2:
        print("存钱")
        access()
    elif index==3:
        print("取钱")
        withdraw()
    elif index==4:
        print("转账")
        card()
    elif index==5:
        print("查询")
        inquire()
    elif index==6:
        print("Bye")
        break