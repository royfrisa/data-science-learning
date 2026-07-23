import cv2 as cv
import matplotlib.pyplot as plt 

def main():
    img = cv.imread('images/lena_color_512.tif')
    img2 = cv.imread('images/4.2.01.tif')

    img = cv.cvtColor(img, cv.COLOR_BGR2RGB) #type:ignore
    img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB) #type:ignore

    #logical operations 
    # and, or, not, xor

    # operations and, or, xor the 0 and 1 in images 
    # and (1 and 1 = 1) or (1+0=1,0+0=0,1+1=1) xor (1+0=1,1+1=0)
    
    #changes binary bit of pixel (white turns black)
    img3 = cv.bitwise_not(img)

    #check both images and keep pixel value if both are non-zero (greater than 0)
    img4 = cv.bitwise_and(img,img2)

    #check both images and keep pixel if either of pixels us non-zero
    img5 = cv.bitwise_or(img, img2)

    #keep pixel if only one of images is non-zero, but drop it if both are non-zero or if both are zero
    img6 = cv.bitwise_xor(img, img2)

    images = [img, img2, img3, img4, img5, img6]
    titles = ['lena','img2','NOT','AND','OR','XOR']

    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()
    

    
if __name__ == '__main__':
    main()