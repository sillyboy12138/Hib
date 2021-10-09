import random
import time
pu=random.randint(0,100)
while True:
	number=int(input("请猜0~100的一个数："))
	if number==pu:
		print("猜对了！！")
		break
	elif number>pu:
		print("猜大了哦！！")
		continue
	else:
		print("猜小了哦！！")
time.sleep(3)
