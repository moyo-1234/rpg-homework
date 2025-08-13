import pgzrun
import random

WIDTH =600
HEIGHT = 383
Gameover = 0
objects = ["cricket","soccer"]
def arrange_objects():
    Act = []
    Apos = [100,500]
    random.shuffle(objects)
    for i in range(len(objects)):
        obj = Actor(objects[i])
        obj.x = Apos[i]
        obj.y = 0
        Act.append(obj)
    return Act
items = arrange_objects()

def draw():
    screen.blit("bg",(0,0))
    if Gameover==1:
        screen.draw.text("GAME OVER",fontsize = 20,color = "black",center = (370,160))
    else:
        for i in items:
            i.draw()

def update():
    if Gameover == 0:
        for i in items:
            i.y = i.y + 1

def on_mouse_down(pos):
    global Gameover
    for i in items:
        if i.collidepoint(pos):
            
            if "cricket" in i.image:
                screen.draw.text("YOU WIN",fontsize = 20,color = "black",center = (370,160))
                print("You win")
                break
            else:
                Gameover = Gameover + 1






pgzrun.go()  
