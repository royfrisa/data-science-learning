import cv2 as cv 
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/lena_color_512.tif')
    img2 = cv.imread('images/house.tif')

    lena = cv.cvtColor(img,cv.COLOR_RGB2BGR) #type:ignore
    house = cv.cvtColor(img2, cv.COLOR_BGR2RGB) #type:ignore

    output = lena + house 
    alpha = 0.7 # alpha and beta has to be conbined 10.0 no more no less
    beta = 0.3

    gamma = 0
    
    #. It calculates the weighted sum of two arrays (images) according to a mathematical formula, allowing you to control the transparency and translucency of each image.
    output2 = cv.addWeighted(lena,alpha,house,beta,gamma)

    # addWeighted() function is used to blend two images together by calculating the weighted sum of the pixel values of the two images. 
    # The function takes in the following parameters: 
    # alpha - the weight of the first image,
    # beta - the weight of the second image,
    # gamma - a scalar value added to the sum of the weighted pixel values, which can be used to adjust the brightness of the resulting image. 
    # The resulting image is a combination of the two input images, with the first image having a weight of alpha and the second image having


    #looping the images one by one 

    images = [lena,house,output,output2]
    titles = ['lena','house','lena+house','lena+house_weighted']

    for i in range(len(images)):
        plt.subplot(2,2,i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.yticks([])
        plt.xticks([])

    plt.show()

    cv.waitKey(0)

if __name__ == '__main__':
    main()