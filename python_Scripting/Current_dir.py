import os

print ("To Get current working directory", os.getcwd()) # To get current working directory

os.chdir("C:/Users/dell/Pictures/Saved Pictures") # To change current working directory

print (" Current Working directory", os.getcwd()) # To working directory

print ("List the directory" , os.listdir()) # This command will list all the directory

os.mkdir("test11") #Creats the new directory


os.remove('test1')  # To Remove the directory

print("Enter the env variable", os.getenv("xyz"))  #To Access the Environement variable