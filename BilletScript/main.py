import yaml
import settings
import os
from latexify import latexify
from ticket import doTicket

###############################################################################
"""
This script should be executed from the folder i lies within.
Also all the latex files should be placed in the same folder.
The destination of the ticketID file and the yaml file does not matter
"""
###############################################################################

###############################################################################
# Setup
###############################################################################
templatePath = settings.latexPath + "/" + settings.latexTemplateName
outputPath = settings.latexPath + "/" + settings.latexOutputName


#The yaml file used. It contains all necesarry information
yamlFile = open(settings.yamlPath, 'r')

#The file containing all Ticket ID's
ticketFile = open(settings.ticketIdPath,'r')

if not os.path.exists(settings.latexPath):
     os.makedirs(settings.latexPath)

#The Latex template where everything is inserted into
latexTemplate = open(templatePath, 'r')

#The final latex document where everything has been inserted into.
#This .tex file needs to be compiled after this script has been run	
outputFile = open(outputPath, 'w')

yamlLoaded = yaml.load_all(yamlFile) # A iterator of dictionaries

# Converts the yamlLoaded iterator into a list
values = [val for val in yamlLoaded] 

ticketIDs = [] # an array containing all the ticketID's from ticketFile
 

###############################################################################
# Section where the magic happens
###############################################################################

# Creates all the tickets based on the values in the dictionaries 
# in values
i = 0
for line in ticketFile.readlines():
     if len(line) > 1:
          ticket = line.replace("\n", "")
          ticketIDs.append(ticket)
          doTicket(ticket, values[i % len(values)])
          i += 1

# Inserts all the images into the loaded latex template
for line in latexTemplate.readlines():
     if line == "<REPLACE>\n":
          outputFile.write(latexify(ticketIDs))
     else:
          outputFile.write(line)




print ""
print "Finished creating " + str(i) + " ticket images"
print ""
###############################################################################
# Cleanup
###############################################################################
yamlFile.close()
ticketFile.close()
latexTemplate.close()
outputFile.close()


