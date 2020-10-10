import cv2


img_location = 'C:/Users/Mohammed Yaseen/Desktop/python/'
filename = 'Nabil.jpg'

###



img = cv2.imread(img_location+filename)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted_gray_image = 255 - gray_image

blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21), 0)

inverted_blurred_img = 255 - blurred_img

pencil_sketch_TMG = cv2.divide(gray_image, inverted_blurred_img, scale=210.0)

##cv2.imshow('1st image', img)
ims = cv2.resize(img, (500, 500))
cv2.imshow("1st", ims)
##cv2.imshow('2nd Image', gray_image)
##cv2.imshow('3rd Image',inverted_gray_image)
##cv2.imshow('4th Image',blurred_img)
##cv2.imshow('4th Image',inverted_blurred_img)
##ims = cv2.resize(inverted_blurred_img, (960, 540))
##cv2.imshow("4th", ims)
##cv2.imshow('5th image',pencil_sketch_TMG)
ims = cv2.resize(pencil_sketch_TMG , (500, 500))
cv2.imshow("2nd", ims)
cv2.imwrite("C:/Users/Mohammed Yaseen/Desktop/python/converted.jpg",pencil_sketch_TMG)

cv2.waitKey(0)


