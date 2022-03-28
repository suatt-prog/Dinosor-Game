import pygame
from pygame import QUIT
pygame.init()
ekran=pygame.display.set_mode([800,600])
run=True
pygame.display.set_caption("Typerex Dinozor")
height=300
sefer=0
horizont=600
dinazor=pygame.image.load("dinazor.PNG")
engel=pygame.image.load("engel.PNG")
first=1
bas=0
speed=0.5
skor=0
yazı=pygame.font.SysFont("monospace",15)
label = yazı.render(("Skorunuz " + str(skor)), 3, (0, 0, 0))
while run:
    if 150-horizont<70 and 150-horizont>69:
        skor=skor+1
        horizont=600
        speed=speed+0.02
    if horizont-150<36 and horizont-150>0 and 300-height<36:
        run=False
    if sefer>0 and sefer<=84/speed:
        sefer=sefer-1
        height=height-speed
    if sefer>-1 and sefer<=0 and bas==1:
        bas=2
        sefer=-1*(84/speed)
    if sefer<0:
        sefer=sefer+1
        height=height+speed
        if sefer>-1:
            sefer=0
    horizont=horizont-speed
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                run=False
            if event.key==pygame.K_UP and  sefer==0:
                bas=1
                sefer=84/speed
    ekran.fill((255,255,255))
    label = yazı.render(("Skorunuz " + str(skor)), 3, (0, 0, 0))
    ekran.blit(engel,(horizont,300))
    ekran.blit(label,(600,100))
    ekran.blit(dinazor,(150,height))
    pygame.display.update()
