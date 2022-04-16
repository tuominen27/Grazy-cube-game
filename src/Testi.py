import pygame
import os
# Määritellään neliön koko
leveys = 800
korkeus = 800
fps = 60

#määritellään värit
musta = (0, 0, 0)
vihrea = (0, 255, 0)

pygame.init()
naytto = pygame.display.set_mode((leveys, korkeus))
clock = pygame.time.Clock()


kierto = 0
kierto_nopeus = 0

kuva_lahde = pygame.image.load(os.path.join("kuvat", "neliö.png"))
kuva_lahde=pygame.transform.scale(kuva_lahde, (310,310))

kuva = kuva_lahde.copy()
kuva.set_colorkey(musta)

rect = kuva.get_rect()
rect.center = (leveys // 2, korkeus // 2)

kaynnissa = True
pressed=1
while kaynnissa:
    clock.tick(fps)

    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            kaynnissa = False

    nappain = pygame.key.get_pressed()
    if nappain[pygame.K_LEFT] and pressed==1:
       for x in range(30):
          naytto.fill(musta)
          kierto += 3
          vanha_keskus = rect.center
          uusi_kuva = pygame.transform.rotate(kuva_lahde, kierto)
          rect = uusi_kuva.get_rect()
          rect.center = vanha_keskus
          naytto.blit(uusi_kuva, rect)
          pygame.display.flip()
    
    if nappain[pygame.K_RIGHT] and pressed==1:
       for x in range(30):
            naytto.fill(musta)
            kierto -= 3
            vanha_keskus = rect.center
            uusi_kuva = pygame.transform.rotate(kuva_lahde, kierto)
            rect = uusi_kuva.get_rect()
            rect.center = vanha_keskus
            naytto.blit(uusi_kuva, rect)
            pygame.display.flip()
    pressed = 2
    if tapahtuma.type == pygame.KEYUP:
        pressed=1 

    vanha_keskus = rect.center


    uusi_kuva = pygame.transform.rotate(kuva_lahde, kierto)
    rect = uusi_kuva.get_rect()

    rect.center = vanha_keskus

    naytto.blit(uusi_kuva, rect)

    pygame.display.flip()

pygame.quit()