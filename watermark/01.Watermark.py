from PIL import Image, ImageDraw, ImageFont
import os

from pillow_heif import register_heif_opener

register_heif_opener()
# create Image object with the input image

# resize_folder_path = 'C:/Users/tanan/Google Drive/Insta Pics/1RawPics'
resize_folder_path = '1.Source'
resize_folder_output_path = '2.Output'
quality_val = 35
rez4k = 1750

def getResizedValues(tempImage):
    x,y=tempImage.size[0],tempImage.size[1]
    if x < y:
        y = y/x*rez4k
        x = rez4k
    else:
        x = x/y*rez4k
        y = rez4k
    return tempImage.resize((int(x), int(y)), Image.LANCZOS)

imageList = [];
for file in os.listdir(resize_folder_path):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".JPEG") or file.endswith(".heic"):
        # print("Filename : ", file)
        # print(os.path.join("/mydir", file))
        imageList.append(file)

# def save4Images(img):
    

def applyWatermark(imgName):
    # im1 = Image.open(resize_folder_output_path+'/'+imgName)
    # watermark = Image.open('21.gif')
    # im1 =  im1.paste(watermark)
    # im1.save('abc.jpg')
    # return img
    im1 = Image.open(resize_folder_output_path+'/'+imgName)
    imTemp = Image.open(resize_folder_output_path+'/'+imgName)
    im2 = Image.open('45.png')
    ximg, yimg = im1.size[0], im1.size[1]
    ximg2, yimg2 = im2.size[0], im2.size[1]

    margin = 35

    areaBox = (margin, margin)
    im1.paste(im2, areaBox, im2)
    im1.save(resize_folder_output_path+'/'+imgName.split('.')[0]+"a.jpg", quality=quality_val)

    im1 = Image.open(resize_folder_output_path+'/'+imgName)
    areaBox = (margin, yimg - margin - yimg2)
    im1.paste(im2, areaBox, im2)
    im1.save(resize_folder_output_path+'/'+imgName.split('.')[0]+"b.jpg", quality=quality_val)

    im1 = Image.open(resize_folder_output_path+'/'+imgName)
    areaBox = (ximg - margin - ximg2, margin)
    im1.paste(im2, areaBox, im2)
    im1.save(resize_folder_output_path+'/'+imgName.split('.')[0]+"c.jpg", quality=quality_val)

    im1 = Image.open(resize_folder_output_path+'/'+imgName)
    areaBox = (ximg - margin - ximg2, yimg - margin - yimg2)
    im1.paste(im2, areaBox, im2)
    im1.save(resize_folder_output_path+'/'+imgName.split('.')[0]+"d.jpg", quality=quality_val)

    im1.close()
    im2.close()
    # os.remove(resize_folder_output_path+'/'+imgName)

# 1. Resize Orignal Image ........................................

ctr = 0
for img_name in imageList:
    ctr = ctr + 1
    print("Processing "+str(ctr)+" : "+str(img_name))
    image = Image.open(resize_folder_path+'/'+img_name)
    # image = getResizedValues(image)  
    image = getResizedValues(image)
    if img_name.endswith(".heic"):
        img_name = img_name[:-4]+"JPEG"
    print(img_name)
    image.save(resize_folder_output_path+'/'+img_name, 'JPEG', quality=70)
    # applyWatermark(img_name)
    # image.close()
    # os.remove(resize_folder_output_path+'/'+img_name)




# 2. Resize logo according to the image dimenstoins
# 3. Lower the image qulaty value for save
# 4. Run program in loop for all images in X folder generates output in X_resize folder
