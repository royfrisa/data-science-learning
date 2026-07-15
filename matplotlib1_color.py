#RGB vs BGR
#COLOR SPACES = RGB, BGR, HSV, LAB, CMYK, CMY....
#opencv uses BGR, matplotlib uses RGB

import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/lena_color_512.tif', 1) 

    img = cv.cvtColor(img, cv.COLOR_BGR2RGB) # convert BGR to RGB #type: ignore

    plt.imshow(img)
    plt.title('Lena_Color')
    plt.xticks([]) # remove x ticks
    plt.yticks([]) # remove y ticks
    plt.show()
    

if __name__ == '__main__':
    main()
