'''
3cook------lanzi-------6customer
1.5*num      500        3*num
'''
import time
from threading import Thread
import threading
max=0
allnum=0

class Make(Thread):
    coname=''
    cocount=0

    def run(self) -> None:
        global max,allnum
        while True:
            if allnum >=6000:
                threadLock.acquire()
                print(self.coname,"制作了",self.cocount,"个蛋挞，工资为",self.cocount*1.5)
                threadLock.release()
                break
            else:
                if max < 500:
                    self.cocount += 1
                    allnum+=1
                    max += 1
                    threadLock.acquire()
                    print(self.coname, '已经制作了', self.cocount, '个蛋挞')
                    threadLock.release()
                else:
                    time.sleep(3)

class Customer(Thread):
    cuname=''
    cucount=0
    money=3000
    def run(self) ->None:
        global max
        while True:
            if max > 0:
                self.cucount += 1
                max -= 1
                self.money-=3
                threadLock.acquire()
                print(self.cuname, '已经购买了', self.cucount, '个蛋挞，收银器累计入账',self.cucount*3)
                threadLock.release()
                if self.money==0:
                    break
            else:
                time.sleep(2)

threadLock = threading.Lock()

m1=Make()
m2=Make()
m3=Make()
mc1=Customer()
mc2=Customer()
mc3=Customer()
mc4=Customer()
mc5=Customer()
mc6=Customer()

mc1.cuname='cus1'
mc2.cuname='cus2'
mc3.cuname='cus3'
mc4.cuname='cus4'
mc5.cuname='cus5'
mc6.cuname='cus6'
m1.coname='coo1'
m2.coname='coo2'
m3.coname='coo3'

m1.start()
m2.start()
m3.start()
mc1.start()
mc2.start()
mc3.start()
mc4.start()
mc5.start()
mc6.start()
