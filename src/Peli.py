import pygame
import os
import random
#määritellään värit
valkoinen=(255, 255, 255)
musta = (0, 0, 0)
vihrea = (17, 79, 16)
harmaa=(50, 50, 50) 
punainen=(105, 9, 9) 
sininen=(25, 33, 126) 
keltainen=(255, 255, 0)
lila=(67, 13, 97)
HOVER_COLOR = (50, 70, 90)

#pelin ikkunan koko ja perus muuttujat
LEVEYS, KORKEUS = 800, 800
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Nappaa pallot")
FPS=50
kello=pygame.time.Clock()

#lisätään kuvat ja fontti
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
Putki1=pygame.transform.scale(Putki1, (110,300))
Putki1 = pygame.transform.rotate(Putki1, 45)

Putki2=pygame.image.load(os.path.join("kuvat", "putki.png"))
Putki2=pygame.transform.scale(Putki2, (110,300))
Putki2 = pygame.transform.rotate(Putki2, 140)

Putki3=pygame.image.load(os.path.join("kuvat", "putki.png"))
Putki3=pygame.transform.scale(Putki3, (110,300))
Putki3 = pygame.transform.rotate(Putki3, -45)

Putki4=pygame.image.load(os.path.join("kuvat", "putki.png"))
Putki4=pygame.transform.scale(Putki4, (110,300))
Putki4 = pygame.transform.rotate(Putki4, -134)

Putki_pun=pygame.image.load(os.path.join("kuvat", "Punainen_putki.png"))
Kolmio_pun_rect=pygame.Rect(345,390,40,40)
Kolmio_lila_rect=pygame.Rect(415,390,40,40)
Kolmio_sin_rect=pygame.Rect(415,320,40,40)
Kolmio_vihr_rect=pygame.Rect(347,322,40,40)
kuva_lahde = pygame.image.load(os.path.join("kuvat", "neliö.png"))
kuva_lahde=pygame.transform.scale(kuva_lahde, (310,310))
def piirrokset(pallo,vari):
    naytto.blit(Tausta,(0,0))
    naytto.blit(vari,(pallo.x,pallo.y))
    naytto.blit(Putki1,(650, 650))
    naytto.blit(Putki2,(650, -150))
    naytto.blit(Putki3,(-150, 650))
    naytto.blit(Putki4,(-150,-150))
    naytto.blit(kuva_lahde, (250, 230))

#aloitus sivun koodit
FONT = pygame.font.SysFont ("freesansbold.ttf", 60)
FONT2 = pygame.font.SysFont ("freesansbold.ttf", 100,)
OTSIKKO=FONT2.render("      Pelin nimi", True, valkoinen)
START = FONT.render("START", True, valkoinen)
LEADERBOARD = FONT.render("LEADERBOARD", True, valkoinen)
QUIT = FONT.render("QUIT", True, valkoinen)
rect_otsikko=pygame.Rect(130,100,600,60)
rect1 = pygame.Rect(248,300,325,80)
rect2 = pygame.Rect(248,400,325,80)
rect3 = pygame.Rect(248,500,325,80)
nappaimet = [
    [START, rect1, musta],
    [LEADERBOARD, rect2, musta],
    [QUIT, rect3, musta],]

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
                    print("Eipä ollutkaan")
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

def havita_pallot():
    Pallo_vihr=pygame.transform.scale(Pallo_vihr,(0,0))
    Pallo_pun=pygame.transform.scale(Pallo_pun,(0,0))
    Pallo_lila=pygame.transform.scale(Pallo_lila,(0,0))
    Pallo_sin=pygame.transform.scale(Pallo_sin,(0,0))

def nayta_score(x,y,score_arvo):
    score=font.render("Score: "+ str(score_arvo),True, (255,255,255))
    naytto.blit(score,(x,y))
    pygame.display.update()


#pallojen funktiot ja spwanlista joka ei toimi
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

def putki():
    pass

def main():
    kaynnissa = True
    nopeus=3
    spawni=random.choice(Spawn_lista)
    pallo=pygame.Rect((spawni[0],spawni[1]),(50,50))
    vari=random.choice(pallo_lista)
    score_arvo=0

    kierto = 0

    kuva = kuva_lahde.copy()
    kuva.set_colorkey(musta)

    rect = kuva.get_rect()
    rect.center = (LEVEYS // 2, KORKEUS // 2)

    pressed = 1
    while kaynnissa:
        kello.tick(FPS)
        for tapahtuma in pygame.event.get():
            if tapahtuma.type==pygame.QUIT:
                kaynnissa=False
            if tapahtuma.type == pygame.KEYUP:
                pressed=1
        
        nappain = pygame.key.get_pressed()
        if nappain[pygame.K_LEFT] and pressed==1:
            for x in range(30):
                kierto += 3
                vanha_keskus = rect.center
                uusi_kuva = pygame.transform.rotate(kuva_lahde, kierto)
                rect = uusi_kuva.get_rect()
                rect.center = vanha_keskus
                naytto.blit(uusi_kuva, rect)
                
                pygame.display.flip()
            pressed = 2
        if nappain[pygame.K_RIGHT] and pressed==1:
            for x in range(30):
                kierto -= 3
                vanha_keskus = rect.center
                uusi_kuva = pygame.transform.rotate(kuva_lahde, kierto)
                rect = uusi_kuva.get_rect()
                rect.center = vanha_keskus
                naytto.blit(uusi_kuva, rect)
                
                pygame.display.flip()
            pressed=2
    
        vanha_keskus = rect.center
        uusi_kuva = pygame.transform.rotate(kuva_lahde, kierto)
        rect = uusi_kuva.get_rect()
        rect.center = vanha_keskus
            
        vihr=pygame.draw.rect(naytto,vihrea, Kolmio_vihr_rect)
        sini=pygame.draw.rect(naytto,sininen, Kolmio_sin_rect)
        puna=pygame.draw.rect(naytto,punainen, Kolmio_pun_rect)
        lil=pygame.draw.rect(naytto,lila, Kolmio_lila_rect)
        Pallo(pallo,nopeus,spawni)
        piirrokset(pallo, vari)
        nayta_score(330,10,score_arvo)
        if pallo.colliderect(vihr):
            if vari==Pallo_vihr:
                spawni=random.choice(Spawn_lista)
                vari=random.choice(pallo_lista)
                pallo=pygame.Rect((spawni[0],spawni[1]),(50,50))
                score_arvo+=1
                if (score_arvo==1) or (score_arvo==2) or (score_arvo==4) or (score_arvo==6) or (score_arvo==8) or (score_arvo==11):
                    nopeus+=1
            else:
                valikko("menu",score_arvo)
        if pallo.colliderect(sini):
            if vari==Pallo_sin:
                spawni=random.choice(Spawn_lista)
                vari=random.choice(pallo_lista)
                pallo=pygame.Rect((spawni[0],spawni[1]),(50,50))
                score_arvo+=1
                if (score_arvo==1) or (score_arvo==2) or (score_arvo==4) or (score_arvo==6) or (score_arvo==8) or (score_arvo==11):
                    nopeus+=1
            else:
                valikko("menu",score_arvo)
        if pallo.colliderect(puna):
            if vari==Pallo_pun:
                spawni=random.choice(Spawn_lista)
                vari=random.choice(pallo_lista)
                pallo=pygame.Rect((spawni[0],spawni[1]),(50,50))
                score_arvo+=1
                if (score_arvo==1) or (score_arvo==2) or (score_arvo==4) or (score_arvo==6) or (score_arvo==8) or (score_arvo==11):
                    nopeus+=1
            else:
                valikko("menu",score_arvo)
        if pallo.colliderect(lil):
            if vari==Pallo_lila:
                spawni=random.choice(Spawn_lista)
                vari=random.choice(pallo_lista)
                pallo=pygame.Rect((spawni[0],spawni[1]),(50,50))
                score_arvo+=1
                if (score_arvo==1) or (score_arvo==2) or (score_arvo==4) or (score_arvo==6) or (score_arvo==8) or (score_arvo==11):
                    nopeus+=1
            else:
                valikko("menu",score_arvo)
      #if pallo.colliderect(pahis):
         #pahis=pygame.Rect(int(random.choice(spawnlist)),int(random.choice(spawnlist)),30,30)
         #nopeus+=0.1
         #score_arvo+=1
      #if kusee pelin niin valikko("menu",score_arvo)

valikko("aloitus", 0)
pygame.quit()