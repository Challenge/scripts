from settings import latexPath
from TextOnImage import drawStringOnImage
import os

# Makes a ticket.
# A ticket in this case is an image of a ticket where the ticket ID has been written on it.
def doTicket(ticketId, values):
     print "Doing ticket: " + str(ticketId)
     ticketImage = values['ticketImage']
     font = (fontPath, fontSize) = (values['fontPath'], values['fontSize'])

     outputImagePath = latexPath +"/"+ "tickets"
     imgName = ticketId + ".png"
     outputImage =  outputImagePath + "/" + imgName

     color = tuple(values['fontColor'])

     (txc, tyc) = textCenter = tuple(values['textCenter'])

     tick = "Billet-ID:" + ticketId
     moreInfo = "Se mere information paa dikulan.dk"

     if not os.path.exists(outputImagePath):
          os.makedirs(outputImagePath)


     lineOffset = fontSize;

     drawStringOnImage(ticketImage, tick, font, color, textCenter, outputImage)
     drawStringOnImage(outputImage, moreInfo, font, color, (txc,tyc + lineOffset), outputImage)

