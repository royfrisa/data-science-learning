import cv2 as cv 

def Play_Video():
    window_name = 'Video Player'
    cv.namedWindow(window_name)
    
    cap = cv.VideoCapture('output.avi') # create a VideoCapture object to read from the video file

    while cap.isOpened():
        ret, frame = cap.read() #read a frame from the video file, ret is boolean indicating if the frame was read successfully, frame is the image

        if (ret):
            cv.imshow(window_name, frame) # display the frame in the windows
            if cv.waitKey(30) == 27: 
                break 
        else:
            break 

        # When you run, you will see the video is really fast.
        # Because the video is with frame rate of 30.0 fps. 
        # And the waitKey(1) is only 1 millisecond.
        # So, you can change the waitKey(1) to waitKey(33)
        # Because 1 second = 1000 milliseconds, and 1000/30 = 33.33 milliseconds per frame.
        # So, waitKey(33) will wait for 33 milliseconds for a key event, which is approximately the time for one frame at 30 fps
        # if slowmotion, change the waitKey(33) to waitKey(100) or waitKey(200) or waitKey(500) or waitKey(1000)
    
    cv.destroyAllWindows()
    cap.release()
        




Play_Video()