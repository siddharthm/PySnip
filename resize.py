from PIL import Image

# This script is designed for the kshitij website
# It takes as input the folder root where the images are , the output folder name
# It also takes Image base img counter and img counter finish and extension
# and thus takes inputs from root/(base+counter+extension) 

# Assumption is that images are taken from same camera and in order, though some 
# images may be missing in between

# It then resizes it and outputs it in OROOT folder with names from 1 to last image

# input folder, include whole path if not child of current directory
IROOT = "grppics/" 

# output folder, include whole path if not child of current directory
OROOT = "output/"

# Common part of image name
IMGBASE = "P1000"

# Extensions of the image
IMGEXTN = ".JPG"

# Start number of images, also the different part of the image
IMGCOUNTER = 532

# End number of images, also the different part of the image
IMGCOUNTERF = 813

# Size you want to resize to
# if every image is of different size then put this in the loop with different aspect
RESIZE = (150,113)

# Rectangle to be cropped out
CUT = (25,0,25,27)

ERRORFILE = open("resize_errs.txt",'w')

j=1
for i in range(IMGCOUNTER,IMGCOUNTERF):
  try:
		im = Image.open(IROOT+IMGBASE+str(i)+IMGEXTN)
		im=im.resize(RESIZE,Image.ANTIALIAS)
		im.save(OROOT+str(j)+IMGEXTN,"JPEG")
		j+=1
	except:
		print "Error for "+IROOT+IMGBASE+str(i)+IMGEXTN
		ERRORFILE.write(IROOT+IMGBASE+str(i)+IMGEXTN)
