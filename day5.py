import random
import time
def shop_show():
	for i,v in enumerate(List):
		print(i,":",v)
	shop_choice()

def shop_choice():
	while True:
		cho=int(input("请选择你需要的商品："))
		if cho<=len(List)-1:
			add_cart(cho,coupon)
		else:
			print("商品选择有误！！")

def add_cart(cho,coupon):
	cart.append(List[cho])
	print("=======================当前已加购物车商品===========================")
	print(cart)
	if 0<len(cart)<=3:
		print("您购买了",len(cart),"件，为您打",coupon/10,"折")
	elif 3<len(cart)<=7:
		print("您购买了",len(cart),"件，为您打",(coupon-10)/10,"折")
	else:
		print("您购买了",len(cart),"件，为您打",(coupon-20)/10,"折")
	discount_coupon(Allmon,coupon,cart)


def discount_coupon(Allmon,coupon,cart):
		for x in range(len(cart)):
			Allmon+=int(cart[x][1])
		if money>=Allmon*coupon/100:
			print("您应付",Allmon,"元，实付",Allmon*coupon/100,"元！！！")
			print("余额",money-Allmon*coupon/100,"元。")
		else:
			print("余额不足！！")
			print("=======================已成功购买的商品=============================")
			cart.pop()
			print(cart)
			time.sleep(5)
			exit()


if __name__ == '__main__':
	List=[
	["死神来了",20000.00],
	["冰冠公主",20990.00],
	["偶像公主",19990.00],
	["白龙吟",1188.00],
	["冠军飞将",1688.00],
	["地狱火",1688.00],
	["冰雪圆舞曲",788.00],
	["一念成魔",1688.00],
	["电玩小子",2888.00],
	["暗影猎兽者",888.00]
	]
	money=float(input("请输入您的现有点券："))
	cart=[]
	Allmon=0
	coupon=90
	shop_show()
