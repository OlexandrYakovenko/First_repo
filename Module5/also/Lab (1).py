#line="Просто рядок тексту"
try:
    with open("f:\\файл.txt","r") as file1:
        lines=file1.read().split("\n")
        print(lines[2].split(" "))

        
except Exception as e:
    print(f"Error: {e}")    