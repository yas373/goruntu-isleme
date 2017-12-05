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
 
def define_mask():
    mask = [[1,1,1],[1,1,1],[1,1,1]]
    mask, mask[1][2], mask[0][0], mask[2][2] #mask[3][1] error
     
    for i in range(3):
        for j in range(3):
            print(mask[i][j], end=" ")
        print()    
    return mask
 
def my_dilation(img, mask):
    m=img.shape[0] #100
    n=img.shape[1] #100
    img_2 = np.random.randint(0,1,(m,n))
    for i in range(1,m-1):
        for j in range(1,n-1):
            print(i,j,img_1[i][j])
            #apply_mask_1 for dilation
            x_1 = img_1[i,j] and mask[1][1]
 
            x_2 = img_1[i-1,j-1] and mask[0][0]
            x_3 = img_1[i-1,j] and mask[0][1]
            x_4 = img_1[i-1,j+1] and mask[0][2]
 
            x_5 = img_1[i+1,j+1] and mask[2][0]
            x_6 = img_1[i+1,j] and mask[2][1]
            x_7 = img_1[i+1,j+1] and mask[2][2]
 
            x_8 = img_1[i,j-1] and mask[1][0]
            x_9 = img_1[i,j+1] and mask[1][2]
 
            result_1 = x_1 or x_2 or x_3 or x_4 or x_5
            result_2 = x_6 or x_7 or x_8 or x_9
 
            result = result_1 or result_2
 
            img_2[i,j]=result
    return img_2
 
img_1 = convert_RGB_to_monochrome_BW(r"test_t_one.jpg")
plt.imshow(img_1, cmap="gray")
plt.show()
 
img_1.ndim #2
 
image_dilated = my_dilation(img_1, mask)
image_dilated
 
plt.subplot(1,2,1), plt.imshow(img_1, cmap="gray")
plt.subplot(1,2,2), plt.imshow(image_dilated, cmap="gray")
plt.show()