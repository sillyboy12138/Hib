import random
import pymysql
db=pymysql.connect(host='localhost',port=3306,user='root',password='',db='test',charset='utf8')
cur=db.cursor()

print('''
	********************************************
	*               中国工商银行                *
	*               账户管理系统                *
	*                  v1.0                    *         
	********************************************
	*1·开户                                    *
	*2·存钱                                    *
	*3·取钱                                    *
	*4·转账                                    *
	*5·查询                                    *
	*6·退出                                    *
	********************************************
	''')

def add_user(x):
	username=random.randint(10000000,99999999)
	namee=input("请输入姓名：")
	password=input("请输入账户密码：")
	country=input("请输入您的国籍：")
	province=input("请输入您的居住省份：")
	street=input("请输入您的街道：")
	gate=input("请输入您的门牌号：")
	moneyy=input("请输入您开户时存入的金额：")
	cur.execute("INSERT INTO icbc(username,namee,password,country,province,street,gate,moneyy) VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"%(username,namee,password,country,province,street,gate,moneyy))
	db.commit()
	print("创建成功！您当前账户为：",username,"！密码：",password,"！余额：",moneyy,"！")
		
def money_save():
	user_index=USER.index(Id)
	while True:
		save_password=input("请输入账户密码：")
		if save_password==PASSWORD[user_index]:
			Change_money=float(input("请输入存款金额："))
			MONEYY[user_index]+=Change_money
			cur.execute("UPDATE icbc SET moneyy='%s' WHERE username='%s'"%(MONEYY[user_index],Id))
			db.commit()
			print("存款成功！当前账户:",Id,"余额为：",MONEYY[user_index])
			break
		else:
			print("密码输入错误！！")

def money_draw():
	user_index=USER.index(Id)
	while True:
		save_password=input("请输入账户密码：")
		if save_password==PASSWORD[user_index]:
			Change_money=float(input("请输入取款金额："))
			if Change_money>MONEYY[user_index]:
				print("余额不足！！")
				break
			else:
				MONEYY[user_index]-=Change_money
				cur.execute("UPDATE icbc SET moneyy='%s' WHERE username='%s'"%(MONEYY[user_index],Id))
				db.commit()
				print("取款成功！当前账户:",Id,"余额为：",MONEYY[user_index])
				break
		else:
			print("密码输入错误！！")

def money_transfer():
	user_index=USER.index(Id)
	while True:
		save_password=input("请输入账户密码：")
		if save_password==PASSWORD[user_index]:
			user_Id=input("请输入转入账户：")
			if user_Id not in USER:
				print("您输入的账户不存在！请检查！！")
			else:
				user_Idindex=USER.index(user_Id)
				Change_money=float(input("请输入转账金额："))
				if Change_money>MONEYY[user_index]:
					print("余额不足！！")
					break
				else:
					MONEYY[user_index]-=Change_money
					MONEYY[user_Idindex]+=Change_money
					cur.execute("UPDATE icbc SET moneyy='%s' WHERE username='%s'"%(MONEYY[user_index],Id))
					cur.execute("UPDATE icbc SET moneyy='%s' WHERE username='%s'"%(MONEYY[user_Idindex],user_Id))
					db.commit()
					print("转账成功！当前账户:",Id,"余额为：",MONEYY[user_index])
					break
		else:
			print("密码输入错误！！")

def chaxun():
	user_index=USER.index(Id)
	while True:
		save_password=input("请输入账户密码：")
		if save_password==PASSWORD[user_index]:
			cur.execute("SELECT * FROM icbc WHERE username='%s'"%(Id))
			print(cur.fetchall())
			break
		else:
			print("密码输入错误！！")

def Id_chaxun():
	cur.execute('SELECT username,password,moneyy FROM icbc')
	data_cx=cur.fetchall()
	for x in range(len(data_cx)):
		USER.append(data_cx[x][0])
		PASSWORD.append(data_cx[x][1])
		MONEYY.append(data_cx[x][2])

if __name__ == '__main__':
	while True:
		choice=int(input("请输入要办理的业务序号："))
		USER=[]
		PASSWORD=[]
		MONEYY=[]
		if choice==1:
			Id_chaxun()
			while True:
				Id=input("请输入您的账号：")
				if Id in USER:
					print("该用户已存在！！")
				else:
					add_user(x)
					break

		elif choice==2:
			Id_chaxun()
			while True:
				Id=input("请输入您的账号：")
				if Id not in USER:
					print("用户不存在！！")
				else:
					money_save()
					break

		elif choice==3:
			Id_chaxun()
			while True:
				Id=input("请输入您的账号：")
				if Id not in USER:
					print("用户不存在！！")
				else:
					money_draw()
					break

		elif choice==4:
			Id_chaxun()
			while True:
				Id=input("请输入您的账号：")
				if Id not in USER:
					print("用户不存在！！")
				else:
					money_transfer()
					break

		elif choice==5:
			Id_chaxun()
			while True:
				Id=input("请输入您的账号：")
				if Id not in USER:
					print("用户不存在！！")
				else:
					chaxun()
					break

		elif choice==6:
			exit()
		else:
			print("请正确选择要办理的业务！！")

cur.close()
db.close()

# while True:

# 	def new_user(username,password,country,province,street,gate,money,Id):
		
# 		dictt[Id]['username']=username
# 		dictt[Id]['password']=password
# 		dictt[Id]['country']=country
# 		dictt[Id]['province']=province
# 		dictt[Id]['street']=street
# 		dictt[Id]['gate']=gate
# 		dictt[Id]['money']=money
# 		print('用户',Id,'添加成功！')
# 		print(dictt)

# 	def money_save():
# 		while True:
# 			savemoney=int(input('请输入存款金额：'))
# 			dictt[Id]['money']=dictt[Id]['money']+savemoney
# 			print('存款成功！当前余额为：',dictt[Id]['money'])
# 			ch=input("是否继续存款？1、继续/其他退出")
# 			if ch==1:
# 				continue
# 			else:
# 				break
						
# 	def money_draw():
# 		mon=float(input("请输入要取得金额数："))
# 		if mon>int(dictt[Id]['money']):
# 			print("余额不足！！")
# 		else:
# 			dictt[Id]['money']=int(dictt[Id]['money'])-mon
# 			print("已成功取出",mon,"元，当前账户余额为",dictt[Id]['money'],"元")

# 	def money_transfer():
# 		tId=input("请输入转入账户:")
# 		dictt[tId]['username']=tId
# 		mone=float(input("请输入转账金额："))
# 		if mone<dictt[Id]['money']:
# 			print("余额不足！！")
# 		else:
# 			print("转账成功！！您当前账户余额为：",dictt[Id]['money']-mone,"元！！")

# 	def chaxun():
# 		print('''
# 	******************************
# 	 1.余额 2.账号密码 3.个人信息 
# 	******************************
# 			''')
# 		cho=int(input('请输入要查询的内容：'))
# 		if cho==1:
# 			print(dictt[Id]['money'])
# 		elif cho==2:
# 			print(dictt[Id]['username'],dictt[Id]['password'])
# 		elif cho==3:
# 			print("")
# 		else:
# 			return 1

# 	if __name__ == '__main__':

# 		choice=int(input('请输入要办理的业务序号：'))
# 		if choice==1:
# 			username = input("请输入您的用户名：")
# 			if username in data:
# 				pass
# 			password = input("请输入您的开户密码：")
# 			country = input("请输入您的国籍：")
# 			province = input("请输入您的居住省份：")
# 			street = input("请输入您的街道：")
# 			gate = input("请输入您的门牌号：")
# 			money = int (input("请输入您开户时存入的金额："))
# 			Id=random.randint(10000000,99999999)
# 			print("你的账户为：",Id)
# 			dictt[Id]={}
# 			new_user(username,password,country,province,street,gate,money,Id)
# 		elif choice==2:
# 			x=0
# 			Id=input("请输入要操作的账户：")
# 			for m in dictt:
# 				if Id==m:
# 					passw=input("请输入账户密码：")
# 					if passw==dictt[Id]['password']:
# 						money_save()
# 					else:
# 						x+=1
# 						print("密码第",x,"次错误！！")
# 						if x>=3:
# 							print("账户已锁定！！")
# 							exit()
# 				else:
# 					print("用户不存在！！")
# 		elif choice==3:
# 			x=0
# 			Id=input("请输入要操作的账户：")
# 			for n in dictt:
# 				if Id==n:
# 					passw=input("请输入账户密码：")
# 					if passw==dictt[Id]['password']:
# 						money_draw()
# 					else:
# 						x+=1
# 						print("密码第",x,"次错误！！")
# 						if x>=3:
# 							print("账户已锁定！！")
# 							exit()
# 				else:
# 					print("用户不存在！！")	
# 		elif choice==4:
# 			x=0
# 			Id=input("请输入要操作的账户：")
# 			for o in dictt:
# 				if Id==o:
# 					passw=input("请输入账户密码：")
# 					if passw==dictt[Id]['password']:
# 						money_transfer()
# 					else:
# 						x+=1
# 						print("密码第",x,"次错误！！")	
# 						if x>=3:
# 							print("账户已锁定！！")
# 							exit()
# 				else:
# 					print("用户不存在！！")	
# 		elif choice==5: 
# 			x=0
# 			Id=input("请输入要操作的账户：")
# 			for p in dictt:
# 				if Id==p:
# 					passw=input("请输入账户密码：")
# 					if passw==dictt[Id]['password']:
# 						chaxun()
# 					else:
# 						x+=1
# 						print("密码第",x,"次错误！！")
# 						if x>=3:
# 							print("账户已锁定！！")
# 							exit()
# 				else:
# 					print("用户不存在！！")	
# 		elif choice==6: 
# 			exit()
# 		else:
# 			print("输入有误！！")
# 			continue

