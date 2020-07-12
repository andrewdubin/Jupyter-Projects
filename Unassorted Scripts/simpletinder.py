import pyautogui as pag
from time import sleep

#hold cursor over like button, then run program using a keyboard shortcut

like_button = pag.position()

i = 0
while i < 100:
    pag.click(like_button[0],like_button[1])
    sleep(1)
    i += 1
