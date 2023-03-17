#! /usr/bin/python

# import the necessary packages
import picamera
import face_recognition
import imutils
import pickle
import time
import cv2
import faceRecUtils

def main():
    #Initialize 'currentname' to trigger only when a new person is identified.
    currentname = "unknown"
    #Determine faces from encodings.pickle file model created from registerFace.py
    encodingsP = "encodings.pickle"

    # load the known faces and embeddings along with OpenCV's Haar
    # cascade for face detection
    print("[INFO] loading encodings + face detector...")
    data = pickle.loads(open(encodingsP, "rb").read())
    cam = picamera.PiCamera()
    time.sleep(2.0)
    count=0
    while True:
        frame = cam.source_camera()
        if frame is None:
            print("Failed to capture image from camera")
            
        names, frame = faceRecUtils.recogniseFace(frame)
        
        # display the image to our screen
        cv2.imshow("Facial Recognition result", frame)
        key = cv2.waitKey(1) & 0xFF

        # quit when 'q' key is pressed
        if key == ord("q"):
            break

    # do a bit of cleanup
    cv2.destroyAllWindows()
    cam.close()

if __name__ == "__main__":
    main()
