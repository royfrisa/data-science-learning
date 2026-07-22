import cv2 as cv 
import matplotlib.pyplot as plt 

def main():
    img = cv.imread('images/lena_color_512.tif',1)
    img1 = cv.cvtColor(img,cv.COLOR_BGR2RGB) #type:ignore
    img2 = cv.cvtColor(img,cv.COLOR_BGR2GRAY) #type:ignore

    img3 = 255-img1
    img4 = 255-img2

    images = [img1, img2, img3, img3]
    titles = ['lena', 'lena-gray', 'lena-negative', 'lena-gray-negative']

    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.imshow(images[i],cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()

    cv.waitKey()

if __name__ == '__main__':
    main()