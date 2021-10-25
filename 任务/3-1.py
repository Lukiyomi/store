# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]

money=0
age=0
for i in range(len(names)):
    money+=names[i][5]
    age+=int(names[i][1])
print(money/(i+1))
print(age/(i+1))

names.append(["刘备","45","男","220","alibaba",500,"30"])
print(names)

man = 0
woman = 0
j=0
while True:
    if names[j][2]=="男":
        man+=1
        j+=1
    elif names[j][2]=="女":
        woman+=1
        j+=1
    if j==len(names):
        break
print('公司男员工为%d名，女员工为%d名' %(man ,woman))

fifty=0
sixty=0
ten=0
thirty=0
h=0
while True:
    if names[h][6]=="50":
        fifty+=1
        h+=1
    elif names[h][6]=="60":
        sixty += 1
        h+=1
    elif names[h][6]=="10":
        ten += 1
        h+=1
    elif names[h][6]=="30":
        thirty+=1
        h+=1
    if h==len(names):
        break
print("公司部门50里有%d名员工，部门60里有%d名员工，部门10里有%d名员工，部门30里有%d名员工" %(fifty,sixty,ten,thirty))