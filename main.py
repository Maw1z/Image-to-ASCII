from PIL import Image
import sys

def image_to_ascii(image_name, file_name):
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
    w, h = resized_img.size
    
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
    
    for row in picgrid:
        file.write("".join(row)+"\n")
                    
    file.close()
  
if __name__ == '__main__':
    image_to_ascii(sys.argv[1], sys.argv[2])
