
import xlrd

wb = xlrd.open_workbook(filename="2020年每个月的销售情况.xlsx",encoding_override=True)

day = 0#天数
num = 0#数量
downjacket = 0#羽绒服
jeans = 0#牛仔裤
windcoat = 0#风衣
fur = 0#皮草
Tshirt = 0#T血
vest = 0#马甲
businesssuit = 0#小西装
furclothing = 0#皮衣
shirt = 0#衬衫
casualpants = 0#休闲裤
fleece = 0#卫衣
paddedcoat = 0#棉衣
pencilpants = 0#铅笔裤




list = [0,1,2,3,4,5,6,7,8,9,10,11]
for j in range(len(list)):
    st = wb.sheet_by_index(j)
    cold = st.col_values(1)
    cold1 = st.col_values(4)
    cold2 = st.col_values(2)
    for i in range(len(cold[1:])+1):
        if cold[i] == "羽绒服":
            downjacket += int(cold1[i] * cold2[i])
        elif cold[i] == "牛仔裤":
            jeans += int(cold1[i] * cold2[i])
        elif cold[i] == "风衣":
            windcoat += int(cold1[i] * cold2[i])
        elif cold[i] == "皮草":
            fur += int(cold1[i] * cold2[i])
        elif cold[i] == "T血":
            Tshirt += int(cold1[i] * cold2[i])
        elif cold[i] == "马甲":
            vest += int(cold1[i] * cold2[i])
        elif cold[i] == "小西装":
            businesssuit += int(cold1[i] * cold2[i])
        elif cold[i] == "皮衣":
            furclothing += int(cold1[i] * cold2[i])
        elif cold[i] == "衬衫":
            shirt += int(cold1[i] * cold2[i])
        elif cold[i] == "休闲裤":
            casualpants += int(cold1[i] * cold2[i])
        elif cold[i] == "卫衣":
            fleece += int(cold1[i] * cold2[i])
        elif cold[i] == "棉衣":
            paddedcoat += int(cold1[i] * cold2[i])
        elif cold[i] == "铅笔裤":
            pencilpants += int(cold1[i] * cold2[i])
    for h in range(len(cold1[1:])):
        day += 1
        num += int(cold1[h+1])
    for x in range(len(cold[1:])+1):
        downjacket_num = 0  # 羽绒服
        jeans_num = 0  # 牛仔裤
        windcoat_num = 0  # 风衣
        fur_num = 0  # 皮草
        Tshirt_num = 0  # T血
        vest_num = 0  # 马甲
        businesssuit_num = 0  # 小西装
        furclothing_num = 0  # 皮衣
        shirt_num = 0  # 衬衫
        casualpants_num = 0  # 休闲裤
        fleece_num = 0  # 卫衣
        paddedcoat_num = 0  # 棉衣
        pencilpants_num = 0  # 铅笔裤
        clothing_num = [downjacket_num, jeans_num, windcoat_num, fur_num, Tshirt_num, vest_num, businesssuit_num,furclothing_num, shirt_num, casualpants_num, fleece_num, paddedcoat_num, pencilpants_num]
        if cold[x] == "羽绒服":
            downjacket_num += int(cold1[x])
        elif cold[x] == "牛仔裤":
            jeans_num += int(cold1[x])
        elif cold[x] == "风衣":
            windcoat_num += int(cold1[x])
        elif cold[x] == "皮草":
            fur_num += int(cold1[x])
        elif cold[x] == "T血":
            Tshirt_num += int(cold1[x])
        elif cold[x] == "马甲":
            vest_num += int(cold1[x])
        elif cold[x] == "小西装":
            businesssuit_num += int(cold1[x])
        elif cold[x] == "皮衣":
            furclothing_num += int(cold1[x])
        elif cold[x] == "衬衫":
            shirt_num += int(cold1[x])
        elif cold[x] == "休闲裤":
            casualpants_num += int(cold1[x])
        elif cold[x] == "卫衣":
            fleece_num += int(cold1[x])
        elif cold[x] == "棉衣":
            paddedcoat_num += int(cold1[x])
        elif cold[x] == "铅笔裤":
            pencilpants_num += int(cold1[x])
        elif x == len(cold[1:]) + 1:
            print("%d月的羽绒服销售量·" % x, downjacket_num)
            print("%d月的牛仔裤销售量·" % x, jeans_num)
            print("%d月的风衣销售量·" % x, windcoat_num)
            print("%d月的皮草销售量·" % x, fur_num)
            print("%d月的T血销售量·" % x, Tshirt_num)
            print("%d月的马甲销售量·" % x, vest_num)
            print("%d月的小西装销售量·" % x, businesssuit_num)
            print("%d月的皮衣销售量·" % x, furclothing_num)
            print("%d月的衬衫销售量·" % x, shirt_num)
            print("%d月的休闲裤销售量·" % x, casualpants_num)
            print("%d月的卫衣销售量·" % x, fleece_num)
            print("%d月的棉衣销售量·" % x, paddedcoat_num)
            print("%d月的铅笔裤销售量·" % x, pencilpants_num)
sum = downjacket + jeans + windcoat + fur + Tshirt + vest + businesssuit + furclothing + shirt + casualpants + fleece + paddedcoat + pencilpants
mean = num / day
print("2020年销售总额为：",sum)
print("平均每日销售数量为：",round(mean,2))
