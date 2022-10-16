import cv2


img_0=cv2.imread("C:\\Users\\bugra\\Desktop\\deneme\\inonu.png")
cv2.imshow("resim",img_0)
cv2.waitKey(0)

B = img_0[:,:,0]
G = img_0[:,:,1]
R = img_0[:,:,2]


from matplotlib import pyplot as plt
import matplotlib.image as mpimg
imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
plt.imshow(imgGray, cmap='gray')
plt.show()

img_yuv=cv2.cvtColor(img_0,cv2.COLOR_BGR2YUV)
y,u,v=cv2.split(img_yuv)

cv2.imshow('y',y)
cv2.imshow('u',u)
cv2.imshow('v',v)
cv2.imshow("inonu.png",img_yuv)
cv2.waitKey(0)

#Hocam kullanmış olduğum resim png uzantılı üniversitemizin logosudur.Görsellerde inönü logo yazıldığında çıkan ilk resimdir.



