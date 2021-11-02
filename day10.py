class Cup(object):
	__high=0
	__volume=0
	__color=''
	__material=''
	
	def setHigh(self,high):
		if high<=0 or high>50:
			print("你的杯子不太合理！")
		else:
			self.__high=high
	def getHigh(self):
		return self.__high

	def setVolume(self,volume):
		if volume<=0 or volume>1000:
			print("你的杯子能装东西吗？")
		else:
			self.__volume=volume
	def getVolumn(self):
		return self.__volume

	def setColor(self,color):
		self.__color=color
	def getColor(self):
		return self.__color

	def setMaterial(self,material):
		self.__material=material
	def getMaterial(self):
		return self.__material

	def save(self,name):
		print("一个",self.__high,"cm的",self.__color,self.__material,"杯能装",self.__volume,"毫升的",name)

class Computer(object):

	__size=0
	__much=0
	__type=''
	__savesize=0
	__time=0

	def setSize(self,size):
		if size<=0 or size>40:
			print("有这样大小的电脑吗？？")
		else:
			self.__size=size
	def getSize(self):
		return self.__size

	def setMuch(self,much):
		if much<=0 or much>100000:
			print("电脑价格不合理吧？？")
		else:
			self.__much=much
	def getMuch(self):
		return self.__much

	def setTypee(self,typee):
			self.__typee=typee
	def getTypee(self):
		return self.__typee

	def setSavesize(self,savesize):
		if savesize<=0 or savesize>4000:
			print("有这样大小的电脑吗？？")
		else:
			self.__savesize=savesize
	def getSize(self):
		return self.__savesize

	def setTime(self,time):
		if time<=0 or time>20:
			print("电脑待机正常吗？？")
		else:
			self.__time=time
	def getSize(self):
		return self.__time

	def write(self,app):
		print("我正在用",app,"练习打字！")

	def playgame(self,gamename):
		print("隔壁老王正在用我",self.__much,"元买的",self.__typee,"打",gamename)

	def looking(self,connect):
		print("小尹用我的",self.__savesize,"GB大小的电脑再看",connect)

	def showMe(self):
		print("我有一台电脑，他的屏幕：",self.__size
			,"英寸，价格：",self.__much
			,"元，cpu型号：",self.__typee
			,"，内存大小:",self.__savesize
			,"GB，待机时长：",self.__time
			,"h")

high=15
volume=500
color='屎黄色'
material='钢筋混凝土'
c=Cup()
c.setHigh(high)
c.setMaterial(material)
c.setColor(color)
c.setVolume(volume)
c.save('岩浆')

com=Computer()
com.setSize(15.6)
com.setMuch(7800)
com.setTypee('酷睿i5')
com.setSavesize(512)
com.setTime(12)

com.write('金山打字')
com.playgame('开心消消乐')
com.looking('苍老师的小电影')

com.showMe()