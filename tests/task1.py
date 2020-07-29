from unittest import TestCase
from functions.gcd import gcd
class GcdFunctionTestCase(TestCase):
    def test_gcd_10_and_5_is_5(self):
        self.assertEqual(5,gcd(10,5))
    def test_gcd_33_and_27_is3(self):
        self.assertEqual(3, gcd(33, 27))
    def test_gcd_99_and_45_is_9(self):
        self.assertEqual(9, gcd(99, 45))
        # assertEqual(1, gcd(97, 23))
        # assertEqual(10, gcd(10, 100))