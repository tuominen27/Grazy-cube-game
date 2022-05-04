from src.Peli import hae_paras_score
import unittest
import pygame

class Testit(unittest.TestCase):
    
    def hae_paras_score_test(self):
        testiarvo = 17
        with open("src/tulokset.txt", "w") as tiedosto:
            tiedosto.write(str(testiarvo))

        funktion_palauttama_arvo = hae_paras_score()
        self.assertEqual(testiarvo,funktion_palauttama_arvo)
