##4-1

# dict1={"k1":"v1","k2":"v2","k3":"v3"}

# for i in dict1:
# 	print(i)
# 	print(dict1[i])

# dict1.update({"k4":"v4"})
# dict1['k5']="v5"
# print(dict1)

##4-2

# info={"苹果":"32.8","香蕉":"22","葡萄":"15.5"}
Friutm=[]
friutm=[]
Friutg=[]
friutg=[]
Friuts={
	"苹果":12.3,
	"草莓":4.5,
	"香蕉":6.3,
	"葡萄":5.8,
	"橘子":6.4,
	"樱桃":15.8
}
info={
	'小明':{'friuts':{'苹果':4,'草莓':13,'香蕉':10},'money':''},
	'小刚':{'friuts':{'葡萄':19,'橘子':12,'樱桃':30},'money':''}
}
for i in (info['小明']['friuts']):
	Friutm.append(Friuts[i])
	friutm.append(info['小明']['friuts'][i])

for m in (info['小刚']['friuts']):
	Friutg.append(Friuts[i])
	friutg.append(info['小明']['friuts'][i])
x=0
y=0
money1=0
money2=0
while x<len(Friutm):
	money1=money1+(Friutm[x]*friutm[x])
	x+=1
while y<len(Friutg):
	money2=money2+(Friutg[y]*friutg[y])
	y+=1
info['小明']['money']=money1
info['小刚']['money']=money2
print(info)

##4-3

# List=[]
# while True:
# 	pa=input("请持续输入数字(输入exit可停止传参)：")
# 	if pa=='exit':
# 		break
# 	else:
# 		List.append(pa)
# count_set=set(List)
# count_list=list()
# dict3={}
# for i in count_set:
# 	dict3.update({i:List.count(i)})
# print(dict3)

##4-4

# shux=['姓名','年龄','性别','编号','任职公司','薪资','部门编号']
# names=[
#     ["刘备","56","男","106","IBM",500,"50"],
#     ["大乔","19","女","230","微软",501,"60"],
#     ["小乔","19","女","210","Oracle",600,"60"],
#     ["张飞","45","男","230","Tencent",700,"10"]
# ]

# for i in range(0,len(names)):
	
# 	dict4={names[i][0]:{}}
# 	x=1
# 	while 1<=x<len(names[i]):
# 		dict4[names[i][0]].update({shux[x]:names[i][x]})
# 		# dict4[names[i][0]][shux[x]]=names[i][x]
# 		x+=1
# 	print(dict4)