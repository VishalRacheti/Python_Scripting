import os
import sys
import shutil

print(sys.argv)

shutil.copy("text.sh" , "text1.sh")  # To Copy and Paste the file
shutil.move("text.sh" , "text2.sh")  # To move the file
