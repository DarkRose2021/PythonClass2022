# Katie King 2022
from tkinter import Image
from PIL import Image as pil_image
import os

path = './new_images'
folder = "./images"


if not os.path.exists(path):
    os.makedirs(path)   

def fixPictures():    
    for count, image in enumerate(os.listdir(folder)):
        #rename
        dst = f"pic{count+1:04}.png"
        dst =f"{path}/{dst}" 
        
        newImage = pil_image.open((f'{folder}/{image}'))
        
        #crop
        width, height = newImage.size
        area = (0,0,width-(width-height), height)
        newImage = newImage.crop(area)
        
        #rotate
        newImage = newImage.rotate(270)
        
        #grayscale
        newImage = newImage.convert('L')
        
        #thumbnails size
        newImage = newImage.resize((75,75))
        
        #moving
        newImage.save(dst)
               
fixPictures()