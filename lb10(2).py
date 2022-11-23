import os
import shutil
from pathlib import Path
py = open("D:\\Задания\\Extracted\\MY_FILES\\py.txt","w")
whl = open("D:\\Задания\\Extracted\\\MY_FILES\\whl.txt","w")
zip = open("D:\\Задания\\Extracted\\\MY_FILES\\zip.txt","w")
for i in os.listdir("D:\\Задания\\Extracted\\\MY_FILES"):
    a = Path(i)
    ext = i.split(".")[-1]
    if ext == "py":
        arg = a.name+"\n"
        py.write(arg)
    elif ext == "whl":
        arg = a.name+"\n"
        whl.write(arg)
    elif ext == "zip":
        arg = a.name+"\n"
        zip.write(arg)