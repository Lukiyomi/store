
num=int(input("请输入你想输入的数字："))
score=1
for i in range(1,num+1):
    score = score * i

print("数字%d的阶乘为" %num,score)
'''
i=1
while True:
    if i<num+1:
        score = score * i
        i+=1
    elif i>=num+1:
        print("数字%d的阶乘为" %num,score)
        break
'''