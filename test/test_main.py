import unittest
from src import main
import pygame

class Testit(unittest.TestCase):

    def testi1(self):
        self.assertEqual(main.putki, None)
