import xlrd
print('''
============================================
日期	  服装名称	价格/件	库存数量	销售量/每日
1号	  羽绒服     253.6	 500	10
2号	  牛仔裤	    86.3	 600	60
3号	  风衣	    96.8	 335	43
4号	  皮草	    135.9	 855	63
5号	  T血	    65.8	 632	63
6号	  衬衫	    49.3	 562	120
7号	  牛仔裤	    86.3	 600	72
8号	  羽绒服	    253.6	 500	69
9号	  牛仔裤 	86.3	 600	35
10号	  羽绒服	    253.6	 500	140
11号	  牛仔裤 	86.3	 600	90
12号	  皮草	    135.9	 855	24
13号	  T血 	    65.8	 632	45
14号	  风衣	    96.8	 335	25
15号	  牛仔裤	    86.3	 600	60
16号	  T血	    65.8	 632	129
17号  羽绒服	    253.6	 500	10
18号	  风衣	    96.8	 335	43
19号	  T血	    65.8	 632	63
20号	  牛仔裤	    86.3	 600	60
21号  皮草	    135.9	 855	63
22号	  风衣	    96.8	 335	60
23号	  T血	    65.8	 632	58
24号  牛仔裤	    86.3	 600	140
25号  T血	    65.8	 632	48
26号	  风衣	    96.8	 335	43
27号	  皮草	    135.9	 855	57
28号  羽绒服	    253.6	 500	10
29号	  T血	    65.8	 632	63
30号	  风衣	    96.8	 335	78
============================================
''')
data=xlrd.open_workbook('0.xls')
table=data.sheet_by_index(0)

list1=table.col_values(1,start_rowx=1,end_rowx=None)
list2=table.col_values(2,start_rowx=1,end_rowx=None)
list3=table.col_values(3,start_rowx=1,end_rowx=None)
list4=table.col_values(4,start_rowx=1,end_rowx=None)

summ=0
allmoney=0
num1=0
num2=0
num3=0
num4=0
num5=0
num6=0
m1=0
m2=0
m3=0
m4=0
m5=0
m6=0
for x in range(0,len(list1)):
	if list1[x]=='羽绒服':
		num1=num1+list4[x]
		m1=m1+list2[x]*list4[x]
	elif list1[x]=='牛仔裤':
		num2=num2+list4[x]
		m2=m2+list2[x]*list4[x]
	elif list1[x]=='风衣':
		num3=num3+list4[x]
		m3=m3+list2[x]*list4[x]
	elif list1[x]=='皮草':
		num4=num4+list4[x]
		m4=m4+list2[x]*list4[x]
	elif list1[x]=='T血':
		num5=num5+list4[x]
		m5=m5+list2[x]*list4[x]
	else:
		num6=num6+list4[x]
		m6=m6+list2[x]*list4[x]

for i in range(len(list1)):
	allmoney=allmoney+list2[i]*list4[i]
	summ=summ+list4[i]

print("总销售量：",summ)
print("平均每日销售数量：",round(summ/30,2))
print("总销售额：",round(allmoney,2))
print('============================================')
print("每个种类月销售量占比情况如下：")
print("羽绒服月销量占比为：",'%.2f%%' %(num1/summ*100))
print("牛仔裤月销量占比为：",format(num2/summ,'.2%'))
print("风衣月销量占比为：",'%.2f%%' %(num3/summ*100))
print("皮草月销量占比为：",format(num4/summ,'.2%'))
print("T血月销量占比为：",'%.2f%%' %(num5/summ*100))
print("衬衫月销量占比为：",format(num6/summ,'.2%'))
print('============================================')
print("每个种类月销售额占比情况如下：")
print("羽绒服月销额占比为：",'%.2f%%' %(m1/allmoney*100))
print("牛仔裤月销额占比为：",format(m2/allmoney,'.2%'))
print("风衣月销额占比为：",'%.2f%%' %(m3/allmoney*100))
print("皮草月销额占比为：",format(m4/allmoney,'.2%'))
print("T血月销额占比为：",'%.2f%%' %(m5/allmoney*100))
print("衬衫月销额占比为：",format(m6/allmoney,'.2%'))
print('============================================')