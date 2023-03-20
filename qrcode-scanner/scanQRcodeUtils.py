import cv2
#import picamera
import numpy as np
from pyzbar.pyzbar import decode, ZBarSymbol

def scanQRCodes(img, draw=False):
    """Scan QR code 

    Args:
        img ([cv2.Mat]): Input Image
        draw (bool, optional): Should we draw qrcode data in the image. Defaults to False.

    Returns:
        qrDataList [list]: QR Codes decoded
        img [cv2.Mat]: image with QR code marked
    """
    qrDataList = []
    for barcode in decode(img, symbols=[ZBarSymbol.QRCODE]):
        qrData = barcode.data.decode('utf-8')
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)
        pts2 = barcode.rect
        if draw:
            cv2.putText(img, qrData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (255, 0, 255), 2)
        qrDataList.append(qrData)
        
    return qrDataList, img
