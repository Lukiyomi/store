'''
分析一个水杯的属性和功能，使用类描述并创建对象
属性：高度，容积，颜色，材质
行为：能存放液体
'''

class Cup:
    __height = 0
    __cubage = 0
    __colour = ""
    __materialquality = ""

    def setHeight(self,height):
        if height < 0 :
            print("水杯的高总得比0大吧！")
        else:
            self.__height = height
    def getHeight(self):
        return self.__height

    def setCubage(self,cubage):
        if cubage < 0:
            print("水杯总得装点东西吧！")
        else:
            self.__cubage = cubage
    def getCubage(self):
        return self.__cubage

    def setColour(self,colour):
        if colour == "":
            print("颜色不能为空！")
        else:
            self.__colour = colour
    def getColour(self):
        return self.__colour

    def setMaterialquality(self,materialquality):
        if materialquality == "":
            print("水杯的材质不能为空！")
        else:
            self.__materialquality = materialquality
    def getMaterialquality(self):
        return self.__materialquality


    def run(self):
        print("这个",self.__colour,"色的水杯，高为",
              self.__height,"厘米，可以存放",self.__cubage,"毫升的",self.__materialquality,"!")

C = Cup()
C.setHeight(10)
C.setCubage(500)
C.setColour("蓝")
C.setMaterialquality("红糖水")

C.run()


'''
有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
'''

class Laptop:
    __size = 0
    __price = 0
    __model = ""
    __memory = 0
    __time = 0

    def setSize(self,size):
        if size < 10 or size >17:
            print("你的笔记本电脑这么大？")
        else:
            self.__size = size
    def getSize(self):
        return self.__size

    def setPrice(self,price):
        self.__price = price
    def getPrice(self):
        return self.__price

    def setModel(self,model):
        if model == "":
            print("电脑型号不能为空")
        else:
            self.__model = model
    def getModel(self):
        return self.__model

    def setMemory(self,memory):
        if memory < 0 or memory >20:
            print("你的笔记本电脑内存这么大？")
        else:
            self.__memory = memory
    def getMemory(self):
        return self.__memory

    def setTime(self,time):
        if time < 0:
            print("你的笔记本电脑待机时间是多少？")
        else:
            self.__time = time
    def getTime(self):
        return self.__time


    def type(self,typenum):
        print("今天有人用这个笔记本电脑打了",typenum,"个字！")

    def playgame(self,gamename,gamehour):
        print("今天有人用这个笔记本电脑打",gamename,"打了",gamehour,"小时！")

    def watchvideo(self,videoname,videohour):
        print("今天有人用这个笔记本电脑看",videoname,"看了",videohour,"小时！")

    def laptop(self):
        print("今田有人以",self.__price,"的价格买下了这个尺寸为",
              self.__size,"寸，型号为",self.__model,"型号，内存为",
              self.__memory,"T，待机可持续",self.__time,"小时的笔记本电脑！")
L = Laptop()
L.setSize(15)
L.setPrice(6999)
L.setModel("XAGE.18.7")
L.setMemory(10)
L.setTime(24)

L.type(5000)
L.playgame("战地",8)
L.watchvideo("权力的游戏",6)
L.laptop()


