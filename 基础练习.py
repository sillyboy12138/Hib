# print('========================1=====================')
# while True:
# 	choice=input('请选择1、摄氏转华氏  2、华氏转摄氏 :')
# 	if choice=='1':
# 		C=float(input("请输入摄氏温度："))
# 		print(C,"对应的华氏温度为：",1.8*C+32)
# 		break
# 	elif choice=='2':
# 		F=float(input("请输入华氏温度："))
# 		print(F,"对应的摄氏温度为：",(F-32)/1.8)
# 		break
# 	else:
# 		print("请重新选择！！")

print('========================2=====================')
while True:
	Rr=float(input("请输入圆的半径："))
	pi=3.1415926
	if Rr>=0:
		print("以",Rr,"为半径的圆的周长为：",round(2*pi*Rr,2),"面积为",round(pi*Rr*Rr,2))
		break
	else:
		print("半径不合法！请重新输入！！")
		continue

# print('========================3=====================')
# while True:
# 	year=int(input("请输入年份："))
# 	if year>=0:
# 		if (year%4==0 and year%100!=0) or (year%400==0):
# 			print(year,"年为闰年！！")
# 			break
# 		else:
# 			print(year,"年不是闰年！！")
# 			break
# 	else:
# 		print("请输入正确的年份！！")
# 		continue

# print('=======================4======================')
# while True:
# 	choice=int(input("请选择1、英寸转厘米 2、厘米转英寸："))
# 	if choice==1:
# 		mil_Num=float(input("请输入数字："))
# 		mil_unit=input("请输入单位：")
# 		if mil_unit=='mil' or mil_unit=='英寸':
# 			print(mil_Num,mil_unit,"=",2.54*mil_Num,"cm")
# 			break
# 		else:
# 			print("单位有误！！")
# 	elif choice==2:
# 		cm_Num=float(input("请输入数字："))
# 		cm_unit=input("请输入单位：")
# 		if cm_unit=='cm' or cm_unit=='厘米':
# 			print(cm_Num,cm_unit,"=",1/2.54*cm_Num,"mil")
# 			break
# 		else:
# 			print("单位有误！！")
# 	else:
# 		print("选择有误！！")

# print('======================5======================')
# def level(grade):
# 	if grade>=90:
# 		print('A')
# 	elif 80<=grade<90:
# 		print('B')
# 	elif 70<=grade<80:
# 		print('C')
# 	elif 60<=grade<70:
# 		print('D')
# 	else:
# 		print('E')

# if __name__ == '__main__':
# 	while True:
# 		grade=float(input("请输入成绩："))
# 		if 0<grade<=100:
# 			level(grade)
# 			break
# 		else:
# 			print("输入有误！！")
# 			continue

# print('======================6======================')
# from math import sqrt
# while True:
# 	a=float(input("第一条边长："))
# 	b=float(input("第二条边长："))
# 	c=float(input("第三条边长："))

# 	if a<0 or b<0 or c<0 or a+b<=c or a+c<=b or b+c<=a:
# 		print("构不成三角形！！")
# 		continue
# 	else:
# 		pl=a+b+c
# 		S=sqrt(pl/2*(pl/2-a)*(pl/2-b)*(pl/2-c))
# 		print("由",a,b,c,"组成的三角形的周长L=：",pl)
# 		print("面积S=",round(S,2))
# 		break
