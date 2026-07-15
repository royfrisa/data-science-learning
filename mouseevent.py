import cv2 as cv 
import numpy as np

#for getting the information about events in cv
'''events = [i for i in dir(cv)] #shows all events in cv module.
events = [i for i in dir(cv) if 'EVENT' in i] #only gets the events if "EVENT" in it. 
print(events)'''

window='Drawing'
cv.namedWindow(window)
img = np.zeros((512,512,3),np.uint8) #created the black frame(image)

def draw_circle(mouse_event, start_x, start_y, flags, param): #mouse_event is event that trigger by mouse, x and y are start positions
    #draw a circle if mouse left button click 
    if mouse_event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(start_x,start_y), 30, (0,255,0), 1)
    
    #draw a circle if you click the middle button down
    elif mouse_event == cv.EVENT_MBUTTONDOWN:
        cv.circle(img,(start_x,start_y), 50, (255,0,0), -1)

cv.setMouseCallback(window, draw_circle) #links the mouse events to specific window

def main():
    while True:
        cv.imshow(window,img)
        if cv.waitKey(1) == 27: #break if 27=escape key is clicked
            break
    
        cv.destroyAllWindows

if __name__ == '__main__':
    main()