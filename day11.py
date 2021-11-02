import time
class Phone(object):
	def __init__(self,brand):
		self.__brand=brand

	def call(self,number):
		print("正在用",self.__brand,"给",number,"打电话")

	def introduce(self):
		print('品牌为：',self.__brand,'的手机很好用')

class Cellphone(Phone):
	def newcall(self,number):
		print("语音拨号中")
		for i in range(5):
			print('.',end='')
			time.sleep(1)
		
		print('正在给',number,'打电话')

p=Phone('nubia')
c=Cellphone('诺基亚')

c.call('13344445554')
c.introduce()
c.newcall('14455556666')

print("===================================")
class ChefA(object):
	def __init__(self,name,age):
		self.__name=name
		self.__age = age
		
	def cookingz(self):
		print("烧开水，下排骨，小火慢炖四十五分钟")

	def showMe(self):
		print("姓名：",self.__name,"年龄：",self.__age)

class ChefB(ChefA):
	def cookingc(self):
		print("烧热油，下排骨，大火爆炒十分钟")

class ChefC(ChefB):
	def cookingz(self):
		print("不烧开水，不下排骨，炖个干锅")
	def cookingc(self):
		print("不倒油，下生姜辣椒，炒个黑暗料理")


ca=ChefA('米其·梅耶',3)
cb=ChefB('米林·尼耶',5)
cc=ChefC('其林·梅尼',35)

cc.showMe()
cc.cookingc()
cc.cookingz()
print('===================================')

class Person(object):
	age=0
	sex=''
	name=''
	def setAge(self,age):
		self.age=age
	def getAge(self):
		return self.age

	def setSex(self,sex):
		self.sex=sex
	def getSex(self):
		return self.sex

	def setName(self,name):
		self.name=name
	def getName(self):
		return self.name

class Working(Person):
	def do(self):
		print("一名",self.age,"的",self.sex,"性工人正在干活，他有一个响亮的名字叫",self.name)

class Student(Person):
	def setId(self,Id):
		self.Id=Id
	def getId(self):
		return self.Id

	def study(self,subject):
		print("学号为",self.Id,"的",self.name,"正在学习",subject)

	def sing(self,song):
		print('一个',self.age,'的',self.sex,'孩子正在唱',song)

p=Person()
p.setAge(12)
p.setSex('男')
p.setName('工藤新一')
w=Working()
w.age=43
w.sex='男'
w.name='毛利小五郎'
s=Student()
s.age=12
s.sex='女'
s.name='工藤静香'
s.setId('11100')
w.do()
s.study('苍老师的招牌动作')
s.sing('妹妹背着洋娃娃')
		













		