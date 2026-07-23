import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 

def main():
    img = cv.imread('images/4.2.01.tif')
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB) #type:ignore

    row, col, channels = img.shape 

    # Affine Transformation 
    #point1 is the original points and point2 is the transformed points
    point1 = np.float32([[100,100],[300,100],[100,300]]) #type:ignore
    point2 = np.float32([[200,150],[400,150],[400,300]]) #type:ignore

    A = cv.getAffineTransform(point1,point2) #type:ignore
    print(A)

    # Perspetive Transform

    point3 = np.float32([[0,0],[300,0],[0,300],[300,300]]) #type:ignore
    point4 = np.float32([[0,0],[100,0],[300,100],[100,100]]) #type:ignore

    P = cv.getPerspectiveTransform(point3,point4) #type:ignore

    #output = cv.warpAffine(img, A, (col,row))
    output = cv.warpPerspective(img, P, (500,500))

    plt.imshow(output)
    plt.title('Affine Transform')
    plt.show()

if __name__ == '__main__':
    main()