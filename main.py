import cv2
import numpy as np
from PIL import Image, ImageFilter 
from PIL import Image, ImageDraw, ImageFont
 
def pic_to_sketch(file_name):
    picture = cv2.imread(file_name) # file name
    gray_picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY) #src, gray pic format
    #cv2.imshow('gray picture', gray_picture)
    inverted_picture = cv2.bitwise_not(gray_picture)
    #cv2.imshow('inverted picture', inverted_picture)
    blur_picture = cv2.blur(inverted_picture, (20,20)) # src, ksize
    #cv2.imshow('blurred picture', blur_picture)
    sketch = cv2.divide(gray_picture, 255,blur_picture, scale=256) #array1, array 2 and scale = 256
    cv2.imshow('sketch’, sketch)
    cv2.imwrite('sketch.jpg’, sketch) # save image

def pic_to_cartoon(file_name):
    pic = cv2.imread(file_name) # file path/file name
    gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY) # src, format for gray
    #cv2.imshow('Gray Image', gray)
    gray = cv2.medianBlur(gray, 5) # 5 = degree of blurring
    #cv2.imshow('Blurred gray Image', gray)
    borders = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,7,5)   # apply threshold to get borders
    #cv2.imshow('Borders', borders)
    color = cv2.bilateralFilter(pic, 9,300,300) 
    #cv2.imshow('color’, color)
    cartoon = cv2.bitwise_and (color, color, mask = borders)
    cv2.imshow('final’, cartoon)
    cv2.imwrite('cartoon.jpg’, cartoon)

def pic_to_blackandwhite(file_name):
    pic = cv2.imread(file_name)
    grayImage = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY) #src, gray pic format
    (thresh, blackAndWhiteImage) =cv2.threshold(gray Image, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow('Black white image', blackAndWhiteImage)
    cv2.imwrite('B&W.jpg', blackAndWhiteImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def pic_to_grayimage(file_name):
    picture = cv2.imread(file_name) # file name
    gray_picture = cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY) #src,gray pic format
    #cv2.imshow('gray picture', gray_picture)
     cv2.imshow('grey', gray_picture)
     cv2.imwrite('grey.jpg', gray_picture)

def pic_to_contour(file_name):
    im1 = Image.open(file_name) 
    # applying the contour filter 
    im2 = im1.filter(ImageFilter. CONTOUR) 
    im2.show()
    im2.save("contour.jpg")

def pic_to_blur(file_name):
    #creating an image object 
    im1 = Image.open(file_name) 
    # applying the blur filter 
    im2 = im1.filter(ImageFilter.BLUR) 
    im2.show()
    im2.save("blur.jpg")
def pic_to_emboss(file_name):
    im1 = Image.open(file_name)
    # applying the emboss filter
    im2 = im1.filter(ImageFilter. EMBOSS)
    im2.show()
    im2.save("emboss.jpg")
def pic_to_border(file_name):
  # read the target file
  target_img = cv2.imread(file_name)
  # create a border of a specfic color (here: black) and apply to image
  BLACK= [0,0,0]
  black_border_img=cv2.copyMakeBorder(target_img,20,20,20,20, cv2.BORDER_CONSTANT, value=BLACK)
  cv2.imshow("BORDER_CONSTANT", black_border_img)
  cv2.waitKey(0)
  cv2.imwrite('border.jpg', black_border_img)

def pic_to_enhance(file_name):
    # creating an image object 
    im1 = Image.open(file_name)
    # applying the EDGE_ENHANCE filter
    im2 = im1.filter(ImageFilter.EDGE_ENHANCE)
    im2.show()
    im2.save('edge enhance.jpg')

def water_mark(file_name):
    try:
        image = Image.open(file_name)
    except:
        print ("Unable to load image")
    idraw = ImageDraw.Draw(image)
    text=input ("Enter text to be displayed")
    font = ImageFont.truetype("arial.ttf", size=22)
    idraw.text ((10, 10), text, font=font)
    image.show('watermarked.png')
    image.save('watermarked.png')

 #main
print ("\t\t\welcome To Photo Editor\t\t\t")
file_name = input ('Enter the File Name:')
choice =1
while choice! =0:
    print ("enter your choice:\n
 choice 1: sketch image\n 
choice 2: cartoon image\n 
choice 3: black and white\n
 choice 4: grey image\n 
choice 5: contour\n 
choice 6: Blur\n 
choice 7: emboss\n 
choice 8: Border\n 
choice 9: edge enhance\n 
choice 10: Text on the Image")
   
image=int (input ())
    if (image==1):
        pic_to_sketch(file_name)
    elif (image==2):
        pic_to_cartoon(file_name)
    elif (image==3):
        pic_to_blackandwhite(file_name)
    elif (image==4):
        pic_to_grayimage(file_name)
    elif (image==5):
        pic_to_contour(file_name)
    elif (image==6):
        pic_to_blur(file_name)
    elif (image==7):
        pic_to_emboss(file_name)
    elif (image==8):
        pic_to_border(file_name)
    elif (image==9):
        pic_to_enhance(file_name)
    else:
        water_mark(file_name)
pic = cv2.imread(file_name) # file name
cv2.imshow('Original Image', pic) # original pic

