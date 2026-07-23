import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/4.2.01.tif')
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB) #type:ignore

    row, col, channels = img.shape 

    Rotation = cv.getRotationMatrix2D((col/2,row/2), 90, 1) #type:ignore
    print(Rotation)

    output = cv.warpAffine(img,Rotation,(col,row))

    plt.imshow(output)
    plt.title('Rotation')
    plt.show()

if __name__ == '__main__':
    main()
