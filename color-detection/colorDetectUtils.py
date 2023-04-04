import numpy as np
import cv2

def createColorMask(inputImage, colorLower, colorUpper):
    """Create color mask from given inputs

    Args:
        inputImage ([opencv Mat]): Input image
        colorLower ([opencv Mat]): Lower range of the color
        colorUpper ([opencv Mat]): Upper range of the color
    Returns:
        color_mask []: Contains the color mask
    """
    # Convert the imageFrame in
    # BGR(RGB color space) to
    # HSV(hue-saturation-value)
    # color space
    hsv_frame = cv2.cvtColor(inputImage, cv2.COLOR_BGR2HSV)
    # define mask
    color_mask = cv2.inRange(hsv_frame, colorLower, colorUpper)
    kernel = np.ones((5, 5), "uint8")
    color_mask = cv2.dilate(color_mask, kernel)

    return color_mask

def detectColors(inputImage, colorMask, name):
    """Detect color in image

    Args:
        inputImage ([opencv Mat]): Input image
        colorMask ([opencv Mat]): Color Mask generated from createColorMask()
        name ([opencv Mat]): Name of the color
    Returns:
        colorInfo [list]: list of colors detected in the image with bounding box info
        outputImage []: Output Image

    """
    colorInfo = []
    # Morphological Transform, Dilation
    # for each color and bitwise_and operator
    # between imageFrame and mask determines
    # to detect only that particular color
    cv2.bitwise_and(inputImage, inputImage, mask = colorMask)

    # Creating contour to track color
    contours, hierarchy = cv2.findContours(colorMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            boundingBox = {"x": x, "y": y, "w": w, "h": h}
            colorInfo.append(boundingBox)
            inputImage = cv2.rectangle(inputImage, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(inputImage, name, (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))

    return colorInfo, inputImage
