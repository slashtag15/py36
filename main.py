import pygame as pyg
pyg.init()
W=800
H=600
scr=pyg.display.set_mode((W,H))
pyg.display.set_caption("space invader")
bg=pyg.image.load("back.jpg")
roc=pyg.image.load("rock.png")
fir=pyg.image.load("magic.png")
bg=pyg.transform.scale(bg,(W,H))
roc=pyg.transform.scale(roc,(60,120))
fir=pyg.transform.scale(fir,(50,70))

don=False
FPS=60
clc=pyg.time.Clock()
while not don:
    clc.tick(FPS)
    for ev in pyg.event.get():
        if ev.type==pyg.QUIT:
            pyg.quit()

    scr.blit(bg,(0,0))
    scr.blit(roc,(350,500))
    scr.blit(fir,(400,50))
    pyg.display.flip()