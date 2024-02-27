from PIL import Image
import os

# image.save("/Users/devansh/Folder_1/Code/Python/main_folder_python/learn/Emilia_Clarke2.png")

# image = Image.open("/Users/devansh/Folder_1/Code/Python/main_folder_python/learn/Emilia_Clarke.jpg")

# image.show()
if not os.path.exists("./learn/pngs_converted_from_jpg"):
    os.mkdir("./learn/pngs_converted_from_jpg")

if not os.path.exists("./learn/resize"):
    os.mkdir("./learn/resize")
size = (400,400)# has to be a tuple in this
for f in os.listdir("./learn"):# this . means current directory
    if f.endswith(".jpg") or f.endswith(".png"):
        # print(f)
        i = Image.open("./learn/"+f)
        file_name, file_ext = f.split(".")
        # print(file_name)
        i.thumbnail(size)
        i.save("./learn/resize/{}_resized.{}".format(file_name,".png"))
    # print(f)