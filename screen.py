import pyautogui
from PIL import Image

p = pyautogui.screenshot(region=(397,119,600,600))
p.save("p.png")