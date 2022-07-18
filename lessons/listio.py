import os
path = './images/'

if not os.path.exists(path):
    os.makedirs(path)
    
files = os.listdir(path)

for images in files:
    if (images.endswith('.jpg')):
        print(images)
        
images = [files for files in files if files.endswith('.jpg')]
print(images)

