# Credits to https://github.com/murtazahassan/Document-Scanner
#import picamera
import cv2
import numpy as np
import docScannerUtils
import time
import sys

def main():
    #cam = picamera.PiCamera()
    cam = cv2.VideoCapture(0)
    time.sleep(2.0)
    docScannerUtils.initializeTrackbars()
    count = 0
    while True:
        #img = cam.source_camera()
        cap, img = cam.read()
        if img is None:
            print("Failed to capture image from camera")

        imageArray = docScannerUtils.scanDocumentsInImage(img)

        lables = [["Original", "Gray", "Threshold", "Contours"],
                  ["Biggest Contour", "Warp Prespective", "Warp Gray", "Adaptive Threshold"]]

        # Display the image array
        stackedImage = docScannerUtils.stackImages(imageArray, 0.75, lables)
        cv2.imshow("Result", stackedImage)

        # Save image on 's' key is press
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite("brainypi-opencv-examples/document-scanner/Scanned/qmyImage"+str(count)+".jpg",stackedImage)
            #cv2.imwrite(filename='saved_img.jpg', img=img)
            cv2.rectangle(stackedImage, ((int(stackedImage.shape[1] / 2) - 230), int(stackedImage.shape[0] / 2) + 50),
                          (1100, 350), (0, 255, 0), cv2.FILLED)
            cv2.putText(stackedImage, "Scan Saved", (int(stackedImage.shape[1] / 2) - 200, int(stackedImage.shape[0] / 2)),
                        cv2.FONT_HERSHEY_DUPLEX, 3, (0, 0, 255), 5, cv2.LINE_AA)

            cv2.namedWindow("Result", cv2.WINDOW_NORMAL)
            cv2.resizeWindow("Result", 1280, 720)
            cv2.imshow('Result', stackedImage)
            cv2.waitKey(300)
            count += 1
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    sys.exit()
        #elif key == ord('q'):
        elif cv2.waitKey(1) & 0xFF == ord('q'):
            print("Turning off camera.")
            cam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
    cam.close()


if __name__ == "__main__":
    main()
