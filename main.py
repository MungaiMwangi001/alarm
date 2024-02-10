#file handling - read
#craw- create"x", read "r", append "a", write ,"w"
import os

hj = open("C:\\Users\\admin\\OneDrive\\Desktop\\serene - Shortcut.lnk", 'r')
print(hj.read())
hj.close()

"""import os
hj=open("C:\Users\\admin\OneDrive\Desktop\serene - Shortcut.lnk", 'r')
print(hj.read(5))
hj.close()

import os#-line by line output
hj=open("C:\Users\admin\OneDrive\Desktop\serene - Shortcut.lnk", 'r')
print(hj.readline())
hj.close()

import os#-multiple lines but in a well organized manner
hj=open("C:\Users\admin\OneDrive\Desktop\serene - Shortcut.lnk", 'r')
print(hj.readlines())
hj.close()

import os#-reads a specific line
hj=open("C:\Users\admin\OneDrive\Desktop\serene - Shortcut.lnk", 'r')
print(hj.readline(3))
hj.close()
"""
#looping over a file object- saves memory,fast and efficient
import os
hj = open("serene.txt", "r")
for line in hj:
    print(hj.readlines())
hj.close()