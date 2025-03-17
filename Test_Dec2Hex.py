import sys
import os

# Add current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Dex2Hex import decimal_to_hex  # Now it should work!
import unittest

class TestDex2Hex(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(decimal_to_hex(255), "FF")

    def test_zero(self):
        self.assertEqual(decimal_to_hex(0), "0")

if __name__ == "__main__":
    unittest.main()
