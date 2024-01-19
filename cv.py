# import cv2
# import matplotlib.pyplot as plt 

# img = cv2.imread('cat.jpg')
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img = cv2.GaussianBlur(img, (11, 11), 0) 
# img = cv2.Canny(img, 30, 150, 3) 
# img = cv2.dilate(img, (1, 1), iterations=0) 


# (cnt, hierarchy) = cv2.findContours( 
#     dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
# cv2.drawContours(img, cnt, -1, (0, 255, 0), 2) 

# plt.imshow(img ,cmap='gray')
# plt.show()



import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
  
image = cv2.imread('coin2.jpg') 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
  
blur = cv2.GaussianBlur(gray, (11, 11), 0) 
canny = cv2.Canny(blur, 30, 150, 3) 
dilated = cv2.dilate(canny, (1, 1), iterations=0) 
  
(cnt, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
print("coins in the image : ", len(cnt))  
plt.imshow(rgb)
plt.show()  
  
