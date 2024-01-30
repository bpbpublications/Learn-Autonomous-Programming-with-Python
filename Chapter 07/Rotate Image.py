from PIL import Image
objImage = Image.open("Image of a Bird.jpg")	
objImage = objImage.rotate(180)	
objImage.save("Rotated Image of a Bird.jpg")
