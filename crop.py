from PIL import Image
import os

# This script is designed for the kshitij website
# It takes as input the folder root where the images are , the output folder name
# It also takes Image base img counter and img counter finish and extension
# and thus takes inputs from root/(base+counter+extension) 

# It then resizes it, crops it and outputs in a folders with each of them having 
# 9 images

IROOT = "output/"
OROOT = "output2/"
IMGBASE = ""
IMGEXTN = ".JPG"
IMGCOUNTER = 1
IMGCOUNTERF = 261


RESIZE = (150,113)
CUT = (25,0,25+86,0+100)

ERRORFILE = open("crop_errs.txt",'w')


for i in range(IMGCOUNTER,IMGCOUNTERF/9):
  os.makedirs(OROOT+str(i)+"/")	
	try:
		for j in range(1,10):
			im = Image.open(IROOT+IMGBASE+str((i-1)*9+j)+IMGEXTN)
			#im.save(OROOT+str(i)+"/b"+str(j)+IMGEXTN,"JPEG")
			im=im.crop(CUT)	
			im.save(OROOT+str(i)+"/"+str(j)+IMGEXTN,"JPEG")
	except:
		print "Error "+i
