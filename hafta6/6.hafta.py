import numpy as np
import matplotlib.pyplot as plt
 
my_Numbers=np.random.randint(1,10,5)
my_Numbers #array([1, 4, 2, 3, 7])
 
myHistogram=[]
myHistogram #[]
 
for number in my_Numbers:
    for histItem in myHistogram:
         
        if(number==histItem[0]):
            histItem[1]=histItem[1]+1
        else:
            myHistogram.append(number,1)
 
myHistogram #[]
 
var_1=(1,2,3)
var_2=(2,5,3)
var_3=(1,5,3)
var_4=(2,5,6)
 
if var_1[2]==var_2[2]:
    print("1 ve 2'nin 3.deðeri eþittir.")
else:
    print("1 ve 2'nin 3.deðeri eþit deðildir.")
 
if var_1==var_2:
    print("1 ve 2 eþittir.")
else:
    print("1 ve 2 eþit deðildir.")
	
	
	import numpy as np
import matplotlib.pyplot as plt
start=0
end=2
n=5
my_Numbers=np.random.randint(start,end,n)
img=plt.imread("")
myHistogram={}
my_Numbers #array([0, 1, 0, 1, 0])
 
for number in my_Numbers:
        if number in myHistogram.keys():
            myHistogram[number]=myHistogram[number]+1
        else:
            myHistogram[number]=1
 
my_Numbers, myHistogram, myHistogram[0]/myHistogram[1] 
#histogram da iki deðer olmalý
#(array([0, 1, 0, 1, 0]), {0: 3, 1: 2}, 1.5)values


import matplotlib.pyplot as plt
import numpy as np
 
def convert_RGB_to_monochrome_BW(image_1):
    threshold=100
    img_1=plt.imread(image_1)
    img_2=np.zeros((img_1.shape[0],img_1.shape[1]))
    for i in range(img_2.shape[0]):
        for j in range(img_2.shape[1]):
            if (img_1[i,j,0]/3+img_1[i,j,1]/3+img_1[i,j,2]/3)>threshold:
                # img_2[i,j]=img_1[i,j,0]/3+img_1[i,j,1]/3+img_1[i,j,2]/3
                img_2[i,j]=1
            else:
                img_2[i,j]=0
    # print(img_1.shape)
    return img_2
 
img_1 = convert_RGB_to_monochrome_BW(r"test_t_one.jpg")
plt.imshow(img_1, cmap="gray")
plt.show()