import cv2 as cv 
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/lena_color_512.tif', 0)

    plt.imshow(img) #display the image with matplotlib # type: ignore
    plt.show() # display the image 

    plt.imshow(img, cmap='gray') #display the image with matplotlib # type: ignore
    plt.title('Gray Image') # add title to the image
    plt.xticks([]) # remove x ticks
    plt.yticks([]) # remove y ticks
    #plt.axis('off') # turn off axis
    plt.show() # display the image 

if __name__ == '__main__':
    main()