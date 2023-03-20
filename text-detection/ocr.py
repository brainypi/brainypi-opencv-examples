import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time
#import picamera
import ocrUtils


def main():
    #cam = picamera.PiCamera()
    cam = cv2.VideoCapture(0)
    #cam.resolution = (640, 480)
    time.sleep(2.0)

    while True:
        #img = cam.source_camera()
        cap, img = cam.read()
        if img is None:
            print("Failed to capture image from camera")
            break

        text, img = ocrUtils.readCharacters(img)

        print(text)
        cv2.imshow("Output", img)
        cv2.waitKey(1)

    # do a bit of cleanup
    #cv2.destroyAllWindows()
    #cam.close()


if __name__ == "__main__":
    main()
