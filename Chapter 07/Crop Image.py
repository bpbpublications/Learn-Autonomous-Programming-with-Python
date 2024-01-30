from PIL import Image
objImage = Image.open("Image of a Bird.jpg")	
fltWidth,fltHeight = objImage.size
fltArea = (fltWidth/5, fltHeight/5, 4*fltWidth/5, 4*fltHeight/5)
objImage = objImage.crop(fltArea)
objImage.save("Cropped Image of a Bird.jpg")
