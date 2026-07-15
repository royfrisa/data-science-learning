import cv2 as cv 
import matplotlib.pyplot as plt 

def Video_Write():
    cap = cv.VideoCapture(0, cv.CAP_AVFOUNDATION) #create a VideoCapture object to read from the webcam, 0 is the index of the webcam
    window_name = 'Live Video'
    cv.namedWindow(window_name)

    file_name = 'output.avi' # specify the output file name
    codec = cv.VideoWriter_fourcc('X', 'V', 'I', 'D') # specify the video codec #type: ignore
    fps = 30.0
    resolution = (1920, 1080) # specify the resolution of the video
    Video_output = cv.VideoWriter(file_name, codec, fps, resolution)

    if cap.isOpened():
        ret, frame = cap.read()  # read a frame from the video capture
        print(ret)
    else:
        ret = False 

    while(ret):
        ret, frame = cap.read() # read a frame from the video capture
        
        Video_output.write(frame) # write the frame to the output video file

        cv.imshow(window_name, frame) # display the frame in a window named 'Live Video'
        print(frame.shape)
        print(frame.dtype)

        if cv.waitKey(1) == (27):
            break 

    cv.destroyAllWindows()
    Video_output.release() #release the video writer object
    cap.release()
    
Video_Write()

    
