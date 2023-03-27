import cv2
#import picamera
import time

threshold = 0.45  # Threshold to detect object

classNames = []
classFile = "./coco.names"
with open(classFile, "rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = "./ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "./frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


def detectObjects(img, thres, nms, draw=True, objects=[]):
    """Detect objects in image

    Args:
        img ([cv2.Mat]): Input Image
        thres ([int]): Object detection threshold
        nms ([type]): [description]
        draw (bool, optional): Draw binding boxes. Defaults to True.
        objects (list, optional): List of objects to filter, i.e will only detect these objects. Defaults to [].

    Returns:
        img [cv2.Mat]: Output image
        objectInfo [list]: Object information
    """
    classIds, confs, bbox = net.detect(
        img, confThreshold=thres, nmsThreshold=nms)
    # print(classIds,bbox)
    if len(objects) == 0:
        objects = classNames
    objectInfo = []
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box, className])
                if (draw):
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, classNames[classId-1].upper(), (box[0]+10, box[1]+30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(img, str(round(confidence*100, 2)), (box[0]+200, box[1]+30),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    return img, objectInfo


def main():
    #cam = picamera.PiCamera()
    cam = cv2.VideoCapture(0)
    #cam.resolution = (1280, 720)
    time.sleep(2.0)

    while True:
        #img = cam.source_camera()
        cap, img = cam.read()
        if img is None:
            print("Failed to capture image from camera")
            break
            
        result, objectInfo = detectObjects(img, threshold, 0.2)
        cv2.imshow("Output", img)
        cv2.waitKey(1)

    # do a bit of cleanup
    cv2.destroyAllWindows()
    #cam.close()

if __name__ == "__main__":
    main()
