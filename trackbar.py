import cv2 as cv
import numpy as np 

def main():
    img = np.zeros((512,512,3), np.uint8)

    def Bfunc(x): #callback function for the Blue channel trackbar
        pass

    def Gfunc(x): #callback function for the Green channel trackbar
        pass

    def Rfunc(x): #callback function for the Red channel trackbar
        pass

    window = "OpenCV Color Plattee" #name of the window
    cv.namedWindow(window)

    cv.createTrackbar('B',window,0,255,Bfunc) #create a trackbar for Blue channel
    cv.createTrackbar('G',window,0,255,Gfunc) #create a trackbar for Green channel
    cv.createTrackbar('R',window,0,255,Rfunc) #create a trackbar for Red channel
    
    while True:
        cv.imshow(window, img) # type: ignore

        blue = cv.getTrackbarPos('B', window) #get the current position of the Blue trackbar
        green = cv.getTrackbarPos('G', window) #get the current position of
        red = cv.getTrackbarPos('R', window) #get the current position of the Red trackbar

        img[:] = [blue, green, red] #set the color of the image to the current values of the trackbars
        print(blue, green, red) #print the current values of the trackbars
        
        if cv.waitKey(1) == 27: #wait for the ESC key to exit
            break
    
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()