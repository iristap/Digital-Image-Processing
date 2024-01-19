import cv2
import matplotlib.pyplot as plt
img = cv2.imread("image/cat.jpg")
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_gray  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('img',img)
# cv2.waitKey(0)
plt.imshow(img_gray,'gray')
plt.show()
