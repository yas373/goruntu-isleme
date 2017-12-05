import matplotlib.pyplot as plt
import numpy as np
 
a1 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\a1.jpg')
a2 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\a2.jpg')
a3 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\a3.jpg')
a4 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\a4.jpg')
a5 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\a5.jpg')
b1 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\b1.jpg')
b2 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\b2.jpg')
b3 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\b3.jpg')
b4 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\b4.jpg')
b5 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\b5.jpg')
c1 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\c1.jpg')
c2 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\c2.jpg')
c3 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\c3.jpg')
c4 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\c4.jpg')
c5 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\c5.jpg')
d1 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\d1.jpg')
d2 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\d2.jpg')
d3 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\d3.jpg')
d4 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\d4.jpg')
d5 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\d5.jpg')
e1 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\e1.jpg')
e2 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\e2.jpg')
e3 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\e3.jpg')
e4 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\e4.jpg')
e5 = plt.imread('C:\\Users\\Yasua\\Desktop\\JupyterExample\\veriler\\e5.jpg')
 
def siyah_beyaz(x):
    threshold=150
    for i in range(x.shape[0]): 
        for j in range(x.shape[1]): 
            n=x[i,j,0]/3+x[i,j,1]/3+x[i,j,2]/3
            if n>threshold:
                x[i,j]=0
            else:
                x[i,j]=255
 
def reshape(img):
    n = img.shape[0] * img.shape[1]
    img_r = img.reshape(1,n)
    return img_r
 
x_array=[]
for i in range(a1.shape[0]): #100
    for j in range(a1.shape[1]): #100
        x_array.append(a1[i,j,0])
print(x_array)
 
def findCenter(List_Of_Points):
    a=0, b=0, c=0 ,d=0, e=0
    for point in List_Of_Points:
        a=a+point[0]
        b=b+point[1]
        c=c+point[2]
        d=d+point[3]
        e=e+point[4]
    l=len(List_Of_Points)
    return [a/l,b/l,c/l,d/l,e/l]
 
sifir=0
bir=0
for i in range(a1.shape[0]): #100
    for j in range(a1.shape[1]): #100
        if(a1[i,j,0]>0):
            bir+=1
        else:
            sifir+=1
print(sifir,bir) #9287 713
 
siyah_beyaz(a1),siyah_beyaz(a2),siyah_beyaz(a3),siyah_beyaz(a4),siyah_beyaz(a5)
siyah_beyaz(b1),siyah_beyaz(b2),siyah_beyaz(b3),siyah_beyaz(b4),siyah_beyaz(b5)
siyah_beyaz(c1),siyah_beyaz(c2),siyah_beyaz(c3),siyah_beyaz(c4),siyah_beyaz(c5)
siyah_beyaz(d1),siyah_beyaz(d2),siyah_beyaz(d3),siyah_beyaz(d4),siyah_beyaz(d5)
siyah_beyaz(e1),siyah_beyaz(e2),siyah_beyaz(e3),siyah_beyaz(e4),siyah_beyaz(e5)
 
plt.subplot(1,5,1), plt.imshow(a1)
plt.subplot(1,5,2), plt.imshow(a2)
plt.subplot(1,5,3), plt.imshow(a3)
plt.subplot(1,5,4), plt.imshow(a4)
plt.subplot(1,5,5), plt.imshow(a5)
plt.show()
plt.subplot(1,5,1), plt.imshow(b1)
plt.subplot(1,5,2), plt.imshow(b2)
plt.subplot(1,5,3), plt.imshow(b3)
plt.subplot(1,5,4), plt.imshow(b4)
plt.subplot(1,5,5), plt.imshow(b5)
plt.show()
plt.subplot(1,5,1), plt.imshow(c1)
plt.subplot(1,5,2), plt.imshow(c2)
plt.subplot(1,5,3), plt.imshow(c3)
plt.subplot(1,5,4), plt.imshow(c4)
plt.subplot(1,5,5), plt.imshow(c5)
plt.show()
plt.subplot(1,5,1), plt.imshow(d1)
plt.subplot(1,5,2), plt.imshow(d2)
plt.subplot(1,5,3), plt.imshow(d3)
plt.subplot(1,5,4), plt.imshow(d4)
plt.subplot(1,5,5), plt.imshow(d5)
plt.show()
plt.subplot(1,5,1), plt.imshow(e1)
plt.subplot(1,5,2), plt.imshow(e2)
plt.subplot(1,5,3), plt.imshow(e3)
plt.subplot(1,5,4), plt.imshow(e4)
plt.subplot(1,5,5), plt.imshow(e5)
plt.show()