import unittest
import json
from unittest.mock import patch
from compression.rle import RLE


class TestRLECompression(unittest.TestCase):

    def setUp(self) -> None:
        self.rle_obj = RLE()
        self.test_input = 'sodaesyn d o b t  hitogii$ a'
        self.test_output = 'sodaesyn d o b t2 hitog2i$ a'

    def test_rle_encode(self):
        """
        Test that it can encode the string
        """
        result = self.rle_obj.encode(self.test_input)
        self.assertEqual(result, self.test_output)

    def test_rle_decode(self):
        """
        Test that it can encode the string
        """
        result = self.rle_obj.decode(self.test_output)
        self.assertEqual(result, self.test_input)

if __name__ == '__main__':
    unittest.main()