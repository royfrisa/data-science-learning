import cv2 as cv 
import numpy as np 

def main():
    #drawing a black image of size 512x512 with 3 channels (RGB)
    img = np.zeros((512,512,3), np.uint8)

    cv.line(img, (0,0), (100,400), (255,0,0), 10) #draw a blue line from (0,0) to (100,200) with thickness of 5
    cv.rectangle(img, (40,60), (200,400), (0,255,0), 5) #draw a green rectangle from (40,60) to (200,400) with thickness of 5
    cv.circle(img, (200,200), 30, (0,0,255), -1) #draw a red circle at (200,200) with radius 30 and filled
    cv.ellipse(img, (300,300), (100,50), 0,0, 360, (250,0,25), 1) #draw a filled ellipse at (300,300) with axes lengths of 100 and 50, rotated by 0 degrees, starting from 0 to 360 degrees

    points = np.array([[67,200], [72,89], [200,90]]) #define the points for the polygon
    print(points) #print the points of the polygon

    cv.polylines(img, [points], True, (0,255,0), 1) #draw a green polygon with the given points and thickness of 3

    text = 'Hello Thar Htet Aung'

    cv.putText(img, text, (10,500), cv.FONT_HERSHEY_SIMPLEX, 1.2, (255,255,0), 2) #draw the text on the image at (10,500) with font size of 1.2 and color of yellow

    cv.imshow('Black Image', img) # type: ignore
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
