
high=20#井的高度
up=3#白天爬的高度
down=2#晚上下降的高度
day=1#天数
while True:
    if day*up-(day-1)*down>=high:
        print("青蛙爬出需要%d天" %day)
        break
    elif day*up-day*down>=high:
        print("青蛙爬出需要%d天" %day)
        break
    else:
        day+=1
'''

high=20#高度
up=3#向上
down=2#向下
num=0#爬了多高
day=1#天数
while True:
    try:
        num+=up
        if num >= high:
            break
        else:
            day+=1
            num-=down
    except:
        break
print("青蛙爬出需要", day, "天")
'''