import pdfkit
import os

path = "input"
outpath = "output\\"

os.chdir(path)
note = os.listdir(path)

for i in note:
    po = i.split(".")
    print(f"now process {i}")
    pdfkit.from_file(i, f"{outpath + po[0]}.pdf")