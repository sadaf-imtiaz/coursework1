import unittest
from Dec2Hex import decimal_to_hex  # Assuming decimal_to_hex is defined in Dec2Hex.py

class TestDec2Hex(unittest.TestCase):
    def test_positive_number(self):
        """Test for a positive decimal number."""
        self.assertEqual(decimal_to_hex(255), "FF")

    def test_zero(self):
        """Test for zero."""
        self.assertEqual(decimal_to_hex(0), "0")

    def test_negative_number(self):
        """Test for a negative decimal number (optional, based on your logic)."""
        self.assertEqual(decimal_to_hex(-255), "-FF")

    def test_large_number(self):
        """Test for a large decimal number."""
        self.assertEqual(decimal_to_hex(123456789), "75BCD15")

    def test_single_digit(self):
        """Test for a single-digit decimal number."""
        self.assertEqual(decimal_to_hex(9), "9")

    def test_non_integer(self):
        """Test for non-integer input, like strings or floats (based on your logic)."""
        with self.assertRaises(ValueError):
            decimal_to_hex("hello")

if __name__ == "__main__":
    unittest.main()

