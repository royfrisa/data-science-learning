import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/lena_color_512.tif', 1)

    img = cv.cvtColor(img, cv.COLOR_BGR2RGB) #type: ignore

    plt.imshow(img)
    plt.show()

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()