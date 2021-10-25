import xlrd	
###各月销售量，销售额
def allmonths(i,namee,numm,moneyy,allmon,allnum):
	for x in range(len(namee)):
		allmon+=numm[x]*moneyy[x]
		allnum+=numm[x]
	print("============================================")
	print(i+1,"月总销售量：",allnum,"总销售额：",round(allmon,2))
	list_num.append(allnum)
	list_money.append(allmon)
	allyear(list_num,list_money,x,allnum,allmon)

def allyear(list_num,list_money,x,allnum,allmon):
	
	print("全年总销售量：",sum(list_num))
	print("全年总销售额：",round(sum(list_money),2))

	clo_num(namee,x_index,allnum,allmon)

def clo_num(namee,x_index,allnum,allmon):
	dictt={str(i+1)+'月':{}}
	for x in namee:
		if x in dictt[str(i+1)+'月']:
			dictt[str(i+1)+'月'][x]+=numm[x_index]
			x_index+=1
			# print(dictt['1月'][x])
		else:
			dictt[str(i+1)+'月'][x]=numm[x_index]
			x_index+=1
	for key in dictt[str(i+1)+'月']:
		print("本月",key,"销售量占比为：",format(dictt[str(i+1)+'月'][key]/sum(numm),'.2%'))

def salenum():
	dictt_num={}
	dictt_mon={}
	x_index=0
	for x in namee:
		if x in dictt:
			dictt_num[x]+=numm[x_index]
			dictt_mon[x]+=round(numm[x_index]*moneyy[x_index],2)
			x_index+=1
		else:
			dictt_num[x]=numm[x_index]
			dictt_mon[x]=round(numm[x_index]*moneyy[x_index],2)
			x_index+=1
	salemon(dictt_num,dictt_mon)

def salemon(dictt_num,dictt_mon):
	mon=0
	for value in dictt_mon:
		mon+=dictt_mon[value]
	print("----------------------------------")
	for x in dictt_mon:
		print("本月",x,"销售额占比为：",format(dictt_mon[x]/mon,'.2%'))
	print("======================================")

def yearsalenum(NAME,NUM,DICT,LIST1,LIST2):
	for i in range(len(NAME)):
		for j in range(len(NAME[i])):
			if NAME[i][j] in DICT:
				DICT[NAME[i][j]]+=NUM[i][j]
			else:
				DICT[NAME[i][j]]=NUM[i][j]
	for x in DICT:
		LIST1.append(x)
		LIST2.append(DICT[x])
	max_index=LIST2.index(max(LIST2))
	min_index=LIST2.index(min(LIST2))
	print("最畅销的衣服是：",LIST1[max_index])
	print("全年销量最低的衣服是：",LIST1[min_index])

def quartersalenum(NAME,NUM):
	for i in range(1,4):
		for j in range(len(NAME[i])):
			if NAME[i][j] in DICTT1:
				DICTT1[NAME[i][j]]+=NUM[i][j]
			else:
				DICTT1[NAME[i][j]]=NUM[i][j]
	for x in DICTT1:
		spring.append(x)
		springmon.append(DICTT1[x])
		maxsp_index=springmon.index(max(springmon))

	for m in range(4,7):
		for n in range(len(NAME[m])):
			if NAME[m][n] in DICTT2:
				DICTT2[NAME[m][n]]+=NUM[m][n]
			else:
				DICTT2[NAME[m][n]]=NUM[m][n]		
	for y in DICTT2:
		summer.append(y)
		summermon.append(DICTT2[y])
		maxsu_index=summermon.index(max(summermon))

	for a in range(7,10):
		for b in range(len(NAME[a])):
			if NAME[a][b] in DICTT3:
				DICTT3[NAME[a][b]]+=NUM[a][b]
			else:
				DICTT3[NAME[a][b]]=NUM[a][b]
	for z in DICTT3:
		autumn.append(z)
		autumnmon.append(DICTT3[z])
		maxa_index=autumnmon.index(max(autumnmon))
	
	for o in [10,11,0]:
		for p in range(len(NAME[o])):
			if NAME[o][p] in DICTT4:
				DICTT4[NAME[o][p]]+=NUM[o][p]
			else:
				DICTT4[NAME[o][p]]=NUM[o][p]
	for q in DICTT4:
		winter.append(q)
		wintermon.append(DICTT4[q])
		maxw_index=wintermon.index(max(wintermon))
	
	print("春季最畅销的衣服：",spring[maxsp_index])
	print("夏季最畅销的衣服：",summer[maxsu_index])
	print("秋季最畅销的衣服：",autumn[maxa_index])
	print("夏季最畅销的衣服：",winter[maxw_index])

if __name__ == '__main__':
	list_num=[]
	list_money=[]
	NAME=[]
	NUM=[]
	LIST1=[]
	LIST2=[]
	spring=[]
	summer=[]
	autumn=[]
	winter=[]
	springmon=[]
	summermon=[]
	autumnmon=[]
	wintermon=[]
	DICT={}
	DICTT1={}
	DICTT2={}
	DICTT3={}
	DICTT4={}
	dictt={}
	dict_clomon={}
	allmon=0
	allnum=0
	x_index=0
	wb=xlrd.open_workbook(filename=r"F:\python自动化\day07\任务\2020年每个月的销售情况.xlsx")
	for i in range(12):
		sheet=wb.sheet_by_index(i)
		namee=sheet.col_values(1,start_rowx=1,end_rowx=None)
		moneyy=sheet.col_values(2,start_rowx=1,end_rowx=None)
		numm=sheet.col_values(4,start_rowx=1,end_rowx=None)
		NAME.append(namee)
		NUM.append(numm)

		allmonths(i,namee,numm,moneyy,allmon,allnum)
		salenum()
	yearsalenum(NAME,NUM,DICT,LIST1,LIST2)
	quartersalenum(NAME,NUM)





















	