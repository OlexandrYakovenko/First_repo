from zipfile import ZipFile as zp
try:
    with zp("f:\\files.zip", mode="a") as archive:
        archive.write("F:\\file.txt","F:\\file1.txt")
except FileExistsError:
    print("File exists")