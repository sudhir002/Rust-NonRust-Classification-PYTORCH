import cv2, os
from PIL import Image

fol = "Data/train/rust/"
c = 1
for x in os.listdir("Data/train/rust"):
    img = cv2.imread(fol + x)
    cv2.imwrite("Data/test/rust/" + str(c) + ".jpg", img)
    c = c+1