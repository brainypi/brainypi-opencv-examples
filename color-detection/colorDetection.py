# Credits to https://github.com/murtazahassan/Document-Scanner
#import picamera
import cv2
import numpy as np
import colorDetectUtils
import time
import sys

def main():
    #cam = picamera.PiCamera()
    webcam = cv2.VideoCapture(0)
    time.sleep(2.0)
    print("Press q to quit")
    while True:
        #img = cam.source_camera()
        cap, img = webcam.read()
        if img is None:
            print("Failed to capture image from camera")

        colorLowerLimit = np.array([136, 187, 111], np.uint8)
        colorUpperLimit = np.array([180, 255, 255], np.uint8)

        colorMask = colorDetectUtils.createColorMask(img, colorLowerLimit, colorUpperLimit)

        colorInfo, outputImg = colorDetectUtils.detectColors(img, colorMask, "Blue color")
        cv2.imshow("Result", outputImg)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()
