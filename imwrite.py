import cv2 as cv

#read the image, 0 for grayscale, 1 for color, -1 for unchaged 
img = cv.imread('images/lena_color_512.tif', 1)
img2 = cv.imread('images/lena_color_512.tif', -1)
img3 = cv.imread('images/lena_color_512.tif', 0)

# Check if the image was loaded successfully
if (img is None) or (img2 is None) or (img3 is None):
    raise FileNotFoundError("Image not found.")

#show the image in a window 
cv.imshow('Lena_color', img)
cv.imshow('Lena_unchanged', img2)
cv.imshow('Lena_grayscale', img3)

#saving the file (imwrite)
cv.imwrite('black_and_white.jpg', img3)


cv.waitKey(0) #wait for a key press to close the window
cv.destroyAllWindows()