'''
            金币
'''
import random
import time

randint=random.randint(10,20)
print(randint)
i=5
n = 0
while True:
    if n == 3:
        print("您输入错误过多")
        time.sleep(10)

    if i==0:
        print('你的金币为0')
        break
    else:
        num=int(input("请输入您猜的数字："))
        if num==randint:
            print('恭喜你猜对了,奖励一个金币')
            i+=1
            n=0
            print("你现在的金币个数为%d" % i)
            randint = random.randint(10, 20)
            print(randint)
            continue

        elif num>randint:
            print('你猜的数太大了，扣一个金币')
            i-=1
            n+=1
            print("你现在的金币个数为%d" %i)
        else:
            print('你猜的数太小了，扣一个金币')
            i-=1
            n += 1
            print("你现在的金币个数为%d" %i)
