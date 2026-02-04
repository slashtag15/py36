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
fir=pyg.transform.scale(fir,(100,120))
don=False
FPS=60
x=350
xx=random.randint(10,740)
yy=40
sor=0
lif=3
clc=pyg.time.Clock()
win=False
fon=pyg.font.SysFont("q.ttf",40)
def showtxt(txt,x1,y1,color="#FF6D00"):
    txtsrfc=fon.render(txt,True,color)
    scr.blit(txtsrfc,(x1,y1))
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
    yy=yy+5
    if yy>H:
        yy=40
        xx=random.randint(10,740)
        sor=sor+1
    rocrect=pyg.Rect(x,500,60,100)
    firrect=pyg.Rect(xx,yy,100,120)
    if rocrect.colliderect(firrect):
        lif=lif-1
        yy=40
        xx=random.randint(10,740)
    if sor>=30:
        win=True
    scr.blit(bg,(0,0))
    scr.blit(roc,(x,500))
    scr.blit(fir,(xx,yy))
    showtxt(f"score:{sor}",10,10)
    showtxt(f"lives:{lif}",10,50)
    if lif==0:
        showtxt("you lost",400,200,"#FF6D00")
        pyg.display.update()
        pyg.time.delay(5151)
        pyg.quit()
    if win:
        showtxt("you win",400,200,"#FF6D00")
        pyg.display.update()
        pyg.time.delay(5151)
        pyg.quit()
    pyg.display.flip()