import os
file = open("demofile.txt","w")
file.write("oops overwritten!")
file.write("hello world, its  me  again")
file.close()

import os
file =open('demofile.txt', "a")
file.write("appending and depenfding")
file.close()

'''import os
file = open("newfile.txt","x")
file.write("am new here")
file.close()'''

import os
file =open("stev.txt", "w")
file.write("am also new here!")
file.write("jeez, back to the basics, am all whole in another existensional life, or am i  in a  new dimension!")

file.close()
#check if file exists
import os
if os.path.exists("stev.txt"):
    print("file does exist actually")
    #os.remove("newfile.txt")
else:
    print("file does not exist")
"""
    
#remove file
import os
os.remove("stev.txt")

#deleting a folder
import  os
os.rmdir("folder g")"""


