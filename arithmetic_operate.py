import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/lena_color_512.tif')
    img2 = cv.imread('images/house.tif')

    img = cv.cvtColor(img,cv.COLOR_BGR2RGB) #type: ignore
    img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB) #type: ignore

    #Operations can be done like + or - to the images 
    add_img = img + img2
    sub_img = img - img2
    sub2_img = img2 - img
    mul_img = img * img2 
    lena50_img = img + 50
    lena_sub_50_img = img - 50
    fifty_sub_lena_img = 50 - img
    divi_img = img/img2 

    img3 = img * 1.5
    img4 = img2/1.5   

    images = [img,img2,add_img,sub_img,
              sub2_img,mul_img,lena50_img,
              lena_sub_50_img,fifty_sub_lena_img,divi_img,img3,img4]
    
    titles = ['Lena','House','Lena+House','Lena-House',
              'House-Lena','Lena*House','Lena+50',
              'Lena-50','50-Lena',
              'Lena/House','Lena*1.5','House/1.5']
    
    for i in range(len(images)):
        plt.subplot(2,6,i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()

    cv.waitKey(0)

if __name__ == '__main__':
    main()