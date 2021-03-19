import numpy as np
from PIL import Image,ImageDraw,ImageFont
import textwrap
import json


 

def textlist(text): # converts text into list of strings
	list1 = text.split("<br />")
	textlist = []
	for text in list1:
		textlist= textlist + textwrap.wrap(text,width = data["width"])
	return(textlist)

def makedoc(data,textlist): # draws the custom font text on image 
	#load image 
	img = Image.open(data["BgImg"]).convert('RGB')
	draw = ImageDraw.Draw(img)
	pixellat=ImageFont.truetype(data["Font"],data["Fontsize"])
	imagelist = []
	page1 = 0
	#generate document
	#draw.text((data["x-axis"],10,data["name"],(0,0,0),font=pixellat))
	#draw.text(300,10,str(data["Roll"]),(0,0,0),font=pixellat)
	i = 0
	k = 0 
	for text in textlist:
		draw.text((data["x-axis"],(data["y-axis"] + int(i*float(data["line spacing"])))),text,(0,0,0),font=pixellat)
		i = i + 1
		if i == 20 and k == 0:
			i = 0
			imagge = img # loading next page
			img = Image.open(data["BgImg"]).convert('RGB')
			draw = ImageDraw.Draw(img)
			k = 1
		elif i == 20:
			i = 0
			imagelist.append(img) # loading next page
			img = Image.open(data["BgImg"]).convert('RGB')
			draw = ImageDraw.Draw(img)
	if k == 0:
		imagge  = img
	else:
		imagelist.append(img)	
	imagge.save('output.pdf',save_all=True, append_images=imagelist)	# saving the final pdf
 	
with open('settings.json') as f:
  data = json.load(f)
	
#image = 'ruled.jpg'
#inputtext = 'test.text'
#font = 'blzee.ttf'
f = open(data["Inputext"], "r")
text = textlist(f.read())
f.close

makedoc(data,text)





