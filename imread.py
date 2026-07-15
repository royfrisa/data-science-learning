import cv2 as cv

#read the image, 0 for grayscale, 1 for colorm -1 for unchaged 
img = cv.imread('images/lena_color_512.tif', 1)

# Check if the image was loaded successfully
if (img is None):
    raise FileNotFoundError("Image not found.")

#show the image in a window 
cv.imshow('Lena_color', img)

cv.waitKey(0) #wait for a key press to close the window
cv.destroyAllWindows()