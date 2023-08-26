import os
import shutil

path = "input_path"
output = "output_path"

os.chdir(path)
print(os.listdir(path))

for i in os.listdir(path):
    os.system(f'jupyter nbconvert --to html {i}')

for i in os.listdir(path):
    source = path + "\\" + i
    ud = source.split(".")
    if ud[1] == "html":
        des =  output + "\\" + i
        print(source)
        shutil.copy(source, des)