import random
dizi=[]
sayac=1
def uret():
    a=random.randint(1,100)
    for i in range(a):
        b=random.randint(1,100)
        dizi.append(b)
def bul():
    global sayac
    for t in range(len(dizi)):
        sayac=1
        for y in range(t,len(dizi)-1):
            if (dizi[t]==(dizi[y+1]) and (dizi[t]!=-1 or dizi[y+1]!=-1) ):
                sayac=sayac+1
                dizi[y+1]=-1
        if (dizi[t]!= -1):
            print (dizi[t],":",sayac)              
uret()
print (dizi)
bul()
