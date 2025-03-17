import unittest
from Dex2Hex import decimal_to_hex

class TestDex2Hex(unittest.TestCase):
    """Unit tests for the decimal_to_hex function."""

    def test_positive_number(self):
        """Test conversion of a positive number."""
        self.assertEqual(decimal_to_hex(10), "A")

    def test_zero(self):
        """Test conversion of zero."""
        self.assertEqual(decimal_to_hex(0), "0")

    def test_large_number(self):
        """Test conversion of a large number."""
        self.assertEqual(decimal_to_hex(255), "FF")

    def test_negative_number(self):
        """Test that negative numbers raise an error."""
        with self.assertRaises(ValueError):
            decimal_to_hex(-5)

if __name__ == "__main__":
    unittest.main()
