import cv2 as cv 
import matplotlib.pyplot as plt 

def main():
    video = cv.VideoCapture(0, cv.CAP_AVFOUNDATION)

    file_name = "sample.MP4"
    video_codec = cv.VideoWriter_fourcc(*'mp4v') #type: ignore
    framerate = 30.0
    resolution = (1920, 1080)
    Video_output = cv.VideoWriter(file_name,video_codec,framerate,resolution)
    
    if video.isOpened():
        ret, frame = video.read()
    else:
        ret = False

    while True: 
        ret, frame = video.read()

        Video_output.write(frame)

        cv.imshow("MP4 Sample", frame)

        if cv.waitKey(1) == (27):
            break

    cv.destroyAllWindows()
    Video_output.release() 
    video.release()

if __name__ == '__main__':
    main()