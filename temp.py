# -*- coding: utf-8 -*-
import math 
def findDistance(x,y):
    return math.sqrt(
            (x[0]-y[0])**2 + (x[1]-y[1])**2)
d=findDistance([3,0],[0,4])
print (d)

from scipy import ndimage
from scipy import misc
f=misc.face()
import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()

print (f.ndim)

print (f.shape)

print (type(f))

im_size=f.shape

center=[im_size[0]/2-50 , im_size[1]/2+70]

#f[:,:,2]=0
#plt.imshow(f)
#plt.show()

for i in range (im_size[0]):
    for j in range (im_size[1]):
        if(findDistance([i,j], center)>350 and findDistance([i,j], center)<360 ):
            f[i,j,:]=0
            
plt.imshow(f)
plt.show()