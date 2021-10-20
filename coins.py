'''
            金币
'''
import random
randint=random.randint(10,20)
print(randint)
i=5
while i<=5:
    if i==0:
        print('你的金币为0')
        break
    else:
        num=int(input("请输入您猜的数字："))
        if num==randint:
            print('恭喜你猜对了')
            break
        elif num>randint:
            print('你猜的数太大了，扣一个金币')
            i=i-1
        else:
            print('你猜的数太小了，扣一个金币')
            i=i-1