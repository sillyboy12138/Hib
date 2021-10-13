# ###1###2
# i=1
# list1=[]
# Sum=0
# Max=0
# while i<=10:
# 	print("请输入第",i,"个数")
# 	Num=float(input("："))
# 	i+=1
# 	list1.append(Num)
# for x in range(0,len(list1)):
# 	Sum+=list1[x]
# 	if list1[x]>=Max:
# 		Max=list1[x]
# 	else:
# 		Max=Max

# print("这十个数的最大值为：",Max)
# print("求和结果为：",sum(list1))
# print("平均数为：",Sum/len(list1))


# ###3
# import random
# print("本次50~150之间产生的随机数为：",random.randint(50,150))

# ###4
# def parseTrigon(a,b,c):
# 	if a+b<=c or a+c<=b or b+c<=a:
# 		print('0(非三角形！)')
# 	elif a+b>c or a+c>b or b+c>a:
# 		print('1(普通三角形！)')
# 		if a==b or a==c or b==c:
# 			print('2(等腰三角形！)')
# 		if a==b==c:
# 			print('3(等边三角形！)')
# 		if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
# 			print('4(直角三角形！)')			

# if __name__ == '__main__':
# 	while True:
# 		a=int(input("输入第一条边长："))
# 		b=int(input("输入第二条边长："))
# 		c=int(input("输入第三条边长："))

# 		if 0<a<=10 and 0<b<=10 and 0<c<=10:
# 			parseTrigon(a,b,c)

# 		else:
# 			print('-1(边长不合法！)')
# 			break


###5
# A=56
# B=78
# C=B-A
# A=A+C
# B=B-C
# print("A=",A,"B=",B)


###6
# i=1
# admin=input("用户名:")
# if admin=='root':
# 	while i<=3:
# 		password=input("密码：")
# 		if password!='admin':
# 			print("密码输入错误",i,"次")
# 			i+=1
# 		else:
# 			print("登陆成功！")
# 			break
# else:
# 	print("用户名错误！")
		

###7
# i=int(input("请输入要打印的层数："))
# for x in range(1,i+1):
# 	print((i-x)*' '+x*'* ')

###8
# for i in range(1,10):
# 	for j in range(1,i+1):
# 		print(j,"*",i,"=",i*j,end="  ")
# 	print()


###9
# for i in range(1,10):
# 	for j in range(9,i-1,-1):
# 		print(i,"*",j,"=",i*j,end="  ")
# 	print()


###10
# i=0
# j=0
# height=0
# height+=3
# i+=1
# while height<20:
# 	height-=2
# 	j+=1
# print(i,j)


###11
import random
import time
pu=random.randint(0,100)
i=1

while True:
	number=int(input("请猜0~100的一个数："))
	if number==pu:
		print("猜对了！！")
		if i<=3:
			print(i,"次猜对，奖励10元宝！！")
		elif 3<i<=10:
			print(i,"次猜对，奖励三元宝，继续加油！！")
		else:
			print("再接再厉！！5S后重试")	
			time.sleep(5)
		break
	elif number>pu:
		print("猜大了哦！！")
		i+=1
	else:
		print("猜小了哦！！")
		i+=1


###12
# number=int(input("请输入20以内的一个数："))
# listt=[]
# result=1
# for x in range(1,number+1):
# 	listt.append(x)
# for i in range(len(listt)):
# 	result=result*listt[i]
# print(result)
