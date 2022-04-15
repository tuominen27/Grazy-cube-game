import unittest
from main import main

class Testit(unittest.TestCase):

    def testi_main(self):
        self.assertEqual(main) is None

if __name__ == '__main__':
    unittest.main()
