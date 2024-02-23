import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

cv2.namedWindow("input", cv2.WINDOW_NORMAL)
# Loading the image 
img = cv2.imread('Downloads/audir8.jpg') #you can use any image you want.
imS = cv2.resize(img, (1280, 720))  
cv2.imshow("input",imS)
cv2.waitKey(0)

# Splitting the image in R,G,B arrays.
 
blue,green,red = cv2.split(img) 
#it will split the original image into Blue, Green and Red arrays.


#initialize PCA with first 20 principal components
pca = PCA(100)
 
#Applying to red channel and then applying inverse transform to transformed array.
red_transformed = pca.fit_transform(red)
red_inverted = pca.inverse_transform(red_transformed)
 
#Applying to Green channel and then applying inverse transform to transformed array.
green_transformed = pca.fit_transform(green)
green_inverted = pca.inverse_transform(green_transformed)
 
#Applying to Blue channel and then applying inverse transform to transformed array.
blue_transformed = pca.fit_transform(blue)
blue_inverted = pca.inverse_transform(blue_transformed)

img_compressed = (np.dstack((red_inverted, red_inverted, red_inverted))).astype(np.uint8)


#viewing the compressed image
cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
imr=cv2.resize(img_compressed,(1280, 720))
cv2.imshow("Output",imr)
cv2.waitKey(0)
