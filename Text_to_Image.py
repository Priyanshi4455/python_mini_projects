!pip install pillow

#pillow / PIL
#Text to Image    >>>(Image, ImageDraw, ImageFont)
from PIL import Image, ImageDraw, ImageFont
txt=input("Enter Your Text: ")

#Create Image
image=Image.new("RGB", (800,300), "white")

#Create Drawing Object
draw=ImageDraw.Draw(image)

#Load Font
font=ImageFont.load_default()    #fontsize, fontStyle

#Draw text on image
draw.text( (50,100) , txt, fill="black",font=font)

#Save Image
image.save("txt_image.png")
print("Image Generated Successfully!")
