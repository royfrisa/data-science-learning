import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/lena_color_512.tif')
    img2 = cv.imread('images/lake.tif')

    img = cv.cvtColor(img,cv.COLOR_BGR2RGB) #type:ignore
    img2 = cv.cvtColor(img2,cv.COLOR_RGB2BGR) #type:ignore

    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.title('Lena')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1,2,2)
    plt.imshow(img2)
    plt.title('Lake')
    plt.xticks([])
    plt.yticks([])

    plt.show()

if __name__ == '__main__':
    main()