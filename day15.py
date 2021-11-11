f=open(r'F:\python自动化\day15【异常处理】\baidu_x_system.log')
listt=[]
Ip=[]
count={}
for i in range(32):
    data=f.readline()
    listt.append(data.split(' '))
    Ip.append(listt[i][0])
for j in set(Ip):
    count[j]=Ip.count(j)
print(count)