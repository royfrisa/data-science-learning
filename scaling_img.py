import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/lena_color_512.tif')

    #resizing (scaling), fx and fy are coordinates of x and y. #scale up and scale down.
    linear = cv.resize(img,None,fx=1.0,fy=0,interpolation=cv.INTER_LINEAR) #type:ignore
    cubic = cv.resize(img,None,fx=1.0,fy=0,interpolation=cv.INTER_CUBIC) #type:ignore
    area = cv.resize(img,None,fx=1.0,fy=0,interpolation=cv.INTER_AREA) #type:ignore
    nearest = cv.resize(img,None,fx=1.0,fy=0,interpolation=cv.INTER_NEAREST) #type:ignore

    #shifting 
    img2 = cv.cvtColor(img,cv.COLOR_BGR2RGB) #type:ignore
    row,col,channels = img.shape #type:ignore

    #up 50 is to shift x, down 50 is to shift y. 

    T = np.float32([[1,0,50],[0,1,50]]) #type:ignore
    print(T)

    output = cv.warpAffine(img,T,(col,row)) #type:ignore

    plt.imshow(output)
    plt.title('shifting')
    plt.show()

    cv.imshow('Linear',linear)
    cv.imshow('cubic',cubic)
    cv.imshow('area',area)
    cv.imshow('nearest',nearest)

    if cv.waitKey(0) == 27:
        cv.destroyAllWindows()

if __name__ == "__main__":
    main()