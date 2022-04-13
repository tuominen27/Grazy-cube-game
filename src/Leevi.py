import pygame
import os

#määritellään värit
musta = (0, 0, 0)
vihrea = (0, 255, 0)
harmaa=(50, 50, 50) 
punainen=(255, 0, 0) 
vihrea=(0, 255, 0) 
sininen=(0, 0, 255) 
keltainen=(255, 255, 0) 

#pelin ikkunan koko ja perus muuttujat
LEVEYS, KORKEUS = 800, 800
naytto = pygame.display.set_mode((LEVEYS, KORKEUS))
pygame.display.set_caption("Nappaa pallot")
FPS=40
kello=pygame.time.Clock()

#lisätään kuvat ja fontti
pygame.init()
font=pygame.font.Font("freesansbold.ttf",32)

Tausta=pygame.image.load(os.path.join("kuvat", "Tausta.PNG"))
Tausta=pygame.transform.scale(Tausta, (800,800))

Pallo_vihr=pygame.image.load(os.path.join("kuvat", "Vihree_pallo.png"))
Pallo_sin=pygame.image.load(os.path.join("kuvat", "Sininen_pallo.png"))
Pallo_lila=pygame.image.load(os.path.join("kuvat", "lila_pallo.png"))
Pallo_pun=pygame.image.load(os.path.join("kuvat", "punanen_pallo.png"))

Kolmio_vihr=pygame.image.load(os.path.join("kuvat", "vihree.png"))
Kolmio_vihr=pygame.transform.scale(Kolmio_vihr, (110,110))

Kolmio_sin=pygame.image.load(os.path.join("kuvat", "sininen.png"))
Kolmio_sin=pygame.transform.scale(Kolmio_sin, (110,110))

Kolmio_lila=pygame.image.load(os.path.join("kuvat", "lila.png"))
Kolmio_lila=pygame.transform.scale(Kolmio_lila, (110,110))

Kolmio_pun=pygame.image.load(os.path.join("kuvat", "punanen.png"))
Kolmio_pun=pygame.transform.scale(Kolmio_pun, (110,110))

 
Putki1=pygame.image.load(os.path.join("kuvat", "putki.png"))
Putki1=pygame.transform.scale(Putki1, (100,300))
Putki1 = pygame.transform.rotate(Putki1, 45)

Putki2=pygame.image.load(os.path.join("kuvat", "putki.png"))
Putki2=pygame.transform.scale(Putki2, (100,300))
Putki2 = pygame.transform.rotate(Putki2, 140)

Putki3=pygame.image.load(os.path.join("kuvat", "putki.png"))
Putki3=pygame.transform.scale(Putki3, (100,300))
Putki3 = pygame.transform.rotate(Putki3, -45)

Putki4=pygame.image.load(os.path.join("kuvat", "putki.png"))
Putki4=pygame.transform.scale(Putki4, (100,300))
Putki4 = pygame.transform.rotate(Putki4, -135)

Putki_pun=pygame.image.load(os.path.join("kuvat", "Punainen_putki.png"))



def piirrokset(Tausta, Putki1, Putki2, Putki3, Putki4, Kolmio_vihr, Kolmio_pun, Kolmio_lila, Kolmio_sin,):
      naytto.blit(Tausta,(0,0))
      naytto.blit(Putki1,(650, 650))
      naytto.blit(Putki2,(650, -150))
      naytto.blit(Putki3,(-150, 650))
      naytto.blit(Putki4,(-150,-150))
      naytto.blit(Kolmio_vihr,(300,275))
      naytto.blit(Kolmio_pun,(300,383))
      naytto.blit(Kolmio_sin,(410,275))
      naytto.blit(Kolmio_lila,(409,383))
      pygame.display.update()

def pyorita():
    pass

def valikko():
    pass

def putki():
    pass


def main():
   kaynnissa = True
   while kaynnissa:
      kello.tick(FPS)
      for event in pygame.event.get():
         if event.type==pygame.QUIT:
            kaynnissa=False
      piirrokset(Tausta, Putki1, Putki2, Putki3, Putki4, Kolmio_vihr, Kolmio_pun, Kolmio_lila, Kolmio_sin,)
      pygame.display.update()
main()
pygame.quit()