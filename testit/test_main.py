from src.hae_paras_score import hae_paras_score
import unittest

class Testit(unittest.TestCase):
    
    def test_hae_paras_score(self):
        testiarvo = 17
        with open("src/tulokset.txt", "w") as tiedosto:
            tiedosto.write(str(testiarvo))

        funktion_palauttama_arvo = hae_paras_score()
        self.assertEqual(testiarvo,funktion_palauttama_arvo)
