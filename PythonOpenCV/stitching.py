from imutils import paths
import numpy as np
import imutils
import cv2

print("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images("D:/Notebooks/UF1/Stitch")))
images = []

for imagePath in imagePaths:
    image = cv2.imread(imagePath)
    images.append(image)

print("[INFO] stitching images...")
cv2.imshow
stitcher = cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

if status == 0:
    cv2.imwrite("output.png", stitched)
    
    cv2.imshow("stitched", stitched)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("[INFO] image stitching failed ({})".format(status))                         