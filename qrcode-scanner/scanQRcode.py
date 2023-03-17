import cv2
import picamera
import scanQRcodeUtils
import time 


def main():
    cam = picamera.PiCamera()
    cam.resolution = (640, 480)
    time.sleep(2.0)

    while True:
        img = cam.source_camera()
        if img is None:
            print("Failed to capture image from camera")
            break
            
        qrDataList, img = scanQRcodeUtils.scanQRCodes(img)
    
        print(qrDataList)
        cv2.imshow("Output", img)
        cv2.waitKey(1)

    # do a bit of cleanup
    cv2.destroyAllWindows()
    cam.close()

if __name__ == "__main__":
    main()
