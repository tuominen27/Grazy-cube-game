
def hae_paras_score():
    with open("src/tulokset.txt") as tiedosto:
        paras_score = int(tiedosto.read())
    return paras_score