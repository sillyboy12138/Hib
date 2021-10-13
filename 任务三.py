###1
import pymysql
db=pymysql.connect(host="localhost",port=3306,user="root",password="",db="test",charset="utf8")
cur=db.cursor()
#sql1='CREATE TABLE 公司职员信息 (姓名 CHAR(10),年龄 CHAR(10),性别 CHAR(20),编号 CHAR(10),任职公司 CHAR(20),薪资 CHAR(10),部门编号 CHAR(10));'
cur.execute('SELECT name,moneyy FROM 公司职员信息')
money=cur.fetchall()
cur.execute('SELECT name,age FROM 公司职员信息')
age=cur.fetchall()
Sum_money=0
Sum_age=0
for x in range(len(money)):
	Sum_money+=int(money[x][1])
	Sum_age+=int(age[x][1])
#1
print("每人的平均薪资为：",Sum_money/len(money))
#2
print("每人的平均年龄为：",Sum_age/len(age))
#3
cur.execute('INSERT INTO 公司职员信息 VALUES("刘备","45","男","220","alibaba",500,"30")')
db.commit()
cur.execute('SELECT name,sex from 公司职员信息')
sex=cur.fetchall()
man=0
women=0
for i in range(len(sex)):
	if sex[i][1]=='男':
		man+=1	
	else:
		women+=1
#4
print("男性有",man,"人,女性有",women,"人")
cur.execute('SELECT id_dept FROM 公司职员信息')
id_dept=cur.fetchall()
result={}
for dept in set(id_dept):
	result[dept]=id_dept.count(dept)
#5
print(result)
cur.close()
db.close()


###2
List=[["罗恩", 23 ,35 ,44],["哈利" ,60, 77 ,68 ,88, 90],["赫敏", 97 ,99 ,89 ,91, 95, 90],["马尔福" ,100, 85 ,90]]
for i in range(len(List)):
	summ=0
	for j in range(1,len(List[i])):
		summ+=List[i][j]
	print(List[i][0],"",summ)


###3
#猜测输出1，2，3，4，5
num=54321
while num!=0:
	print(num%10)
	num=num//10


###4
a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
for i in range(0,len(a)):
	for j in range(1,len(a)-i):
		if a[j-1]<a[j]:
			a[j-1],a[j]=a[j],a[j-1]
print(a)
