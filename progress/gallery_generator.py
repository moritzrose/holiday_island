import os

files = sorted(os.listdir("."))
for f in files:
    if f.endswith(".png"):
        print(f'<img alt="" src="progress/{f}" style="width: 350px;">')