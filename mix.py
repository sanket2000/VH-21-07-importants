import textwrap
import random
import os
from PIL import Image

def textlist(text): # converts text into list of strings
	list1 = text.split("\n")
	textlist = []
	for text in list1:
		textlist= textlist + textwrap.wrap(text,width = 55)
	return(textlist)


scale = 16
xoff = 42
yoff = 38
line_spacing = 23

letter_spacing = 13
max_lines = 18
totalset = len(os.listdir("images/letters")) + 1

inputtext = 'test.txt'
f = open(inputtext, "r")
#text = textlist(f.read())
text = f.read()
#print(ord(text[5]))
f.close

letterlist = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,.?{}()-_+=*&^%@<>|/'\"\\;:"


#for char in text:
filename = 'images/letters/set{}/blue/{}.png' 
bg_file = 'ruled.jpg'
save_name = 'page{}.png'
bg = Image.open(bg_file, 'r')
bg_w, bg_h = bg.size
text_img = Image.new('RGBA', (bg_w, bg_h), (0, 0, 0, 0))
text_img.paste(bg, (0,0))
image_list = []

i = 0
j = 0
img_num = 0
str1 = ''
str1 += str1.join(text).replace("<br />", " ").replace("<br/>", " ")

#print(str1)
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
				ironman = Image.open(filename.format(random.randrange(1, totalset),ord(letts)), 'r').resize((2*scale,3*scale))
			except:
				ironman = Image.open(filename.format(1,ord(letts)), 'r').resize((2*scale,3*scale))
			text_img.paste(ironman, (i*letter_spacing + xoff,j*line_spacing + yoff), mask=ironman)

		i += 1

text_img.save(save_name.format(img_num), format="png")
text_img = text_img.convert('RGB')#.resize((2480, 3508), Image. ANTIALIAS)
image_list.append(text_img)

image_list[0].save('imagelist.pdf',save_all=True, append_images=image_list[1:])
print("PDF made successfully....")