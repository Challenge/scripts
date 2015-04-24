import settings


# Takes a list of ticketID's and 
# creates latex code for each of the ticketID's corresponding
def latexify(ticketList):
     string = "\\begin{figure}\n"

     for i in range(0,len(ticketList)):
          ticket = ticketList[i].replace("\n","") + ".png"
          string += "\\includegraphics[" + settings.imgOptions + "]{tickets/"+ ticket + "}\n"
  
          if (i + 1) % settings.imgPrPage == 0:
               string += "\\end{figure}\n\n\\pagebreak\n\\begin{figure}\n"

          elif (i + 1) % settings.rowPrPage == 0:
               string += "\\\\\\\\\n"
	
     string += "\end{figure}\n"

     return string

