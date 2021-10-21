'''
随即点名然后处罚遍数
#优化代码：只有一个input 进行判断 1or2 生成人名or几遍    q or Q退出  输入其他的直接锁死time.sleep(10)睡10秒
'''
import random
import time

list=["法外狂徒","小李子","汤老师","郭达","强森","抖森","小罗伯特","汉弗莱","兰尼斯特","千纸鹤"]
print("输入1生成人名，输入2生成处罚遍数，输入Q或q退出，输入其他直接锁死10秒")
while True:
    index=input("请输入：")
    if index=="1":
        dint=random.randint(0,len(list)-1)#生成人名
        print(list[dint])
    elif index=="2":
        num=random.randint(0,10)#生成处罚遍数
        print(num,"遍")
    elif index=="q" or index3=="Q":
        print("退出系统")
        break
    else:
        time.sleep(10)
