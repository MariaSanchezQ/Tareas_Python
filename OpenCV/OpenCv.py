import cv2
import numpy as np


img = cv2.imread("gatitos.jpg")
imgr = img
img = cv2.resize(img,(300,200))
imgr = cv2.resize(img,(300,200))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5), np.uint8)
imgCanny = cv2.Canny(img, 100, 80)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
import cv2
import numpy as np 
cv2.rectangle(imgr,(130,230),(30,60),(230,186,31),cv2.FILLED) 



cv2.imshow("Imagen Normal", img) #Imagen Normal
cv2.imshow("Imagen con rectangulo",imgr)#Imagen Dibujo rectangulo tapando primer gato
cv2.imshow("Imagen en escala de grises", imgGray) #Imagen en Escala de Grises
cv2.imshow("Bordes de la imagen ", imgCanny) #Imagen con bordes
cv2.imshow("Bordes gruesos de la imagen ", imgDialation) # Imagen con bordes gruesos
cv2.imshow("Bordes delgados de la imagen ", imgEroded)#Imagen con bordes delgados
cv2.waitKey(0)
