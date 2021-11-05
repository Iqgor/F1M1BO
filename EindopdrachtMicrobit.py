# Add your Python code here. E.g.
from microbit import *

display.scroll('GAMES')

import random

answers = [
    "MISSCHIEN WEL", 
    "100% ZEKER",
    "HET LIJKT EEN JA",
    "JA",
    "NEE", 
    "VERW8 HET MAAR NIET",
    "DE OUTCOME LIJKT OK",
    "YOU MAY RELY ON IT",
    "VRAAG HET NOG EEN X",
    "HOU HET MAAR VOOR JE ZELF", 
    "MET GEEN ENKELE TWIJFEL",

]


while True:
    if button_b.is_pressed():
       display.show(random.randint(1, 6))
       sleep(1000)
    elif button_a.is_pressed(): 
        tool = random.randint(0,2)
        if tool == 0:
            display.show(Image.SQUARE_SMALL)
            sleep(1000)
        elif tool == 1:
            display.show(Image.SQUARE) 
            sleep(1000)
        else:
            display.show(Image.SWORD)
            sleep(1000)
    
    elif accelerometer.was_gesture("shake"):
       display.clear()
       sleep(2000)
       display.scroll(random.choice(answers))
         

    
        
   
     