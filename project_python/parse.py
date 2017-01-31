import os
import sys
import time
import urllib2
import xml.etree.ElementTree as ET

#Get the root node of the XML hierarchy
tree = ET.parse('stream.xml')
root = tree.getroot()

#create file for output
f = open('streamdata.csv','w')

#Get the 'Detector-id' and its 'status' from XML
for i in range(1,100,1):
    z = root.getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[i]
    print z.getchildren()[0].text, '|', z.getchildren()[1].text
    f.write( z.getchildren()[0].text+ ','+ z.getchildren()[1].text+ "\n")

#close out file
f.close()
