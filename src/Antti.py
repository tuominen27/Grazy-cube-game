import pygame

# Määritellään neliön koko
leveys = 500
korkeus = 500
fps = 30

#määritellään värit
musta = (0, 0, 0)
vihrea = (0, 255, 0)

pygame.init()
naytto = pygame.display.set_mode((leveys, korkeus))
clock = pygame.time.Clock()


kierto = 0
kierto_nopeus = 0

kuva_lahde = pygame.Surface((100, 100))

kuva_lahde.set_colorkey(musta)

kuva_lahde.fill(vihrea)

kuva = kuva_lahde.copy()
kuva.set_colorkey(musta)

rect = kuva.get_rect()
rect.center = (leveys // 2, korkeus // 2)

kaynnissa = True
while kaynnissa:
    clock.tick(fps)

    naytto.fill(musta)

    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            kaynnissa = False
    
    nappain = pygame.key.get_pressed()
    if nappain[pygame.K_LEFT]:
        kierto_nopeus = 2

    vanha_keskus = rect.center

    kierto = (kierto + kierto_nopeus) % 360

    uusi_kuva = pygame.transform.rotate(kuva_lahde, kierto)
    rect = uusi_kuva.get_rect()

    rect.center = vanha_keskus
    if nappain[pygame.K_RIGHT]:
        kierto_nopeus = 0

    naytto.blit(uusi_kuva, rect)

    pygame.display.flip()

pygame.quit()
