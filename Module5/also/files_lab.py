import os
import re
dir = "F:\\"
for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    if re.match(r"[\w-]+\.txt",filename) and os.path.isfile(f):
        print(f)
        with open(f,"rb") as file1:
            print(file1.read())

