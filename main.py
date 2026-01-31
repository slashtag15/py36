import pygame as pyg
import random
pyg.init()
W=800
H=600
scr=pyg.display.set_mode((W,H))
pyg.display.set_caption("space invader")
bg=pyg.image.load("back.jpg")
roc=pyg.image.load("rock.png")
fir=pyg.image.load("magic.png")
bg=pyg.transform.scale(bg,(W,H))
roc=pyg.transform.scale(roc,(60,100))
fir=pyg.transform.scale(fir,(80,120))

don=False
FPS=60
x=350
xx=400
clc=pyg.time.Clock()
while not don:
    clc.tick(FPS)
    for ev in pyg.event.get():
        if ev.type==pyg.QUIT:
            pyg.quit()
        key=pyg.key.get_pressed()
    if key[pyg.K_RIGHT]:
        x=x+5
    if key[pyg.K_LEFT]:
        x=x-5
    if x>740:
        x=350
    if x<10:
        x=350
    scr.blit(bg,(0,0))
    scr.blit(roc,(x,500))
    scr.blit(fir,(xx,50))
    pyg.display.flip()