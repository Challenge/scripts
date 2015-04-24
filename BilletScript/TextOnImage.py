from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# Draws string on imgIn, the string will use fontPath as a font
# and will have a font size of fontSize
# the string will be drawn with the given color.
# When everything is done it save the new image at the imgOut destionation.
def drawStringOnImage(imgIn, string, (fontPath, fontSize), (r, g, b), textCenter, imgOut):
	
     font = ImageFont.truetype(fontPath ,fontSize)

     img = Image.open(imgIn)
     draw = ImageDraw.Draw(img)

     (x, y) = textCenter
	
     (textWidth, textHeight) = draw.textsize(string, font)

     textX = x - textWidth /2
     textY = y - textHeight /2

     draw.text((textX, textY), string, (r, g, b), font=font)
     draw = ImageDraw.Draw(img)

     img.save(imgOut)
     return img


