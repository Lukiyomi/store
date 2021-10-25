
list=[]
max=0
sum=0
for i in range(10):
    num=int(input("请输入数字："))
    list.append(num)
    if max<num:
        max=num
    sum=num+sum
    average=sum/10
print(max)
print(sum)
print(average)