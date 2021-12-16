import unittest
import sys, os
from builder import *

sys.path.append(os.getcwd())


class Service_Builder_Test(unittest.TestCase):
    director = Director()
    builder = Service_Builder()
    director.builder = builder

    def test_Luminarc_builder(self):
       print("\nLuminarc: ")
       self.director.Luminarc()
       self.builder.product.list_parts()

    def test_AnnaLafargue_builder(self):
        print("\nАнна Лафарг: ")
        self.director.AnnaLafargue()
        self.builder.product.list_parts()


if __name__ == "__main__":
    unittest.main()