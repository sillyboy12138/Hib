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
class User(object):
	username=""
	namee=""
	password=""
		
	def add_user(self):
		cur.execute("INSERT INTO icbc(username,namee,password) VALUES('%s','%s','%s')"%(self.username,self.namee,self.password))
		db.commit()

class Adress(User):
	country=""
	province=""
	street=""
	gate=""

	def add_user(self):
		cur.execute("UPDATE icbc SET country='%s',province='%s',street='%s',gate='%s' WHERE username='%s'"%(a.country,self.province,self.street,self.gate,u.username))
		db.commit()

class Bank(User):
	moneyy=""

	def add_user(self):
		cur.execute("UPDATE icbc SET moneyy='%s' WHERE username='%s'"%(m.moneyy,u.username))
		db.commit()
		print(myinfo.format(username=u.username,
							namee=u.namee,
							password=u.password,
							country=a.country,
							province=a.province,
							street=a.street,
							gate=a.gate,
							moneyy=m.moneyy
							))

	def save_money(self):
		user_index=USER.index(Id)
		while True:
			save_password=input("请输入您的密码：")
			if save_password==PASSWORD[user_index]:
				change_money=float(input("请输入要存多少钱："))
				money=float(MONEYY[user_index])+change_money
				cur.execute("UPDATE icbc SET moneyy='%s' WHERE username='%s'"%(money,Id))
				db.commit()
				print("存款成功！当前账户：",Id,"余额为：",money)
				break
			else:
				print("密码输入错误！")

	def draw_money(self):
		user_index=USER.index(Id)
		while True:
			save_password=input("请输入您的密码：")
			if save_password==PASSWORD[user_index]:
				change_money=float(input("请输入要取多少钱："))
				if change_money>float(MONEYY[user_index]):
					print("余额不足！")
				else:
					money=float(MONEYY[user_index])-change_money
					cur.execute("UPDATE icbc SET moneyy='%s' WHERE username='%s'"%(money,Id))
					db.commit()
					print("取款成功！当前账户：",Id,"余额为：",float(MONEYY[user_index])-change_money)
					break
			else:
				print("密码输入错误！")

	def transfer(self):
		user_index=USER.index(Id)
		while True:
			save_password=input("请输入您的密码：")
			if save_password==PASSWORD[user_index]:
				change_user=input("请输入转入账户：")
				if change_user not in USER:
					print("用户不存在！")
				else:
					change_money=float(input("请输入转账金额："))
					if change_money>float(MONEYY[user_index]):
						print("余额不足！")
					else:
						cur.execute("UPDATE icbc SET moneyy='%s' WHERE username='%s'"%(float(MONEYY[user_index])-change_money,Id))
						cur.execute("UPDATE icbc SET moneyy='%s' WHERE username='%s'"%(float(MONEYY[user_index])+change_money,change_user))
						db.commit()
						print("转账成功！")
						break
			else:
				print("密码输入错误！")

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
		u=User()
		a=Adress()
		m=Bank()
		myinfo='''
			\033[0;32;40m
			------------账户信息------------
			账号：{username}
			姓名：{namee}
			密码：{password}
			地址：
				国家：{country}
				省份：{province}
				街道：{street}
				门牌号：{gate}
			账户余额：{moneyy}
			-------------------------------
			\033[0m
'''
		if choice==1:
			Id_chaxun()
			while True:
				Id=input("请输入您的账号：")
				if Id in USER:
					print("该用户已存在！！")
				else:
					u.username=random.randint(10000000,99999999)
					u.namee=input("请输入您的名字：")
					u.password=input("请输入您的密码：")				
					a.country=input("请输入您的国家：")
					a.province=input("请输入您的省份：")
					a.street=input("请输入您的街道：")
					a.gate=input("请输入您的门牌号：")					
					m.moneyy=input("请输入开户存的金额：")
					u.add_user()
					a.add_user()
					m.add_user()
					break

					
		elif choice==2:
			Id_chaxun()
			while True:
				Id=input("请输入您的账号：")
				if Id not in USER:
					print("该用户不存在！！")
				else:
					m.save_money()
					break

		elif choice==3:
			Id_chaxun()
			while True:
				Id=input("请输入您的账号：")
				if Id not in USER:
					print("该用户不存在！！")
				else:
					m.draw_money()
					break
		elif choice==4:
			Id_chaxun()
			while True:
				Id=input("请输入您的账号：")
				if Id not in USER:
					print("该用户不存在！！")
				else:
					m.transfer()
					break
		elif choice==5:
			Id_chaxun()
			while True:
				Id=input("请输入您的账号：")
				if Id not in USER:
					print("该用户不存在！！")
				else:
					chaxun()
					break
		elif choice==6:
			exit()
		else:
			print("业务序号输入有误！")
