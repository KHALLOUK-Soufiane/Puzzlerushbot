import pyautogui
from PIL import Image

p = pyautogui.screenshot(region=(397,119,600,600))
width, height = p.size
for i in range(0,8):
    for j in range(0,8):
        c = p.crop(box=(j*width/8, i*height/8, (j*width/8)+(width/8), (i*height/8)+(height/8)))
        c.save("board/" + chr(ord('a')+j) + str(8-i) + ".png")

