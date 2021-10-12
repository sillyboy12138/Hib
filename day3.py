import random
List=["晶晶","洛洛","猛虎王","狂野猩","暴龙神","冲击波","龙卷风","风火轮","超音速"]
Listt=["偷能源紫水晶","攻打雷霆殿","深陷火龙山谷"]
while True:
	cho=input("输入1开始选人,输入2开始生成处罚遍数,输入3选择原因,输入q或Q查看结果：")
	if cho=='1':
		cell=random.choice(List)
	elif cho=='2':
		Num=random.randint(0,90)
	elif cho=='3':
		res=random.choice(Listt)
	elif cho=='q' or cho=='Q':
		break
print(cell,'因为',res,'被处罚了',Num,'遍')


