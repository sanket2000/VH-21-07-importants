'''from PIL import Image
img = Image.open('images/letters/set1/blue/75.png', 'r')
img = img.convert("RGBA") 
img_w, img_h = img.size
background = Image.open('../test.png', 'r')#Image.new('RGBA', (1440, 900), (255, 255, 225, 225))
bg_w, bg_h = background.size
offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
background.paste(img, offset)
background.save('out3.png')
'''
import textwrap
import os
from PIL import Image

def textlist(text): # converts text into list of strings
	list1 = text.split("<br />")
	
	textlist = []
	for text in list1:
		textlist= textlist + textwrap.wrap(text,width = 33)
	return(textlist)


scale = 15
xoff = 42
yoff = 40
line_spacing = 23

letter_spacing = 10
max_lines = 18


inputtext = 'test2.text'
f = open(inputtext, "r")
text = textlist(f.read())
f.close

letterlist = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,.?{}()-_+=*&^%@<>|/'\"\\;:"


#for char in text:
filename = 'images/letters/set1/blue/{}.png' 
bg_file = 'images/bg/ruled.jpg'
save_name = 'page{}.png'
bg = Image.open(bg_file, 'r')
bg_w, bg_h = bg.size
text_img = Image.new('RGBA', (bg_w, bg_h), (0, 0, 0, 0))
text_img.paste(bg, (0,0))
image_list = []

i = 0
j = -1
img_num = 0

#str1 = '\n'
#str1 += str1.join(text)
for str1 in text:
	print(str1)
	i = 0
	j +=1
	for letts in str1:
		if(letts in letterlist):
			if i*letter_spacing < bg_w - xoff - 2*scale:
				pass
			else:
				i = 0
				j += 1

			if j > max_lines:
				text_img.save(save_name.format(img_num), format="png")
				text_img = text_img.convert('RGB')#.resize((2480, 3508), Image. ANTIALIAS)
				image_list.append(text_img)
				img_num += 1
				i = 0
				j = 0
				text_img = Image.new('RGBA', (bg_w, bg_h), (0, 0, 0, 0))
				text_img.paste(bg, (0,0))
			if ord(letts) == 32 and i==0:
				pass
			else:
				try:
					ironman = Image.open(filename.format(ord(letts)), 'r').resize((2*scale,3*scale))
				except:
					ironman = Image.open(filename.format(ord(letts)), 'r').resize((2*scale,3*scale))
				text_img.paste(ironman, (i*letter_spacing + xoff,j*line_spacing + yoff), mask=ironman)

			i += 1

text_img.save(save_name.format(img_num), format="png")
text_img = text_img.convert('RGB')#.resize((2480, 3508), Image. ANTIALIAS)
image_list.append(text_img)

image_list[0].save('imagelist.pdf',save_all=True, append_images=image_list[1:])
