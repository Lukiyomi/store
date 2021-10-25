while True:
    print("请分别输入三角形的三边")
    a=int(input("请输入a:"))
    b=int(input("请输入b:"))
    c=int(input("请输入c："))
    print("当三角形的三边分别为：",a,b,c,"时")
    if a+b>c and a+c>b and b+c>a and a-b<c and a-c<b and b-c<a and a*b*c!=0:
        print("可以构成三角形！")
        if a==b==c:
            print("构成等边三角形！")
        elif a == b or a == c or b == c:
            print("构成等腰三角形！")
        elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
            print("构成直角三角形！")
        else:
            print("构成普通三角形！")
    else:
        print("不能构成三角形！")