import cv2
import numpy
import time
def toGrey(color, n):
    ConversionFactor = 255 / (n - 1)
    AverageValue = (int(color[0]) + int(color[1]) + int(color[2])) / 3
    Gray = int(((AverageValue / ConversionFactor) + 0.5) * ConversionFactor)
    color[0] = Gray
    color[1] = Gray
    color[2] = Gray
    return color
def main():
    cap = cv2.VideoCapture(0)
    lastFrame = None
    RED = [0,0,0]

    #LOOP fram capture, each time capture 1 frame.
    while 1:
        #giving some air to the CPU
        time.sleep(0.05)

        #This check if last frame (which is the one i compare other frames to) is initialized or not. Accurres on the first time the script run.
        if lastFrame is None:
            # ret bool... lastframe- matrix cointaining arrays of size of 3 for example on the place lastFrame[i][j] there is a array of 3 values (RGB)
            # example [255,255,255]
            ret, lastFrame = cap.read() # capture 1 frame.
            #Resize it so the matrix will not be huge. make the code faster.
            
            pass

        ret, frame = cap.read() #capture 1 frames
        #same as before...
        

        #initializing a matrix that will contain the difference between two frames (later will be the difference bbetween average frames and new frame.)
        diff = numpy.zeros([len(frame),len(frame[0]),3],dtype=numpy.uint8)

        #Main nested loop run through all points on the matrix.
        i = 0
        j = 0
        while i<len(frame):
            j = 0
            while j<len(frame[0]):
                #toGrey is a function that i buid. It converts an RGB array to a grey scale with n amounts of colors available. For example on the
                #Following there are only 4 shades of grey in the picture.
                lastFrame[i][j] = toGrey(lastFrame[i][j],4)
                frame[i][j] = toGrey(frame[i][j],4)


                #compare between the current frame and the last one.
                val = abs(int(frame[i][j][0])-int(lastFrame[i][j][0]))

                #Set the diff matrix. the change will be seen on this matrix.
                diff[i][j] = [val,val,val]

                #Check in a specific place if there is a change. If there is a change, color it!
                if(diff[i][j][0]!=0 and diff[i][j][1]!=0 and diff[i][j][2]!=0):
                    diff[i][j] = (255,0,0)

                #print(diff[i][j])
                j+=1
                #print(j)
            i+=1
        lastFrame = frame


        # Display the resulting frame
        cv2.imshow('Final Report Difference motion detect by webcam ',diff)

        #display windows
        cv2.resizeWindow('Final Report Difference motion detect by webcam', 600,600)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # runs on start
if __name__ == '__main__':
    main()
