import unittest
import json
from unittest.mock import patch
from compression.bwt import BWT


class TestBWTCompression(unittest.TestCase):

    def setUp(self) -> None:
        self.BWT_obj = BWT()
        self.test_compressed_str_length_input = 'DOGWOOD$'
        self.test_compressed_str_length_output = 'DO$OODWG'

    def test_compressed_str_length(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = self.BWT_obj.transform(self.test_compressed_str_length_input)
        self.assertEqual(result, self.test_compressed_str_length_output)

if __name__ == '__main__':
    unittest.main()