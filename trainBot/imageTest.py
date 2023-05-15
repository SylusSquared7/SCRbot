import cv2
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = "image.png"

image = cv2.imread('image.png', 0)
thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

data = pytesseract.image_to_string(thresh, lang='eng',config='--psm 6')
print(data)

cv2.imshow('thresh', thresh)
cv2.waitKey()
