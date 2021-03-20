import os
os.system("git init")
# images = 'images'
os.system("git add .")
comment = 'add images'
os.system("git commit -m "+ comment)
os.system("git remote add origin https://github.com/sanket2000/VH-21-07-importants.git")
os.system("git push -u origin master")