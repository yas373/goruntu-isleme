# -*- coding: utf-8 -*-
import math 
#def findDistance(x,y):
#    return math.sqrt(
#            (x[0]-y[0])**2 + (x[1]-y[1])**2)
#d=findDistance([3,0],[0,4])
#print (d)
#
#from scipy import ndimage
#from scipy import misc
#f=misc.face()
import matplotlib.pyplot as plt
#plt.imshow(f)
#plt.show()
#
#print (f.ndim)
#
#print (f.shape)
#
#print (type(f))
#
#im_size=f.shape
#
#center=[im_size[0]/2-50 , im_size[1]/2+70]
#
##f[:,:,2]=0
##plt.imshow(f)
##plt.show()
#
#for i in range (im_size[0]):
#    for j in range (im_size[1]):
#        if(findDistance([i,j], center)>350 and findDistance([i,j], center)<360 ):
#            f[i,j,:]=0
#            
#plt.imshow(f)
#plt.show()
import matplotlib.image as mpimg
import numpy as np
def createList(size):
    myList=[]
    for i in range (size):
        myList.append(i)
    return myList
def listIncrement(l,n):
    myL=[]
    for i in range(len(l)):
        myL.append(l[i]+n)
    return l
L_1=createList(5)
print (L_1)
L_2=listIncrement(L_1,5)
print (L_2)

img=mpimg.imread(r'C:\Users\Yasin\Desktop\2013-12-14 07-54-54.JPG')
print (img.ndim)
print (img.shape)
plt.imshow(img)
plt.show()
img[:,100,:].max()
img_1=img[1:375:2,:,:]
img_1=img[:,1:500:2,:]
plt.imshow(img_1)
plt.show()
img_20=np.zeros((2448,3264,3))
img_20.shape
for i in range(3264):
    for j in range(2448):
        img_20[j,i,:]=img[i,j,:]
img_30=np.zeros((2448,3264,3))
img_30.shape
for i in range(3264):
    for j in range (2448):
        img_30[j,i,:]=1-img[i,j,:]
        
img_40=np.zeros((3264,2448,3))
img_40.shape

for i in range (3264):
    for j in range(2448):
        img_40[3264-i-1,2448-j-1, : ]=img[i,j,:]
plt.subplot(1,4,1) , plt.imshow(img)
plt.subplot(1,4,2), plt.imshow(img_20)
plt.subplot(1,4,3), plt.imshow(img_30)
plt.subplot(1,4,4), plt.imshow(img_40)
plt.show()

















