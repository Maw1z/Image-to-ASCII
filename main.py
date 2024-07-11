from PIL import Image
import sys
import re
from errors import NoFileExtensionError

def image_to_ascii(image_name, type, file_name):
    img = Image.open(image_name)
    w, h = img.size
    
    # Resizing image
    if w <= 100 and h <= 100:
        scale = 3
    elif w <= 800 and h <= 600:
        scale = 4
    else:
        scale = 5
    
    resized_img = img.resize((w//scale, h//scale))
    w_resized, h_resized = resized_img.size
    
    # Populating picture list with blank pixels
    picgrid = []
    for i in range(h):
        picgrid.append(["X"]*w)
        
    pix = img.load()
        
    for y in range(h):
        for x in range(w):
            if sum(pix[x,y]) == 0:
                picgrid[y][x] = "#"
            elif sum(pix[x,y]) in range(1, 100):
                picgrid[y][x] = "@"
            elif sum(pix[x,y]) in range(100, 200):
                picgrid[y][x] = "&"
            elif sum(pix[x,y]) in range(200, 300):
                picgrid[y][x] = "+"
            elif sum(pix[x,y]) in range(300, 400):
                picgrid[y][x] = "*"
            elif sum(pix[x,y]) in range(400, 500):
                picgrid[y][x] = ":"
            elif sum(pix[x,y]) in range(500, 600):
                picgrid[y][x] = "."
            elif sum(pix[x,y]) in range(600, 700):
                picgrid[y][x] = "'"
            elif sum(pix[x,y]) in range(700, 750):
                picgrid[y][x] = "-"
            else:
                picgrid[y][x] = " "
                
    file = open(file_name, "w")
    
    for column in picgrid:
        file.write("".join(column)+"\n")
                    
    file.close()
    
def get_file_extension(filename):
    extension = re.search(r"\.([^.]+)$", filename)
    if extension:
        return extension.group(1)
    else:
        raise NoFileExtensionError(f"No file extension found in filename: {filename}")
    
if __name__ == '__main__':
    try:
        extension = get_file_extension(sys.argv[1])
        image_to_ascii(sys.argv[1], extension, sys.argv[2])
    except NoFileExtensionError as e:
        print(e)
