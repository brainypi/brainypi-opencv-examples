import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time
import picamera

def readCharacters(img, draw=False):
    """Read characters from image

    Args:
        img ([cv2.Mat]): Input Image
        draw (bool, optional): Should we draw characters in the image. Defaults to False.

    Returns:
        [type]: [description]
    """
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
    hImg, wImg, _ = img.shape
    text = pytesseract.image_to_string(img)
    boxes = pytesseract.image_to_boxes(img)
    for b in boxes.splitlines():
        b = b.split(' ')
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 2)
        if draw:
            cv2.putText(img, b[0], (x, hImg - y+25),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

    return text, img
