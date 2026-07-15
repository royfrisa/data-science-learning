import cv2 as cv
import matplotlib.pyplot as plt 

def Webcam_Image():
    cap = cv.VideoCapture(0, cv.CAP_AVFOUNDATION) #create a VideoCapture object to read from the webcam, 0 is the index of the webcam
    #cap_avfoundation is for macOS, for Windows use cv.CAP_DSHOW, for Linux use cv.CAP_V4L2

    ret, frame = cap.read() #read a frame from the webcam, ret is boolean indicating if the frame was read successfully, frame is the image

    if cap.isOpened(): #check if the webcam is opened successfully
        ret, frame = cap.read() 
        print(ret) #print the boolean value indicating if the frame was read successfully

        img = cv.cvtColor(frame, cv.COLOR_BGR2RGB) # convert BGR to RGB #type: ignore

        plt.imshow(img)
        plt.title('Webcam Image')
        plt.show()

        cap.release() #release the webcam

def Webcam_Video():
    cap = cv.VideoCapture(0)

    print("Width: " + str(cap.get(3))) #print the width
    print("Height: " + str(cap.get(4))) #print the height

    cap.set(3, 1024) # set width of the video frame, 3 is the property id for width, 1024 is the width in pixels
    cap.set(4, 720) # set height of the video frame, 4 is the property id for height, 720 is the height in pixels

    if cap.isOpened(): # if capture device is opened...
        ret, frame = cap.read() #read a frame from the webcam
    else: 
        ret = False #if not opened, set ret to False

    while(ret): #while ret is True, meaning the webcam is opened and a frame is read successfully
        ret, frame = cap.read()

        cv.imshow("Webcam Video", frame) #display the frame in a window named 'Webcam Video'

        key = cv.waitKey(1) #wait for 1 millisecond for a key event
        if key == (27):
            break

    cv.destroyAllWindows() 
    cap.release() #release the webcam

Webcam_Video()

