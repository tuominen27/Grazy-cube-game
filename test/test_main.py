import unittest
import os
from src.main import putki
#import pygame

class Testit(unittest.TestCase):

    def testi_putki(self):
        self.assertEqual(putki, None)
