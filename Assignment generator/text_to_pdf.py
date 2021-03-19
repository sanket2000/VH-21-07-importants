import numpy as np
from PIL import Image,ImageDraw,ImageFont
import textwrap
 

def textlist(text): # converts text into list of strings
	list1 = text.split("\n")
	textlist = []
	for text in list1:
		textlist= textlist + textwrap.wrap(text,width = 55)
	return(textlist)

def makedoc(image,textlist,font): # draws the custom font text on image 
	#load image 
	img = Image.open(image).convert('RGB')
	draw = ImageDraw.Draw(img)
	pixellat=ImageFont.truetype(font,12)
	imagelist = []
	imagge = 0
	#generate document
	x = 50
	y = 54
	i = 0
	k = 0 
	for text in textlist:
		draw.text((x,(y + int(i*23.5))),text,(0,0,0),font=pixellat,spacing = 11,align ="left")
		i = i + 1
		if i == 20 and k == 0:
			i = 0
			imagge = img # loading next page
			img = Image.open(image).convert('RGB')
			draw = ImageDraw.Draw(img)
			k = 1
		elif i == 20:
			i = 0
			imagelist.append(img) # loading next page
			img = Image.open(image).convert('RGB')
			draw = ImageDraw.Draw(img)
	if k == 0:
		imagge  = img
	else:
		imagelist.append(img)	
	imagge.save('imagelist.pdf',save_all=True, append_images=imagelist)	# saving the final pdf
 	
 	
image = 'ruled.jpg'
inputtext = 'test.text'
font = 'blzee.ttf'
f = open(inputtext, "r")
text = textlist(f.read())
f.close
makedoc(image,text,font)





