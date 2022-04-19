#Ohjelman kirjastot

from numpy import unicode_
import pygame
import os
import random


#Määritellään värit

valkoinen=(255, 255, 255)
musta = (0, 0, 0)
vihrea = (74, 151, 72)
harmaa=(50, 50, 50) 
punainen=(172, 55, 55) 
sininen=(89, 102, 186) 
keltainen=(255, 255, 0)
lila=(141, 64, 166)
HOVER_COLOR = (50, 70, 90)


#Pelin ikkunan koko ja perusmuuttujat

LEVEYS, KORKEUS = 800, 800
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Nappaa pallot")
FPS=30
kello=pygame.time.Clock()


#Lisätään kuvat ja fontti

pygame.init()
font=pygame.font.Font("freesansbold.ttf",32)

Tausta=pygame.image.load(os.path.join("kuvat", "Tausta.PNG"))
Tausta=pygame.transform.scale(Tausta, (800,800))

Pallo_vihr=pygame.image.load(os.path.join("kuvat", "Vihree_pallo.png"))
Pallo_vihr=pygame.transform.scale(Pallo_vihr,(50,50))

Pallo_sin=pygame.image.load(os.path.join("kuvat", "Sininen_pallo.png"))
Pallo_sin=pygame.transform.scale(Pallo_sin,(50,50))

Pallo_lila=pygame.image.load(os.path.join("kuvat", "lila_pallo.png"))
Pallo_lila=pygame.transform.scale(Pallo_lila,(50,50))

Pallo_pun=pygame.image.load(os.path.join("kuvat", "punanen_pallo.png"))
Pallo_pun=pygame.transform.scale(Pallo_pun,(50,50))
 
Putki1=pygame.image.load(os.path.join("kuvat", "putki.png"))
Putki1=pygame.transform.scale(Putki1, (110,200))
Putki1 = pygame.transform.rotate(Putki1, 45)

Putki2=pygame.image.load(os.path.join("kuvat", "putki.png"))
Putki2=pygame.transform.scale(Putki2, (110,200))
Putki2 = pygame.transform.rotate(Putki2, 140)

Putki3=pygame.image.load(os.path.join("kuvat", "putki.png"))
Putki3=pygame.transform.scale(Putki3, (110,200))
Putki3 = pygame.transform.rotate(Putki3, -45)

Putki4=pygame.image.load(os.path.join("kuvat", "putki.png"))
Putki4=pygame.transform.scale(Putki4, (110,200))
Putki4 = pygame.transform.rotate(Putki4, -134)

Putki_pun=pygame.image.load(os.path.join("kuvat", "Punainen_putki.png"))

Kolmio_pun_rect=pygame.Rect(345,410,40,40)
Kolmio_lila_rect=pygame.Rect(415,410,40,40)
Kolmio_sin_rect=pygame.Rect(415,340,40,40)
Kolmio_vihr_rect=pygame.Rect(347,340,40,40)

kuva_lahde = pygame.image.load(os.path.join("kuvat", "neliö.png"))
kuva_lahde=pygame.transform.scale(kuva_lahde, (210,210))

def piirrokset(pallo,vari, uusi_kuva, rect):
    naytto.blit(Tausta,(0,0))
    naytto.blit(vari,(pallo.x,pallo.y))
    naytto.blit(Putki1,(700, 700))
    naytto.blit(Putki2,(690, -120))
    naytto.blit(Putki3,(-120, 690))
    naytto.blit(Putki4,(-120,-120))
    naytto.blit(uusi_kuva, rect)
    pygame.display.update()


#Aloitussivun koodit

FONT = pygame.font.SysFont ("freesansbold.ttf", 60)
FONT2 = pygame.font.SysFont ("freesansbold.ttf", 100,)
OTSIKKO=FONT2.render("      Pelin nimi", True, valkoinen)
START = FONT.render("START", True, valkoinen)
LEADERBOARD = FONT.render("LEADERBOARD", True, valkoinen)
QUIT = FONT.render("BACK", True, valkoinen)
MENU = FONT.render("BACK", True, valkoinen)
PARAS = FONT.render("PARAS TULOS:", True, valkoinen)

rect_otsikko=pygame.Rect(130,100,600,60)
rect1 = pygame.Rect(248,300,325,80)
rect2 = pygame.Rect(248,400,325,80)
rect3 = pygame.Rect(248,500,325,80)
rect4 = pygame.Rect(248,500,325,80)
rect5 = pygame.Rect(130,100,600,60)
rect6 = pygame.Rect(248,300,325,80)

nappaimet = [
    [START, rect1, musta],
    [LEADERBOARD, rect2, musta],
    [QUIT, rect3, musta],
    [MENU, rect4, musta],
    ]


#Funktio hakee parhaan scoren tiedostosta tulokset.txt

def hae_paras_score():
    with open("src/tulokset.txt") as tiedosto:
        paras_score = int(tiedosto.read())
    return paras_score



def leaderboard():
    TULOS = FONT.render(str(hae_paras_score()), True, valkoinen)
    naytto.blit(Tausta,(0,0))
    pygame.draw.rect(naytto, musta, rect4)
    naytto.blit(MENU, rect4)
    naytto.blit(PARAS, rect5)
    naytto.blit(TULOS, rect6)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if rect4.collidepoint(pos):
                    valikko("aloitus", 0)


def valikko(muoto, score_arvo):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEMOTION:
                for nappain in nappaimet:
                    if nappain[1].collidepoint(event.pos):
                        nappain[2] = HOVER_COLOR
                    else:
                        nappain[2] = musta
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if rect1.collidepoint(pos):
                    main()
                if rect2.collidepoint(pos):
                    leaderboard()
                if rect3.collidepoint(pos):
                    pygame.quit()

        naytto.fill((34,139,34))

        for teksti, rect, vari in nappaimet:
            pygame.draw.rect(naytto, vari, rect)
            naytto.blit(teksti, rect)
        if muoto=="aloitus":
           naytto.blit(OTSIKKO,rect_otsikko)
        if muoto=="menu":
           SCORE=FONT2.render("YOUR SCORE: "+ str(score_arvo),True, keltainen)
           naytto.blit(SCORE,rect_otsikko)

        pygame.display.flip()
        kello.tick(15)


#Näyttää scoren pelissä

def nayta_score(x,y,score_arvo):
    score=font.render("Score: "+ str(score_arvo),True, (255,255,255))
    naytto.blit(score,(x,y))
    pygame.display.update()


#Pallojen määrittely

Spawn_lista=[(20,0),(790,780),(750,0),(0,750)]
pallo_lista=[Pallo_lila,Pallo_pun,Pallo_sin,Pallo_vihr,]
def Pallo(pallo,nopeus,spawni):
    if (spawni[0]==20) and (spawni[1]==0):
        if pallo.x<400:
            pallo.x+=nopeus
            pallo.y+=nopeus
    if (spawni[0]==790) and (spawni[1]==780):
        if pallo.x>350:
            pallo.x-=nopeus
            pallo.y-=nopeus
    if (spawni[0]==750) and (spawni[1]==0):
        if pallo.x>350:
            pallo.x-=nopeus
            pallo.y+=nopeus
    if (spawni[0]==0) and (spawni[1]==750):
        if pallo.y>350:
            pallo.x+=nopeus
            pallo.y-=nopeus


#Ohjelman pääfunktio

def main():

    #Määritellään muuttujia
    kaynnissa = True
    nopeus=2
    spawni=random.choice(Spawn_lista)
    pallo=pygame.Rect((spawni[0],spawni[1]),(50,50))
    vari=random.choice(pallo_lista)
    score_arvo=0
    score_paras = hae_paras_score()
    kierto = 0
    Pallo(pallo,nopeus,spawni)
    nayta_score(330,10,score_arvo)
    kuva = kuva_lahde.copy()
    kuva.set_colorkey(musta)
    uusi_kuva=kuva
    rect = kuva.get_rect()
    rect.center = (LEVEYS // 2, KORKEUS // 2)
    naytto.blit(kuva_lahde, rect)
    piirrokset(pallo, vari, kuva_lahde, rect)
    pygame.display.update()
    pressed = 1

    while kaynnissa:
        kello.tick(FPS)
        Pallo(pallo,nopeus,spawni)
        for tapahtuma in pygame.event.get():
            if tapahtuma.type==pygame.QUIT:
                kaynnissa=False
            if tapahtuma.type == pygame.KEYUP:
                pressed=1
        
        nappain = pygame.key.get_pressed()
        if nappain[pygame.K_LEFT] and pressed==1:
            if kierto==360 or kierto==-360:
                kierto=0
            for x in range(45):
                kierto += 2
                vanha_keskus = rect.center
                uusi_kuva = pygame.transform.rotate(kuva_lahde, kierto)
                rect = uusi_kuva.get_rect()
                rect.center = vanha_keskus
                naytto.blit(uusi_kuva, rect)              
                pygame.display.update(rect)
            pressed = 2

        if nappain[pygame.K_RIGHT] and pressed==1:
            if kierto==360 or kierto==-360:
                kierto=0            
            for x in range(45):
                kierto -= 2
                vanha_keskus = rect.center
                uusi_kuva = pygame.transform.rotate(kuva_lahde, kierto)
                rect = uusi_kuva.get_rect()
                rect.center = vanha_keskus
                naytto.blit(uusi_kuva, rect)
                pygame.display.update(rect)
            pressed=2

        Pallo(pallo,nopeus,spawni)
        piirrokset(pallo, vari, uusi_kuva, rect)
        nayta_score(330,10,score_arvo)
        vanha_keskus = rect.center
        uusi_kuva = pygame.transform.rotate(kuva_lahde, kierto)
        rect = uusi_kuva.get_rect()
        rect.center = vanha_keskus

        if kierto==0 or kierto==360 or kierto==-360:    
            vihr=pygame.draw.rect(naytto,vihrea, Kolmio_vihr_rect)
            sini=pygame.draw.rect(naytto,sininen, Kolmio_sin_rect)
            puna=pygame.draw.rect(naytto,punainen, Kolmio_pun_rect)
            lil=pygame.draw.rect(naytto,lila, Kolmio_lila_rect)
        if kierto==-90 or kierto==270:
            vihr=pygame.draw.rect(naytto,vihrea, Kolmio_sin_rect)
            sini=pygame.draw.rect(naytto,sininen, Kolmio_lila_rect)
            puna=pygame.draw.rect(naytto,punainen, Kolmio_vihr_rect)
            lil=pygame.draw.rect(naytto,lila, Kolmio_pun_rect)        
        if kierto==-180 or kierto==180:   
            vihr=pygame.draw.rect(naytto,vihrea, Kolmio_lila_rect)
            sini=pygame.draw.rect(naytto,sininen, Kolmio_pun_rect)
            puna=pygame.draw.rect(naytto,punainen, Kolmio_sin_rect)
            lil=pygame.draw.rect(naytto,lila, Kolmio_vihr_rect)
        if kierto==-270 or kierto==90:   
            vihr=pygame.draw.rect(naytto,vihrea, Kolmio_pun_rect)
            sini=pygame.draw.rect(naytto,sininen, Kolmio_vihr_rect)
            puna=pygame.draw.rect(naytto,punainen, Kolmio_lila_rect)
            lil=pygame.draw.rect(naytto,lila, Kolmio_sin_rect)
        if pallo.colliderect(vihr):
            if vari==Pallo_vihr:
                spawni=random.choice(Spawn_lista)
                vari=random.choice(pallo_lista)
                pallo=pygame.Rect((spawni[0],spawni[1]),(50,50))
                score_arvo+=1
                if (score_arvo==1) or (score_arvo==5) or (score_arvo==10):
                    nopeus+=1
            else:
                valikko("menu",score_arvo)
        if pallo.colliderect(sini):
            if vari==Pallo_sin:
                spawni=random.choice(Spawn_lista)
                vari=random.choice(pallo_lista)
                pallo=pygame.Rect((spawni[0],spawni[1]),(50,50))
                score_arvo+=1
                if (score_arvo==1) or (score_arvo==5) or (score_arvo==10):
                    nopeus+=1
            else:
                valikko("menu",score_arvo)

        if pallo.colliderect(puna):
            if vari==Pallo_pun:
                spawni=random.choice(Spawn_lista)
                vari=random.choice(pallo_lista)
                pallo=pygame.Rect((spawni[0],spawni[1]),(50,50))
                score_arvo+=1
                if (score_arvo==1) or (score_arvo==5) or (score_arvo==10):
                    nopeus+=1
            else:
                valikko("menu",score_arvo)
                
        if pallo.colliderect(lil):
            if vari==Pallo_lila:
                spawni=random.choice(Spawn_lista)
                vari=random.choice(pallo_lista)
                pallo=pygame.Rect((spawni[0],spawni[1]),(50,50))
                score_arvo+=1
                if (score_arvo==1) or (score_arvo==5) or (score_arvo==10):
                    nopeus+=1
            else:
                valikko("menu",score_arvo)
        pygame.display.update()

        if score_paras < score_arvo:
            with open("src/tulokset.txt", "w") as tiedosto:
                tiedosto.write(str(score_arvo))

valikko("aloitus", 0)
pygame.quit()
