import unittest
import json
from unittest.mock import patch
from compression.rle import RLE


class TestRLECompression(unittest.TestCase):

    def setUp(self) -> None:
        self.rle_obj = RLE()
        self.test_compressed_str_length_input = list('aabbbbbbbccd')
        self.test_compressed_str_length_output = 7

    def test_compressed_str_length(self):
        """
        Test that it can encode the string
        """
        data = [1, 2, 3]
        result = self.rle_obj.compress(self.test_compressed_str_length_input)
        self.assertEqual(result, self.test_compressed_str_length_output)

if __name__ == '__main__':
    unittest.main()