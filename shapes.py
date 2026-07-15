import cv2 as cv 

def main():
    img = cv.imread('images/lena_color_512.tif',1)
    img2 = cv.imread('images/lena_color_512.tif',0)

    print(type(img)) #type of the image (numpy.ndarray) 
    print(img.dtype) #data type of the image (uint8, float32, etc.) # type: ignore 

    print(img.shape) #shape of the image (rows, columns, channels) # type: ignore 
    print(img2.shape) #shape of the image (rows, columns) no channels # type: ignore 

    print(img2.ndim) #number of dimensions of the image (2 for grayscale, 3 for color) # type: ignore 
    print(img.ndim) #number of dimensions of the image (2 for grayscale, 3 for color) # type: ignore 

    print(img.size) #total number of pixels in the image (rows * columns * channels) # type: ignore 
    print(img2.size) #total number of pixels in the image (rows * columns * channels) # type: ignore 

if __name__== '__main__':
    main()